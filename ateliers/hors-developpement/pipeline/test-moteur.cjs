const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const {Pipeline, validerExtraction, validerEtat} = require('./moteur.js');
const donnees = require('./donnees.js');
const exemple = () => structuredClone(donnees.exemple);
const prepare = () => {
  const pipeline = new Pipeline();
  pipeline.changerExtraction(JSON.stringify(exemple(), null, 2));
  pipeline.controler();
  return pipeline;
};
const refuse = mutation => {
  const extraction = exemple();
  mutation(extraction);
  assert.throws(() => validerExtraction(extraction));
};

test('les neuf sources intégrées reproduisent les fichiers fournis', () => {
  assert.equal(Object.keys(donnees.sources).length, 9);
  for (const [nom, contenu] of Object.entries(donnees.sources)) {
    const vrai = fs.readFileSync(path.join(__dirname, '..', 'entrees', nom), 'utf8');
    assert.equal(contenu, vrai, nom);
  }
  assert.equal(donnees.sources['courriels/01-nora.txt'], donnees.sources['courriels/03-copie-nora.txt']);
});

test('la démonstration est explicitement fictive et M004 est seul connu au départ', () => {
  assert.equal(validerExtraction(exemple()).origine, 'exemple_fictif');
  const pipeline = new Pipeline();
  assert.deepEqual(pipeline.etat.connus, ['M004']);
  pipeline.changerExtraction(JSON.stringify(exemple()));
  assert.deepEqual(pipeline.controler().nouveaux, ['M001', 'M002', 'M005']);
  assert.deepEqual(pipeline.etat.connus, ['M004']);
  assert.match(pipeline.etat.brouillon.point, /03-copie-nora/);
});

test('les champs obligatoires, versions, types et valeurs inconnues sont refusés', () => {
  refuse(e => { delete e.origine; });
  refuse(e => { e.envoi = true; });
  refuse(e => { e.version = '1'; });
  refuse(e => { e.lot = 'autre-lot'; });
  refuse(e => { e.origine = 'modèle_testé'; });
  refuse(e => { e.alertes = ['']; });
  refuse(e => { e.messages[0].inconnu = 'test'; });
  refuse(e => { e.messages[0].type = 'confirmation'; });
  refuse(e => { e.messages[0].atelier = 'Peinture'; });
});

test('les places en texte, zéro, fraction ou nombre excessif sont refusées ; null reste admis', () => {
  for (const value of ['deux', 0, -1, 1.5, Number.MAX_SAFE_INTEGER + 1]) {
    refuse(e => { e.messages[1].places = value; });
  }
  const extraction = exemple();
  extraction.messages[1].places = null;
  assert.equal(validerExtraction(extraction).messages[1].places, null);
});

test('les identifiants manquants, inconnus et répétés sont refusés', () => {
  refuse(e => { e.messages.pop(); });
  refuse(e => { e.messages[1].id = 'M099'; });
  refuse(e => { e.messages[1] = {...e.messages[0]}; });
});

test('chaque référence est liée à son identifiant et chaque extrait existe exactement', () => {
  refuse(e => { e.messages[0].source = 'courriels/02-leo.txt'; });
  refuse(e => { e.messages[0].source = '../../secret.txt'; });
  refuse(e => { e.messages[1].extrait = 'Je choisis Reliure.'; });
  refuse(e => { e.messages[1].extrait = ' '; });
  refuse(e => { e.messages[0].extrait = e.messages[0].extrait.replace('\n', ' '); });
});

test('un extrait réel ne prouve pas la fidélité de tous les champs', () => {
  const extraction = exemple();
  extraction.messages[1].atelier = 'Reliure';
  assert.equal(validerExtraction(extraction).messages[1].atelier, 'Reliure');
  // Le message de Léo ne précise aucun atelier : c’est le contre-exemple humain du cours.
  assert.equal(donnees.sources['courriels/02-leo.txt'].includes('Reliure'), false);
});

test('date et horaire non arbitrés restent null ; M005 reste une question sans place', () => {
  refuse(e => { e.date_evenement = '17 octobre 2026'; });
  refuse(e => { e.horaire_cartographie = '14 h'; });
  refuse(e => { e.messages[3].type = 'inscription'; });
  refuse(e => { e.messages[3].places = 2; });
});

test('une approbation exige un contrôle réussi et une relecture humaine explicite', () => {
  const pipeline = new Pipeline();
  assert.throws(() => pipeline.approuver(true));
  pipeline.changerExtraction(JSON.stringify(exemple()));
  pipeline.controler();
  assert.throws(() => pipeline.approuver(false));
  assert.throws(() => pipeline.pointApprouve());
  pipeline.approuver(true);
  assert.equal(pipeline.estApprouve(), true);
  assert.deepEqual(pipeline.etat.connus, ['M004']);
});

test('modifier puis rétablir le point ne rétablit jamais l’accord précédent', () => {
  const pipeline = prepare();
  pipeline.approuver(true);
  const avant = pipeline.etat.brouillon.point;
  pipeline.changerPoint(avant + '\nModification');
  assert.equal(pipeline.estApprouve(), false);
  pipeline.changerPoint(avant);
  assert.equal(pipeline.estApprouve(), false);
  assert.throws(() => pipeline.marquerExport());
  pipeline.approuver(true);
  assert.equal(pipeline.estApprouve(), true);
});

test('changer l’extraction retire immédiatement accord et préparation, avant tout contrôle', () => {
  const pipeline = prepare();
  pipeline.approuver(true);
  const avant = pipeline.etat.brouillon.extraction;
  pipeline.changerExtraction(avant + ' ');
  assert.equal(pipeline.estApprouve(), false);
  assert.equal(pipeline.peutApprouver(), false);
  assert.throws(() => pipeline.marquerExport());
  pipeline.changerExtraction(avant);
  assert.throws(() => pipeline.approuver(true));
  pipeline.controler();
  pipeline.approuver(true);
  assert.equal(pipeline.estApprouve(), true);
});

test('un contrôle échoué retire l’accord, sans inscrire de message', () => {
  const pipeline = prepare();
  pipeline.approuver(true);
  pipeline.changerExtraction('{ pas JSON');
  assert.throws(() => pipeline.controler());
  assert.equal(pipeline.estApprouve(), false);
  assert.deepEqual(pipeline.etat.connus, ['M004']);
});

test('seul l’export du point marque les trois messages ; l’état et l’approbation ne le font pas', () => {
  const pipeline = prepare();
  pipeline.approuver(true);
  pipeline.exporterEtat();
  assert.deepEqual(pipeline.etat.connus, ['M004']);
  pipeline.marquerExport();
  assert.deepEqual(pipeline.etat.connus, ['M001', 'M002', 'M004', 'M005']);
  assert.deepEqual(pipeline.etat.rapports[0].messages, ['M001', 'M002', 'M005']);
  assert.throws(() => pipeline.marquerExport());
});

test('reprise et rejeu n’ajoutent aucun deuxième rapport et ne reprennent aucun accord', () => {
  const pipeline = prepare();
  pipeline.approuver(true);
  pipeline.marquerExport();
  const sauvegarde = pipeline.exporterEtat();
  const reprise = new Pipeline();
  reprise.reprendre(sauvegarde);
  assert.equal(reprise.estApprouve(), false);
  assert.deepEqual(reprise.controler().nouveaux, []);
  assert.equal(reprise.etat.rapports.length, 1);
  assert.throws(() => reprise.approuver(true));
  assert.throws(() => reprise.marquerExport());
});

test('un brouillon peut être sauvegardé sans être déclaré traité ou approuvé', () => {
  const pipeline = prepare();
  pipeline.changerPoint('Mon point à continuer');
  const reprise = new Pipeline();
  reprise.reprendre(pipeline.exporterEtat());
  assert.equal(reprise.etat.brouillon.point, 'Mon point à continuer');
  assert.deepEqual(reprise.etat.connus, ['M004']);
  assert.equal(reprise.peutApprouver(), false);
});

test('les états incohérents sont refusés et la session précédente est conservée', () => {
  const pipeline = prepare();
  const avant = structuredClone(pipeline.etat);
  for (const mutation of [
    e => { e.lot = 'autre'; },
    e => { e.connus.push('M001'); },
    e => { e.connus = []; },
    e => { e.connus.push('M004'); },
    e => { e.approbation = true; },
    e => { e.brouillon.extraction = 42; },
    e => { e.journal[0].action = 'envoyer'; },
    e => { e.journal[0].numero = -1; }
  ]) {
    const faux = structuredClone(avant);
    mutation(faux);
    assert.throws(() => pipeline.reprendre(JSON.stringify(faux)));
    assert.deepEqual(pipeline.etat, avant);
  }
});

test('un rapport contenant une référence forgée ou un traitement doublé est refusé', () => {
  const pipeline = prepare();
  pipeline.approuver(true);
  pipeline.marquerExport();
  const etat = JSON.parse(pipeline.exporterEtat());
  const faux = structuredClone(etat);
  faux.rapports[0].extraction.messages[0].source = '../../hors-dossier';
  assert.throws(() => validerEtat(faux));
  etat.rapports.push({...structuredClone(etat.rapports[0]), numero: 2});
  assert.throws(() => validerEtat(etat));
});

test('les noms de propriétés inattendus et les entrées trop longues sont refusés', () => {
  const pipeline = prepare();
  const state = JSON.parse(pipeline.exporterEtat());
  Object.defineProperty(state, '__proto__', {value: {pollue: true}, enumerable: true});
  assert.throws(() => pipeline.reprendre(JSON.stringify(state)));
  assert.equal({}.pollue, undefined);
  assert.throws(() => pipeline.reprendre(' '.repeat(512001)));
  assert.throws(() => pipeline.changerExtraction('x'.repeat(64001)));
});

// SPDX-License-Identifier: GPL-3.0-only
// Contrôles du JSON exporté et de ses deux nœuds Code, hors moteur n8n.
const assert = require('node:assert/strict');
const { readFileSync } = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const { test } = require('node:test');

const workflow = JSON.parse(readFileSync(path.join(__dirname, 'point-equipe.json'), 'utf8'));
const node = name => workflow.nodes.find(item => item.name === name);
const exemple = () => JSON.parse(node('Extraction fictive ou collée').parameters.jsonOutput);
function executer(name, items) {
  const code = node(name).parameters.jsCode;
  const result = new vm.Script('(function () {\n' + code + '\n})()').runInNewContext(
    { $input: { all: () => structuredClone(items) } }, { timeout: 1000 }
  );
  return JSON.parse(JSON.stringify(result));
}
const controler = extraction => executer('Contrôler le lot', [{ json: extraction }]);
const traiter = extraction => executer('Préparer le point interne', controler(extraction));
function refuse(mutateur, message) {
  const extraction = exemple();
  mutateur(extraction);
  assert.throws(() => controler(extraction), message);
}

test('export manuel inactif, sans credential ni nœud d’action extérieure', () => {
  assert.equal(workflow.active, false);
  assert.deepEqual(workflow.nodes.map(item => [item.type, item.typeVersion]), [
    ['n8n-nodes-base.manualTrigger', 1], ['n8n-nodes-base.set', 3.4],
    ['n8n-nodes-base.code', 2], ['n8n-nodes-base.code', 2]
  ]);
  assert.deepEqual(workflow.pinData, {});
  for (const item of workflow.nodes) {
    assert.equal(Object.hasOwn(item, 'credentials'), false);
    assert.equal(item.continueOnFail, undefined);
    if (item.parameters.jsCode) {
      assert.doesNotMatch(item.parameters.jsCode, /\b(?:fetch|require|eval|XMLHttpRequest)\s*\(/);
    }
  }
  for (let i = 0; i < workflow.nodes.length - 1; i++) {
    assert.deepEqual(workflow.connections[workflow.nodes[i].name].main, [[
      { node: workflow.nodes[i + 1].name, type: 'main', index: 0 }
    ]]);
  }
});

test('le corpus incorporé correspond exactement aux messages sur disque', () => {
  const prefixe = node('Contrôler le lot').parameters.jsCode.split('function refuser')[0];
  const sources = new vm.Script('(function () {\n' + prefixe + '\nreturn sources; })()')
    .runInNewContext({}, { timeout: 1000 });
  for (const source of Object.values(sources)) {
    assert.equal(source.texte, readFileSync(path.join(__dirname, '..', source.source), 'utf8'));
  }
  assert.equal(
    readFileSync(path.join(__dirname, '../entrees/courriels/01-nora.txt'), 'utf8'),
    readFileSync(path.join(__dirname, '../entrees/courriels/03-copie-nora.txt'), 'utf8')
  );
});

test('la démo conserve les inconnues et produit trois messages nouveaux', () => {
  const extraction = exemple();
  assert.equal(extraction.origine, 'exemple_fictif');
  assert.equal(extraction.date_evenement, null);
  assert.equal(extraction.horaire_cartographie, null);
  assert.equal(extraction.messages.find(message => message.id === 'M002').atelier, null);
  const sortie = traiter(extraction)[0].json;
  assert.deepEqual(sortie.nouveaux, ['M001', 'M002', 'M005']);
  assert.deepEqual(sortie.deja_connus, ['M004']);
  assert.equal(sortie.statut, 'proposition_interne_non_approuvee');
  assert.equal(sortie.action_exterieure, false);
  assert.equal(sortie.persistance, false);
  assert.match(sortie.point_interne, /M002 \| inscription \| non précisé \| 2/);
  assert.match(sortie.point_interne, /M005 \| question \| Cartographie \| sans objet/);
});

test('une extraction réelle peut déclarer son origine sans contourner les contrôles', () => {
  const extraction = exemple();
  extraction.origine = 'assistant';
  assert.equal(traiter(extraction)[0].json.origine, 'assistant');
  extraction.messages[0].source = 'autre.txt';
  assert.throws(() => traiter(extraction), /source incorrecte/);
});

test('les champs absents, supplémentaires et mauvais types sont refusés', () => {
  refuse(extraction => { delete extraction.lot; }, /champs absents ou inconnus/);
  refuse(extraction => { extraction.approuve = true; }, /champs absents ou inconnus/);
  refuse(extraction => { extraction.messages[0].commande = 'envoyer'; }, /champs absents ou inconnus/);
  refuse(extraction => { extraction.messages = 'M001'; }, /quatre messages/);
  refuse(extraction => { extraction.alertes = ['']; }, /alertes doit être/);
});

test('l’entrée doit contenir un seul item n8n', () => {
  assert.throws(() => executer('Contrôler le lot', []), /un seul objet/);
  assert.throws(() => executer('Contrôler le lot', [{ json: exemple() }, { json: exemple() }]), /un seul objet/);
});

test('lot inconnu et versions incompatibles sont refusés', () => {
  refuse(extraction => { extraction.lot = 'quartier-02'; }, /version ou lot inconnu/);
  refuse(extraction => { extraction.version = '1'; }, /version ou lot inconnu/);
});

test('un message manquant, inconnu ou répété bloque le lot', () => {
  refuse(extraction => { extraction.messages.pop(); }, /quatre messages/);
  refuse(extraction => { extraction.messages[0].id = 'M999'; }, /identifiant inconnu/);
  refuse(extraction => { extraction.messages[1] = { ...extraction.messages[0] }; }, /identifiant répété/);
});

test('une source déplacée ou une citation inventée bloque le lot', () => {
  refuse(extraction => { extraction.messages[0].source = extraction.messages[1].source; }, /source incorrecte/);
  refuse(extraction => { extraction.messages[0].extrait = 'Je réserve neuf places.'; }, /extrait absent/);
  refuse(extraction => { extraction.messages[0].extrait = ' '; }, /extrait absent/);
});

test('date tranchée et horaire inventé restent refusés pour ce lot non arbitré', () => {
  refuse(extraction => { extraction.date_evenement = '2026-10-17'; }, /restent à arbitrer/);
  refuse(extraction => { extraction.horaire_cartographie = '14 h'; }, /restent à arbitrer/);
});

test('quantités négatives, fractionnaires ou textuelles sont refusées', () => {
  for (const quantite of [-1, 0, 1.5, '2']) {
    refuse(extraction => { extraction.messages[0].places = quantite; }, /entier positif ou null/);
  }
});

test('M005 ne devient ni inscription ni place supplémentaire', () => {
  refuse(extraction => { extraction.messages[3].places = 1; }, /question n’ajoute aucune place/);
  refuse(extraction => { extraction.messages[3].type = 'inscription'; }, /M005 reste une question/);
});

test('la limite sémantique reste visible : une quantité fausse mais bien formée passe', () => {
  const extraction = exemple();
  extraction.messages[0].places = 9;
  assert.match(traiter(extraction)[0].json.point_interne, /M001 \| inscription \| Reliure \| 9/);
  // La citation n’a pas changé et dit bien « deux personnes » : relecture indispensable.
});

test('les alertes extraites restent du texte, sans lien ou HTML actif ajouté au point', () => {
  const extraction = exemple();
  extraction.alertes = ['<script>envoyer()</script> [ouvrir](https://exemple.invalid)'];
  assert.match(traiter(extraction)[0].json.point_interne, /\\<script\\>/);
  assert.doesNotMatch(traiter(extraction)[0].json.point_interne, /\[ouvrir\]\(/);
});

test('relancer refait la même proposition et ne simule pas un suivi durable', () => {
  assert.deepEqual(traiter(exemple()), traiter(exemple()));
});

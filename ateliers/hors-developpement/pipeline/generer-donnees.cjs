/* À relancer uniquement si les sources de l'exercice changent : node generer-donnees.cjs */
const fs = require('node:fs');
const path = require('node:path');
const base = path.resolve(__dirname, '..');
const paths = [
  'courriels/01-nora.txt', 'courriels/02-leo.txt', 'courriels/03-copie-nora.txt',
  'courriels/04-samir.txt', 'courriels/05-question-nora.txt',
  'reunions/01-preparation.md', 'reunions/02-communication.md', 'suivi-initial.csv'
];
const sources = Object.fromEntries(paths.map(p => [p, fs.readFileSync(path.join(base, 'entrees', p), 'utf8')]));
sources['../regles-equipe.md'] = fs.readFileSync(path.join(base, 'regles-equipe.md'), 'utf8');
const data = {sources, fichiers: {
  M001: 'courriels/01-nora.txt', M002: 'courriels/02-leo.txt',
  M004: 'courriels/04-samir.txt', M005: 'courriels/05-question-nora.txt'
}, exemple: {
  version: 1, lot: 'quartier-01', origine: 'exemple_fictif',
  messages: [
    {id: 'M001', type: 'inscription', atelier: 'Reliure', places: 2, source: 'courriels/01-nora.txt', extrait: 'Nous aimerions participer à l’atelier Reliure. Pouvez-vous noter\nune demande pour deux personnes ?'},
    {id: 'M002', type: 'inscription', atelier: null, places: 2, source: 'courriels/02-leo.txt', extrait: 'Je voudrais m’inscrire avec un ami : une place pour lui et une pour moi.'},
    {id: 'M004', type: 'inscription', atelier: 'Reliure', places: 1, source: 'courriels/04-samir.txt', extrait: 'Je souhaite participer à l’atelier Reliure, pour une personne.'},
    {id: 'M005', type: 'question', atelier: 'Cartographie', places: null, source: 'courriels/05-question-nora.txt', extrait: 'À quelle heure commence l’atelier Cartographie ? Je pose la question\npour savoir si je pourrai passer le voir ; ma demande d’inscription\nporte toujours sur les deux places en Reliure.'}
  ], date_evenement: null, horaire_cartographie: null,
  alertes: [
    'Date à clarifier avec Camille : le 10 octobre dans CR01 et le 17 octobre sur le projet d’affiche de CR02.',
    'Horaire de Cartographie absent dans CR01 et CR02.',
    'Atelier de Léo non précisé dans M002.',
    '03-copie-nora.txt est la copie identique de M001 ; M004 figure déjà dans le suivi initial.'
  ]
}};
const output = '/* Généré depuis les fichiers du dossier. Démonstration fictive, sans appel à un modèle. */\n' +
  '(function (root) {\n  "use strict";\n  const donnees = ' + JSON.stringify(data, null, 2) + ';\n' +
  '  if (typeof module === "object" && module.exports) module.exports = donnees;\n' +
  '  else root.DonneesAtelier = donnees;\n})(typeof globalThis !== "undefined" ? globalThis : this);\n';
fs.writeFileSync(path.join(__dirname, 'donnees.js'), output);

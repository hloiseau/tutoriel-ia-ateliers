(function (root) {
  'use strict';
  const donnees = typeof module === 'object' && module.exports ? require('./donnees.js') : root.DonneesAtelier;
  const IDS = ['M001', 'M002', 'M004', 'M005'];
  const MAX_TEXTE = 64000;
  const ACTIONS = ['initialisation', 'extraction_modifiee', 'point_modifie', 'controle_refuse', 'point_prepare',
    'rejeu_sans_nouveaute', 'approbation', 'point_exporte', 'etat_exporte', 'reprise'];
  const copie = value => JSON.parse(JSON.stringify(value));
  function exigence(condition, message) { if (!condition) throw new Error(message); }
  function objet(value, keys, label) {
    exigence(value !== null && typeof value === 'object' && !Array.isArray(value), label + ' doit être un objet.');
    const actual = Object.keys(value).sort();
    exigence(JSON.stringify(actual) === JSON.stringify([...keys].sort()), label + ' : champs manquants ou inconnus.');
  }
  function texte(value, label, max = MAX_TEXTE, vide = false) {
    exigence(typeof value === 'string' && value.length <= max && (vide || value.trim().length > 0), label + ' : texte absent, trop long ou invalide.');
  }
  function lireJSON(raw, label) {
    texte(raw, label, 512000);
    try { return JSON.parse(raw); } catch (_) { throw new Error(label + ' : JSON illisible.'); }
  }
  function validerExtraction(value) {
    objet(value, ['version', 'lot', 'origine', 'messages', 'date_evenement', 'horaire_cartographie', 'alertes'], 'Extraction');
    exigence(value.version === 1 && value.lot === 'quartier-01', 'Version ou lot non reconnu. Cet outil attend quartier-01, version 1.');
    exigence(['exemple_fictif', 'manuel', 'assistant'].includes(value.origine), 'Origine non reconnue.');
    exigence(value.date_evenement === null && value.horaire_cartographie === null,
      'La date et l’horaire restent à null : ce lot contient des décisions non arbitrées.');
    exigence(Array.isArray(value.alertes) && value.alertes.length <= 30, 'Alertes : une liste de 30 textes au maximum est attendue.');
    value.alertes.forEach(t => texte(t, 'Alerte', 2000));
    exigence(Array.isArray(value.messages) && value.messages.length === 4, 'Le lot doit contenir exactement M001, M002, M004 et M005.');
    const seen = new Set();
    for (const message of value.messages) {
      objet(message, ['id', 'type', 'atelier', 'places', 'source', 'extrait'], 'Message');
      exigence(IDS.includes(message.id) && !seen.has(message.id), 'Identifiant inconnu ou répété.');
      seen.add(message.id);
      exigence(['inscription', 'question'].includes(message.type), message.id + ' : type inconnu.');
      exigence(message.atelier === null || ['Reliure', 'Cartographie'].includes(message.atelier), message.id + ' : atelier inconnu.');
      exigence(message.places === null || (Number.isSafeInteger(message.places) && message.places > 0), message.id + ' : places doit être un entier positif ou null.');
      exigence(message.type !== 'question' || message.places === null, message.id + ' : une question n’ajoute pas de places.');
      exigence(message.id !== 'M005' || message.type === 'question', 'M005 reste une question, sans inscription supplémentaire.');
      exigence(message.source === donnees.fichiers[message.id], message.id + ' : la référence ne correspond pas au message.');
      texte(message.extrait, message.id + ' : extrait', 4000);
      exigence(donnees.sources[message.source].includes(message.extrait), message.id + ' : extrait absent du fichier source. Conservez ses caractères et retours à la ligne.');
    }
    return copie(value);
  }
  function extractionJSON(raw) { return validerExtraction(lireJSON(raw, 'Extraction JSON')); }
  const trier = ids => IDS.filter(id => ids.includes(id));
  function preparerTexte(extraction, nouveaux) {
    if (!nouveaux.length) return 'Aucun nouveau message : M001, M002, M004 et M005 sont déjà connus.\nAucun nouveau point à exporter pour ce lot.';
    const rows = extraction.messages.filter(m => nouveaux.includes(m.id));
    const lignes = [
      '# Point interne — Les ateliers du quartier', '',
      'Origine de l’extraction : ' + extraction.origine + '.',
      'Proposition à relire avec les sources. Aucune inscription confirmée et aucun envoi.', '',
      '## Messages nouveaux', ''
    ];
    for (const m of rows) {
      lignes.push('- ' + m.id + ' — ' + m.type + ' ; atelier : ' + (m.atelier ?? 'non précisé') +
        ' ; places : ' + (m.places ?? 'non précisé') + '.',
      '  Source : entrees/' + m.source,
      '  Extrait : ' + JSON.stringify(m.extrait));
    }
    lignes.push('', '## Suivi déjà connu', '',
      'M004 : demande de Samir déjà enregistrée sous D001 dans entrees/suivi-initial.csv ; aucune nouvelle inscription.', '',
      '## Décisions encore ouvertes', '',
      'Date à clarifier : le 10 octobre 2026 dans CR01, section « Date de la journée », et le 17 octobre 2026 dans CR02, section « Projet d’affiche ».',
      'Sources : entrees/reunions/01-preparation.md et entrees/reunions/02-communication.md.',
      'Horaire de Cartographie non renseigné : CR01, section « Ateliers », et CR02, section « Programme ».',
      'Atelier de Léo à demander : entrees/courriels/02-leo.txt (M002).', '',
      '## Alertes de l’extraction à vérifier', '', ...extraction.alertes.map(a => '- ' + a), '',
      '## Rapprochement des fichiers', '',
      'entrees/courriels/03-copie-nora.txt reproduit M001. La référence principale est 01-nora.txt ; les deux fichiers sont conservés.', '',
      'L’approbation et l’export concernent ce point interne. Les demandes restent à examiner ; aucune date, heure ou place n’est confirmée.', '');
    return lignes.join('\n');
  }
  function validerEtat(value) {
    objet(value, ['version', 'lot', 'connus', 'rapports', 'journal', 'brouillon'], 'État');
    exigence(value.version === 1 && value.lot === 'quartier-01', 'État : version ou lot non reconnu.');
    exigence(Array.isArray(value.connus) && value.connus.length <= 4 && value.connus.every(id => IDS.includes(id)) && new Set(value.connus).size === value.connus.length, 'État : identifiants connus invalides.');
    exigence(Array.isArray(value.rapports) && value.rapports.length <= 10, 'État : rapports invalides.');
    const connus = ['M004'];
    value.rapports.forEach((rapport, index) => {
      objet(rapport, ['numero', 'messages', 'point', 'extraction'], 'Rapport');
      exigence(rapport.numero === index + 1, 'État : numéro de rapport incohérent.');
      texte(rapport.point, 'Point archivé');
      validerExtraction(rapport.extraction);
      exigence(Array.isArray(rapport.messages), 'État : messages du rapport invalides.');
      const nouveaux = IDS.filter(id => !connus.includes(id));
      exigence(nouveaux.length > 0 && JSON.stringify(rapport.messages) === JSON.stringify(nouveaux), 'État : rapport rejoué ou identifiants de rapport incohérents.');
      connus.push(...nouveaux);
    });
    exigence(JSON.stringify(trier(value.connus)) === JSON.stringify(trier(connus)), 'État : identifiants connus sans rapport correspondant.');
    exigence(Array.isArray(value.journal) && value.journal.length <= 200, 'État : journal invalide.');
    let precedent = 0;
    for (const event of value.journal) {
      objet(event, ['numero', 'action', 'detail'], 'Événement');
      exigence(Number.isSafeInteger(event.numero) && event.numero > precedent && event.numero < Number.MAX_SAFE_INTEGER - 1000, 'État : ordre du journal invalide.');
      precedent = event.numero;
      exigence(ACTIONS.includes(event.action), 'État : action de journal inconnue.');
      texte(event.detail, 'Détail du journal', 4000);
    }
    objet(value.brouillon, ['extraction', 'point'], 'Brouillon');
    texte(value.brouillon.extraction, 'Extraction du brouillon', MAX_TEXTE, true);
    texte(value.brouillon.point, 'Point du brouillon', MAX_TEXTE, true);
    return copie(value);
  }
  class Pipeline {
    constructor() {
      this.etat = {version: 1, lot: 'quartier-01', connus: ['M004'], rapports: [], journal: [], brouillon: {extraction: '', point: ''}};
      this.preparation = null;
      this.accord = null;
      this.noter('initialisation', 'M004 est déjà connu par le suivi initial.');
    }
    noter(action, detail) {
      const journal = this.etat.journal;
      journal.push({numero: (journal.at(-1)?.numero ?? 0) + 1, action, detail});
      if (journal.length > 200) journal.shift();
    }
    changerExtraction(raw) {
      texte(raw, 'Extraction JSON', MAX_TEXTE, true);
      if (raw === this.etat.brouillon.extraction) return;
      this.etat.brouillon.extraction = raw;
      this.preparation = null;
      this.accord = null;
      this.noter('extraction_modifiee', 'Extraction modifiée : contrôle et approbation à refaire.');
    }
    changerPoint(point) {
      texte(point, 'Point proposé', MAX_TEXTE, true);
      if (point === this.etat.brouillon.point) return;
      this.etat.brouillon.point = point;
      this.accord = null;
      this.noter('point_modifie', 'Point modifié : approbation à refaire.');
    }
    controler() {
      this.preparation = null;
      this.accord = null;
      let extraction;
      try { extraction = extractionJSON(this.etat.brouillon.extraction); }
      catch (error) { this.noter('controle_refuse', error.message); throw error; }
      const nouveaux = IDS.filter(id => !this.etat.connus.includes(id));
      this.etat.brouillon.point = preparerTexte(extraction, nouveaux);
      this.preparation = {extraction, raw: this.etat.brouillon.extraction, nouveaux};
      this.noter(nouveaux.length ? 'point_prepare' : 'rejeu_sans_nouveaute', nouveaux.length ? 'À relire : ' + nouveaux.join(', ') + '. Aucun identifiant ajouté au suivi.' : 'Lot déjà pris en compte ; aucun nouveau rapport.');
      return {nouveaux: [...nouveaux], point: this.etat.brouillon.point};
    }
    peutApprouver() { return !!this.preparation && this.preparation.nouveaux.length > 0 && this.preparation.raw === this.etat.brouillon.extraction && this.etat.brouillon.point.trim().length > 0; }
    approuver(lectureHumaine) {
      exigence(lectureHumaine === true, 'Relisez les sources et confirmez le contrôle humain.');
      exigence(this.peutApprouver(), 'Contrôlez une extraction contenant de nouveaux messages avant d’approuver.');
      this.accord = {point: this.etat.brouillon.point, raw: this.etat.brouillon.extraction};
      this.noter('approbation', 'Accord sur cette version exacte du point interne, après relecture humaine.');
    }
    estApprouve() { return !!this.accord && this.peutApprouver() && this.accord.point === this.etat.brouillon.point && this.accord.raw === this.etat.brouillon.extraction; }
    pointApprouve() {
      exigence(this.estApprouve(), 'Cette version du point n’est pas approuvée.');
      return this.accord.point;
    }
    marquerExport() {
      const point = this.pointApprouve();
      const messages = [...this.preparation.nouveaux];
      this.etat.rapports.push({numero: this.etat.rapports.length + 1, messages, point, extraction: copie(this.preparation.extraction)});
      this.etat.connus = trier([...this.etat.connus, ...messages]);
      this.noter('point_exporte', messages.join(', ') + ' pris en compte dans un point interne téléchargé. Aucune inscription confirmée.');
      this.preparation = null;
      this.accord = null;
      return point;
    }
    exporterEtat() {
      this.noter('etat_exporte', 'Sauvegarde locale demandée ; aucune nouvelle demande traitée.');
      return JSON.stringify(this.etat, null, 2);
    }
    reprendre(raw) {
      const candidat = validerEtat(lireJSON(raw, 'État'));
      this.etat = candidat;
      this.preparation = null;
      this.accord = null;
      this.noter('reprise', 'État repris ; tout brouillon doit être contrôlé et approuvé à nouveau.');
    }
  }
  const api = {Pipeline, validerExtraction, extractionJSON, validerEtat, preparerTexte};
  if (typeof module === 'object' && module.exports) module.exports = api;
  else root.MoteurAtelier = api;
})(typeof globalThis !== 'undefined' ? globalThis : this);

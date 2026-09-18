(function () {
  'use strict';
  const pipeline = new MoteurAtelier.Pipeline();
  const champ = id => document.getElementById(id);
  const extraction = champ('extraction');
  const point = champ('point');
  const lecture = champ('lecture');
  function statut(message, erreur = false) {
    champ('statut').textContent = message;
    champ('statut').classList.toggle('erreur', erreur);
  }
  function afficher() {
    champ('connus').textContent = 'Messages déjà connus : ' + pipeline.etat.connus.join(', ') + ' · Points exportés : ' + pipeline.etat.rapports.length;
    champ('approuver').disabled = !pipeline.peutApprouver() || !lecture.checked;
    champ('exporter-point').disabled = !pipeline.estApprouve() || !lecture.checked;
    const journal = champ('journal');
    journal.replaceChildren();
    for (const event of pipeline.etat.journal) {
      const li = document.createElement('li');
      li.value = event.numero;
      li.textContent = event.action + ' — ' + event.detail;
      journal.append(li);
    }
  }
  function proteger(action) {
    try { action(); } catch (error) { statut(error.message, true); }
    afficher();
  }
  function synchroniser() {
    pipeline.changerExtraction(extraction.value);
    pipeline.changerPoint(point.value);
  }
  function telecharger(blob, nom) {
    const url = URL.createObjectURL(blob);
    const lien = document.createElement('a');
    lien.href = url;
    lien.download = nom;
    document.body.append(lien);
    try { lien.click(); } finally { lien.remove(); setTimeout(() => URL.revokeObjectURL(url), 1000); }
  }
  extraction.addEventListener('input', () => proteger(() => {
    pipeline.changerExtraction(extraction.value);
    lecture.checked = false;
    statut('Extraction modifiée : contrôlez le lot, puis relisez et approuvez le nouveau point.');
  }));
  point.addEventListener('input', () => proteger(() => {
    pipeline.changerPoint(point.value);
    lecture.checked = false;
    statut('Point modifié : l’accord précédent ne vaut plus pour cette version.');
  }));
  lecture.addEventListener('change', afficher);
  champ('exemple').addEventListener('click', () => proteger(() => {
    extraction.value = JSON.stringify(DonneesAtelier.exemple, null, 2);
    pipeline.changerExtraction(extraction.value);
    lecture.checked = false;
    statut('Exemple fictif chargé. Cette extraction est préparée pour l’exercice ; aucun modèle n’a été appelé.');
  }));
  champ('controler').addEventListener('click', () => proteger(() => {
    synchroniser();
    lecture.checked = false;
    const resultat = pipeline.controler();
    point.value = resultat.point;
    statut(resultat.nouveaux.length ? 'Contrôles de structure et de provenance réussis. ' + resultat.nouveaux.length + ' messages nouveaux. Comparez les faits aux sources avant d’approuver.' : 'Lot déjà pris en compte : aucun nouveau message, aucun rapport supplémentaire à exporter.');
  }));
  champ('approuver').addEventListener('click', () => proteger(() => {
    synchroniser();
    pipeline.approuver(lecture.checked);
    statut('Cette version exacte du point interne est approuvée. Vous pouvez la télécharger. Aucune inscription n’est confirmée.');
  }));
  champ('exporter-point').addEventListener('click', () => proteger(() => {
    synchroniser();
    if (!lecture.checked) throw new Error('Confirmez votre relecture avant l’export.');
    const texte = pipeline.pointApprouve();
    const blob = new Blob([texte], {type: 'text/markdown;charset=utf-8'});
    telecharger(blob, 'point-quartier-01.md');
    pipeline.marquerExport();
    lecture.checked = false;
    statut('Téléchargement du point déclenché. M001, M002 et M005 sont pris en compte dans le rapport. Sauvegardez l’état pour les retrouver après fermeture. Aucune confirmation ni aucun envoi.');
  }));
  champ('exporter-etat').addEventListener('click', () => proteger(() => {
    synchroniser();
    telecharger(new Blob([pipeline.exporterEtat()], {type: 'application/json;charset=utf-8'}), 'etat-quartier-01.json');
    statut('Téléchargement de l’état déclenché. Exporter l’état ne marque aucun nouveau message comme traité.');
  }));
  champ('reprendre').addEventListener('change', async event => {
    const fichier = event.target.files[0];
    if (!fichier) return;
    try {
      if (fichier.size > 512000) throw new Error('État trop volumineux : 512 000 octets au maximum.');
      const raw = await fichier.text();
      pipeline.reprendre(raw);
      extraction.value = pipeline.etat.brouillon.extraction;
      point.value = pipeline.etat.brouillon.point;
      lecture.checked = false;
      statut('État repris après validation du format et de la cohérence des identifiants. Aucun accord conservé : contrôlez et relisez le brouillon avant un éventuel nouvel export.');
    } catch (error) { statut('Reprise refusée. ' + error.message, true); }
    event.target.value = '';
    afficher();
  });
  for (const [nom, contenu] of Object.entries(DonneesAtelier.sources)) {
    const details = document.createElement('details');
    const summary = document.createElement('summary');
    summary.textContent = nom === '../regles-equipe.md' ? 'regles-equipe.md' : 'entrees/' + nom;
    const pre = document.createElement('pre');
    pre.textContent = contenu;
    details.append(summary, pre);
    champ('sources').append(details);
  }
  afficher();
})();

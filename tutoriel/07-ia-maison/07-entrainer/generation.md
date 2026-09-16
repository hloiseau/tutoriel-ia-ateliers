Ouvrez `echantillon.txt`. L’échantillon fourni commence ainsi :

```text
le produit 27 revient en stock. son prix reste a 50 centimes. le service prepare une notification.
```
Code: Début réellement généré par notre modèle de base

La phrase ressemble à notre corpus, mais son sens pose déjà problème : elle prépare une notification après un simple retour en stock à prix inchangé. Puis la génération se détériore. Avec l’adaptateur, l’échantillon commence par `INFO produit=28 prix=44`, avant de partir lui aussi dans une suite incohérente.

Comment peut-on obtenir cela avec une perte en baisse ? Pendant l’évaluation, nous donnons au modèle les **vrais caractères précédents**. Pendant la génération, il reçoit progressivement ses **propres caractères produits**. Une erreur peut donc l’amener dans un contexte qu’il a peu rencontré, puis en provoquer d’autres.

Ajoutons la courte fenêtre, le petit réseau et les gabarits très répétitifs : nous sommes loin d’un assistant capable de comprendre notre service. La génération tire aussi les caractères selon les probabilités produites, avec une graine fixée pour nos échantillons.

Notre essai a réussi à entraîner un modèle et à changer ses prédictions. Il n’a pas produit un générateur fiable de règles ou de journaux. Conserver les deux observations nous évite de transformer une courbe encourageante en promesse que les sorties ne tiennent pas.

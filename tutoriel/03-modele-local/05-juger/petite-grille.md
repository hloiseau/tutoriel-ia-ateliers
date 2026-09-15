Complétez nos premiers essais avec deux autres demandes :

```bash
python client.py --fichier questions/format.json --sortie resultats/format.json
python client.py --fichier questions/francais.json --sortie resultats/francais.json
```

Le premier demande un objet JSON très précis. Le second reprend l’explication d’une variable, en français. Ouvrez les réponses et remplissez une table dans un fichier `evaluation.md` :

| Cas | Vérification | Votre observation |
| --- | --- | --- |
| Variable en anglais | Explication juste, deux phrases | À relever |
| Horaire présent | Mardi à 10 heures | À relever |
| Horaire absent | Pas d’horaire inventé pour dimanche | À relever |
| JSON demandé | Objet valide avec la seule clé `colors` et la liste attendue | À relever |
| Variable en français | Explication juste, français compréhensible, deux phrases | À relever |
Table: Cinq cas à examiner séparément

Pour vérifier le JSON, commencez par copier **le texte produit**, sans le corriger, dans `resultats/format-produit.json`, puis lancez :

```bash
python -m json.tool resultats/format-produit.json
```

Cette commande contrôle la syntaxe JSON. Elle ne vérifie pas que les clés et les valeurs répondent à la demande : ouvrez aussi le résultat et comparez-le à l’attendu.

Si vous retirez vous-même des balises Markdown ou réparez une virgule, notez cette intervention. Le résultat brut et le résultat obtenu après votre correction ne racontent pas la même histoire.

Dans l’exécution de référence sous Linux, le modèle a trouvé 10 heures pour le mardi et répondu « I do not know. » pour le dimanche. Le JSON demandé était valide et contenait la bonne liste. En revanche, l’explication anglaise tenait en une phrase au lieu des deux demandées. La réponse française était maladroite et a atteint la limite de 96 tokens avant de se terminer.

Ce mélange est intéressant : le même modèle respecte certaines consignes et en manque d’autres sur cinq demandes très courtes. Les réponses brutes sont dans `resultats-reference` dans l’archive. Comparez-les aux vôtres, mais conservez aussi vos propres observations si elles diffèrent.

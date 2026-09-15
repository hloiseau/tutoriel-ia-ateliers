Si vous voulez lui confier cette étape, repartez de la copie initiale et donnez-lui cette consigne :

```text
À partir de TICKET.md, propose une table de cas puis écris
les tests manquants dans test_ticket.py.
Ne modifie pas suivi.py.
Lance python -m unittest discover -v.
Rapporte les noms des tests en échec et la différence
entre la valeur attendue et la valeur obtenue.
```

La séparation entre les tests et la correction nous permet d’observer le comportement initial. Vérifiez le diff après son intervention : s’il a modifié `suivi.py` en même temps, l’expérience ne montre plus aussi clairement que les nouveaux tests attrapent l’ancien comportement.

Regardez également si ses tests appellent vraiment `notifier`. Un test qui compare deux constantes ou reproduit sa propre version de la condition peut passer sans contrôler notre fonction.

Enfin, les tests sont du code exécuté sur votre ordinateur. Dans cet atelier, ils utilisent seulement nos petites fonctions. Dans un dépôt inconnu, regardez leurs imports, leurs préparatifs et les commandes proposées avant de les lancer. Le mot « test » ne garantit pas à lui seul l’absence d’écriture ou d’appel réseau.

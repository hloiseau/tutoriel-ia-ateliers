Faisons une petite expérience, dans une **copie du projet corrigé**. Remplacez `<` par `<=` dans `notifier`, puis relancez la suite.

Le prix identique autorise maintenant une notification. Les tests qui attendent l’absence de notification à prix inchangé doivent échouer. S’ils ne le font pas, vérifiez que vous avez exécuté la bonne copie et que ces cas sont présents.

Rétablissez ensuite `<`, puis retirez temporairement la condition `nouveau.disponible and`. Le test de baisse sur un produit indisponible doit cette fois protester.

Ces modifications volontaires sont de petites **mutations** : nous introduisons une erreur précise pour voir si les tests la remarquent. Cela ne prouve pas qu’ils détecteront tous les bugs. Cela permet de vérifier que les cas importants ne sont pas seulement décoratifs.

Revenez enfin à la version corrigée et relancez la suite. Ne gardez pas une mutation dans votre copie de travail ; le but est de tester nos tests, pas de préparer discrètement le prochain ticket. 🙂

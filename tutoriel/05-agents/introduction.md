**TL;DR** — Nous allons suivre les appels d’outils, choisir ce qui entre dans le contexte et repérer les contrôles qui arrêtent une action. Nous préparerons aussi une reprise de session et un relevé de coût.

Dans la partie précédente, nous avons demandé à un agent d’ajouter des tests et de corriger une fonction. Nous avons relu son diff et exécuté les vérifications. Suivons maintenant le trajet complet : **que se passe-t-il entre notre demande et les fichiers modifiés ?**

Quand l’agent annonce qu’il va lancer les tests, qui les lance ? Quand il lit une consigne dans un fichier, doit-il la suivre ? Et s’il répète la même action sans avancer, combien de temps le laissons-nous continuer ?

Nous garderons l’assistant choisi pour la partie 4. À côté, un petit banc Python rejouera des demandes d’outils écrites à la main. Il nous donnera toujours les mêmes refus et les mêmes limites d’appels, ce qui est bien pratique pour examiner les contrôles sans attendre qu’un modèle veuille bien tomber dans notre piège. Ce banc n’appelle aucun modèle : ses traces montrent l’exécution du script, jamais le comportement d’un agent réel.

Gardez `mon-suivi` pour observer votre assistant. Le banc Python se télécharge dans un dossier séparé et fonctionne avec Python 3.12, sans nouveau service ni GPU. Les observations menées dans votre assistant dépendent, elles, de l’accès au modèle que vous utilisez déjà.

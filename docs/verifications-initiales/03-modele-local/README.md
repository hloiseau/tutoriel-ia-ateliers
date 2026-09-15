# Vérifications de l’atelier local

Exécution réelle sous Linux x86-64, Python 3.12.14, sans GPU. Le moteur utilisé est llama.cpp b10809 (version 0.4.0-dev, commit 5266f24da). Les poids ont été téléchargés par le script fourni et vérifiés par taille et SHA-256. Ils sont exclus de la livraison.

La commande et les variables nécessaires sont dans `commande.json`. Une variante CPU générique `libggml-cpu-x64.so` a été chargée explicitement, car la découverte automatique des moteurs ne fonctionnait pas dans cet environnement. Cela limite la portée des mesures de performances ; elles ne représentent pas le meilleur débit possible sur ce CPU.

Le serveur a répondu à `/health`. Les cinq fichiers de questions ont été exécutés réellement. Un échauffement puis trois appels ont été conservés sous `resultats-reference/cpu-verifie-2048` dans le ZIP d’annexes. Les résultats bruts restent disponibles, y compris les réponses qui respectent mal la demande. La mesure est une durée de requête complète, pas le débit du seul décodage. Aucun relevé de RAM, aucune mesure GPU ni consommation électrique ne sont revendiqués.

Le client a également passé six tests unitaires utilisant des réponses factices. Ils vérifient des comportements du code HTTP et ne constituent pas des appels à un modèle.

Le serveur et les clients de validation ont été lancés par un même processus de contrôle pour partager l’environnement réseau d’exécution. Les premiers essais lancés séparément ne partageaient pas leur accès à la boucle locale et ont reçu « connection refused » ; aucun résultat de modèle n’est déduit de ces essais.

L’installation a nécessité la déclaration du chemin des bibliothèques partagées sous Linux ; cette étape a été ajoutée au chapitre. Windows, macOS, le GPU et l’import ZdS restent à vérifier. Les illustrations ont été inspectées ; le HTML est contrôlé structurellement, sans rendu complet dans un navigateur réel.

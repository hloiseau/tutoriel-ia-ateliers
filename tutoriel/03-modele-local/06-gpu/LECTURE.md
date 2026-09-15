# 6. Essayer une carte graphique, si vous en avez une

[Sommaire de la partie](../README.md) · [Sources](.)

**TL;DR :** la carte graphique est une variante de l’expérience. Nous conserverons le modèle et les questions pour comparer ce qu’elle change réellement.

Si vous avez suivi le parcours sur CPU, vous avez déjà réalisé l’objectif principal. Les manipulations de ce chapitre demandent un moteur compilé pour votre GPU.

## Vérifier que le moteur voit la carte

Une carte NVIDIA présente dans l’ordinateur ne signifie pas que n’importe quel exécutable saura l’utiliser. Il faut un pilote compatible et un moteur construit avec le bon support. Les cartes d’autres fabricants et les puces Apple utilisent d’autres voies.

Sur une machine NVIDIA, commencez par :

```bash
nvidia-smi
```

Cette commande permet notamment de voir le pilote, la carte et sa mémoire. La version CUDA affichée par le pilote n’est pas une preuve qu’un kit de développement CUDA complet est installé.

Pour Windows, la version b10809 propose des archives CUDA et des archives `cudart` correspondantes. Gardez la même variante entre le moteur et ses bibliothèques. Pour une compilation NVIDIA, la [documentation de construction de llama.cpp](https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md) détaille les prérequis et l’option `GGML_CUDA`.[^p3-gpu]

Une fois votre moteur préparé, demandez-lui :

```bash
./moteur/llama-server --list-devices
```

Sous Windows, utilisez le chemin `.\moteur\llama-server.exe`. Si aucune carte utilisable n’apparaît, revenez au choix du binaire et aux messages du moteur. Changer le nom du modèle ne corrigera pas l’absence du support GPU.

[^p3-gpu]: ggml-org, [construction pour les différents moteurs de calcul](https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md), notamment CUDA, Metal et Vulkan.

## Rejouer notre série sur GPU

Arrêtez le serveur CPU. Dans sa commande, retirez `--device none` et remplacez `-ngl 0` par `-ngl all`. Conservez le fichier GGUF, la taille de contexte, le nombre de requêtes simultanées et les autres paramètres.

Regardez les messages de démarrage : le moteur doit indiquer le placement des couches sur le GPU. Une commande qui accepte une option n’est pas une preuve que tout le calcul a été placé où vous l’imaginez.

Relancez la série :

```bash
python mesurer.py --nom gpu-contexte2048
```

Notez la commande exacte et la mémoire vidéo observée. Comparez les durées aux essais CPU et relisez les réponses. Nous utilisons un modèle minuscule à l’échelle de certaines cartes : cette comparaison ne permettra pas de prévoir le gain pour tous les modèles ou toutes les tailles de requêtes.

Une RTX 3090 Ti avec 24 Go de mémoire vidéo permet d’envisager des expériences plus grandes que celle-ci, mais il faut toujours tenir compte du modèle, de sa précision, du contexte et de la mémoire déjà occupée. Il n’y a pas de correspondance universelle « tant de Go = tel modèle sans aucune contrainte ».

Avant de télécharger plus gros, choisissez ce que vous voulez améliorer dans votre grille d’évaluation. Sinon, il est assez facile de passer la soirée à remplir un disque sans avoir avancé sur son besoin.

## Conserver une expérience que l’on peut refaire

À la fin, votre dossier de résultats devrait permettre de retrouver :

- la machine et le système utilisés ;
- la version du moteur et sa commande ;
- le fichier de poids identifié dans `modele.json` ;
- les questions envoyées et les réponses brutes ;
- les mesures, leur définition et votre lecture des réponses.

Vous n’avez pas besoin de publier toutes les traces de votre ordinateur. Regardez leur contenu avant de les partager et gardez uniquement ce qui explique l’expérience.

Pour libérer de la place, vous pouvez arrêter le serveur puis supprimer le fichier de poids téléchargé. Gardez `modele.json` et vos résultats si vous souhaitez retrouver l’expérience plus tard. Relancer `telecharger.py` permettra de récupérer de nouveau le fichier tant qu’il reste disponible à cette adresse.

Nous avons maintenant un modèle que nous pouvons démarrer, interroger, mesurer et arrêter. La prochaine décision vous appartient : le garder pour une tâche précise, en essayer un autre, ou passer à autre chose.



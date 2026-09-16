# 6. Essayer une carte graphique, si vous en avez une

[Sommaire de la partie](../README.md) · [Sources](.)

**TL;DR :** la carte graphique est une variante de l’expérience. Nous conserverons le modèle et les questions pour comparer ce qu’elle change réellement.

Si vous avez suivi le parcours sur CPU, vous avez déjà réalisé l’objectif principal. Les manipulations de ce chapitre demandent un moteur compilé pour votre GPU.

## Vérifier que le moteur voit la carte

Pour utiliser une carte NVIDIA, il faut un pilote compatible et un moteur construit avec le support correspondant. Un exécutable prévu uniquement pour le CPU continuera d’ignorer la carte. Les autres fabricants et les puces Apple utilisent d’autres voies.

Sur une machine NVIDIA, commencez par :

```bash
nvidia-smi
```

Cette commande affiche notamment le pilote, la carte et sa mémoire. La version CUDA indiquée décrit la compatibilité du pilote ; vérifiez séparément la présence du kit de développement si vous voulez compiler le moteur.

Pour Windows, la version b10809 propose des archives CUDA et des archives `cudart` correspondantes. Gardez la même variante entre le moteur et ses bibliothèques. Pour une compilation NVIDIA, la [documentation de construction de llama.cpp](https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md) détaille les prérequis et l’option `GGML_CUDA`.[^p3-gpu]

Une fois votre moteur préparé, demandez-lui :

```bash
./moteur/llama-server --list-devices
```

Sous Windows, utilisez le chemin `.\moteur\llama-server.exe`. Si aucune carte utilisable n’apparaît, revenez au choix du binaire et aux messages du moteur. Changer le nom du modèle ne corrigera pas l’absence du support GPU.

[^p3-gpu]: ggml-org, [construction pour les différents moteurs de calcul](https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md), notamment CUDA, Metal et Vulkan.

## Rejouer notre série sur GPU

Arrêtez le serveur CPU. Dans sa commande, retirez `--device none` et remplacez `-ngl 0` par `-ngl all`. Conservez le fichier GGUF, la taille de contexte, le nombre de requêtes simultanées et les autres paramètres.

Regardez les messages de démarrage : le moteur doit indiquer le placement des couches sur le GPU. C’est ce journal, puis l’activité de la carte, qui nous dira si l’option a produit l’effet attendu.

Relancez la série :

```bash
python mesurer.py --nom gpu-contexte2048
```

Notez la commande exacte et la mémoire vidéo observée. Comparez les durées aux essais CPU et relisez les réponses. Avec ce modèle de 360 millions de paramètres et ces courtes requêtes, les résultats décriront cette expérience précise. Un modèle plus grand ou un contexte plus long changeraient le travail demandé à la carte.

Une RTX 3090 Ti avec 24 Go de mémoire vidéo permet d’envisager des expériences plus grandes que celle-ci. Avant de choisir la suivante, comptez le modèle, sa précision, le contexte et la mémoire déjà occupée : la capacité de la carte ne suffit pas à désigner un modèle universellement adapté.

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

Nous avons maintenant un modèle que nous pouvons démarrer, interroger, mesurer et arrêter. Gardez-le pour une tâche précise, comparez-en un autre sur les mêmes cas ou récupérez l’espace disque : les trois décisions sont parfaitement valables.



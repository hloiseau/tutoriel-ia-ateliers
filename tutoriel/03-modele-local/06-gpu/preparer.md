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

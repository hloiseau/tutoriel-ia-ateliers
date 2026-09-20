**TL;DR** — LoRA ajoute de petites matrices entraînables à une transformation existante. La base reste figée ; l’adaptateur actif modifie tout de même les sorties, y compris parfois celles que nous voulions préserver.

Notre adaptation complète pouvait toucher 15 055 paramètres. Repartons des mêmes poids et limitons la correction à deux matrices beaucoup plus petites.

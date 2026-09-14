Pour cet atelier, prenons **SmolLM2-360M-Instruct**, dans sa version GGUF Q8_0 publiée dans l’espace HuggingFaceTB. Il compte environ 360 millions de paramètres. Sa fiche le présente comme un modèle principalement anglophone et déclare une licence Apache 2.0.[^p3-smol]

Le fichier choisi pèse **386 404 992 octets**, soit environ **386 Mo** ou **369 Mio**. Voilà un téléchargement plus abordable que celui d’un très grand modèle. Ce choix sert à prendre en main l’inférence locale. Il ne signifie pas que ce petit modèle est un bon agent de développement ni qu’il sera à l’aise en français.

Ouvrez sa fiche et cherchez quatre informations : la langue, l’usage prévu, la licence et les limites indiquées. Si l’une manque, notez son absence. Un nom contenant « open » ne répond pas à ces questions.

Le suffixe **Instruct** indique une adaptation destinée à suivre des instructions. **GGUF** désigne le format de fichier utilisé ici. **Q8_0** désigne une forme de quantification : les nombres sont stockés avec une précision réduite selon ce format. Nous allons revenir sur ce que cela change en mémoire.

[^p3-smol]: HuggingFaceTB, [fiche de SmolLM2-360M-Instruct](https://huggingface.co/HuggingFaceTB/SmolLM2-360M-Instruct) et [version GGUF](https://huggingface.co/HuggingFaceTB/SmolLM2-360M-Instruct-GGUF). Taille et empreinte du fichier relevées le 14 septembre 2026 ; révision conservée dans `modele.json`.

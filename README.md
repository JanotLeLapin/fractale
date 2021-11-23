# Fractale

## Utilisation

```sh
pip install -r requirements.txt # Installer les modules nécessaires
python main.py # Lancer le script
```

Si vous êtes Monsieur Daumont/Kunian et que vous vous intéressez au code des algorithmes, ouvrez le fichier [algo.py](algo.py) et ignorez `main.py`. Ce dernier permet **uniquement** d'afficher l'écran de sélection des algorithmes.

## Dessin A

- On crée une boucle qui se répète 2 fois pour dessiner les deux segments perpendiculaires de même longueur
- On répète cette boucle 10 fois pour dessiner la figure

## Dessin B

- On crée une boucle qui dessine un cercle de rayon 80 puis se décale de 10 degrés.
- La boucle se répète 36 fois, ce qui correspond à l'angle d'un cercle divisé par le décalage entre chaque cercle ou 360 / 10.

## Dessin C

- On écrit les fonctions tleft et tright pour éviter d'avoir à appeller les fonctions right et left en spécifiant l'angle à chaque fois (c'est toujours le même)
- On crée une boucle qui dessine chaque créneau sur les côtés du dessin 10 fois, puis une boucle qui dessine les créneaux sur les angles du carré du dessin
- On exécute ces deux boucles 4 fois afin de former un carré de 4 côtés

## Motif

### II.1

- On écrit une fonction `motif(l)` qui dessine le motif demandé
- On sait que c'est un triangle équilatéral donc les angles sont de 60 degrés, c'est pourquoi on tourne à gauche de 60, puis à droite de 120 car 180 - 60 = 120.

### II.2

- On écrit une fonction `iteration1(l)`
- On crée une boucle qui s'exécute 2 fois, à l'intérieur on dessine deux fois le motif précédemment créé avec un angle de 60 degrés entre les deux puis on tourne de 120.
- On sait qu'à la fin la tortue doit avoir un angle de 0° et que le `right` à la fin de la boucle donne un angle de 120 degrés à la tortue. On sait également que 120° \* 3 = 360° ce qui correspond à un angle de 0°.
- Pour ce faire, on multiplie 120 par `j` et on fait en sorte qu'au premier tour `j` vaut 1 puis au 2ème `j` vaut 3. On initialise donc le `range` de la boucle avec 1 pour valeur de départ, 4 pour valeur finale et un pas de 2.
- La taille L1 d'un segment de la première itération équivaut au tiers de la taille de L d'un segment du premier motif.

### II.3

- On réutilise la logique qu'on a utilisé pour l'itération 1, on remplace chaque appel à la fonction `motif` par un appel à la fonction `iteration1`.
- La taille de L2 vaut 1/3/3 de L, donc 1/9 de L.

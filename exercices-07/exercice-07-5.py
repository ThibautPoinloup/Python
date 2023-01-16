# exo 7.5
# en utilisant une boucle for, on tire 100 fois un nombre entier `r` au hasard entre 1 et 10 inclus
# affichez `r` s'il est plus grand ou égal à 6

import random

# réponse 7.5
for r in range(0,101):
    r = random.randint(1,10)
    if r >= 6:
        print(r)

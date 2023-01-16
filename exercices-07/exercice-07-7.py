# exo 7.7
# en utilisant une boucle for, on tire 100 fois un nombre entier `r` au hasard entre 1 et 10 inclus
# affichez `r` s'il est compris entre 3 et 8 inclus

import random

# réponse 7.7
for r in range(0,101):
    r = random.randint(1,10)
    if r >= 3 and r <= 8:
        print(r)

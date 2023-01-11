# exo 6.18
# Avec le même tableau en 2 dimensions, affichez toutes les valeurs plus petites ou égales à 50 ainsi que leur cordoonnées (ligne et colonne)
# Vous pouvez réutiliser la variable `size` qui a permis de construire le tableau en 2 dimensions

import random

size = 5
matrix = []

for _ in range(0, size):
    row = [random.randint(40, 100) for _ in range(0, size)]
    matrix.append(row)

print(matrix)

# réponse 6.18

#[
#     [62, 67, 77, 50, 71], 
#     [83, 55, 91, 87, 53], 
#     [70, 83, 76, 48, 86], 
#     [43, 57, 91, 87, 43], 
#     [56, 55, 98, 55, 96]
# ]


for x in range(0, size):
    for y in range(0, size):
        for line in matrix:
         for line in matrix:
             for column in line:
              if column<= 50: 
                print(x,column) 


  











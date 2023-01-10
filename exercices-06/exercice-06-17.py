# exo 6.17
# Affichez la valeur qui se trouve à la colonne 4, ligne 3
# ATTENTION : il faut faire `- 1` pour obtenir les index correspondant

import random

size = 5
matrix = []

for _ in range(0, size):
    row = [random.randint(40, 100) for _ in range(0, size)]
    matrix.append(row)

print(matrix)

# réponse 6.17

for line in range(0, size):
    if line == 3:
        line = matrix[2]
        print(line)
        for column in range(0, size):
            if column == 4:
                column = line[3]
                print(column)

# La matrice Générée de base
# [
#     [64, 63, 79, 50, 85], 
#     [85, 52, 77, 84, 86], 
#     [45, 78, 78, 41, 46], 
#     [75, 58, 66, 62, 74], 
#     [83, 50, 89, 62, 55]
# ]

# La ligne 3
# [45, 78, 78, 41, 46]

# Colonne 4
# 41
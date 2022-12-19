# Affectation
import random
import math
foo = 123
# Les additions + et incrementation += / le ++ n'existe pas en python
foo = foo + 42
foo += 42

print(foo)
# Les soustractions - et décrementation -= / le -- n'existe pas en python
foo = foo - 42
foo -= 42

print(foo)
# Les multiplication *
print(3*8)

# Les divisions / 
100 / 2
print(100 / 3)
# Les divisions entiere //
print(90 // 4)

# Les modulo % 
print(4 % 3)

# la fonction random.randint() renvoie un nombre entier aléatoir compris entre 1 et 100 inclus
x = random.randint(1, 100)
print(x % 8)

# Les puissance **
print(2**4)

# racine de 2
result = 10 ** (1 / 2)
print(result)

# Opérateur de comparaisons

# Opérateur ==
result = 1 == 1
print(result)

# Opérateurs de grandeurs 
result = 123 < 42
print(result)
result = 123 <= 42
print(result)
result = 123 >= 42
print(result)
result = 123 >= 42
print(result)

# Opérateur d'innégalitée !=
result = 123 != 42
print(result)

# Encadrements
my_number = random.randint(0, 100)
print(my_number)
result = 0 <= my_number < 50
print(result)
result = 50 < my_number <= 100
print(result)

#Opérateur and (et)
result= True and False
print(result)
result= False and True
print(result)
result= True and True
print(result)
result= False and False
print(result)

result = bool(random.randint(0, 1)) and bool(random.randint(0, 1))
print(result)
# utilisation special des comparaison de grandeur
result = "A" < "a"
print(result)

# Opérateur or (ou)
result= True or False
print(result)
result= False or True
print(result)
result= True or True
print(result)
result= False or False
print(result)

#opérateur not (négation)
result = not True
print(result)
result = not False
print(result)

#Opérateur in

fruits =['abricot', 'baies', 'cerise']
result = 'ananas' in fruits

print(result)

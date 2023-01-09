# exo 6.10
# Calculez la moyenne des nombres de la liste et affichez le résultat

my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.10

somme = 0

for item in my_list:
    somme = somme + item
    print(somme)

moyenne = somme / len(my_list)
#Pour avoir 2 chiffres après la virgule on utilise : '%2f' % (maVariable)
print('%.2f' % (moyenne))
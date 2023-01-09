# exo 6.9
# Calculez la somme des nombres de la liste et affichez le résultat

my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.9

# result = my_list[0] + my_list[1] + my_list[2] + my_list[3] + my_list[4] + my_list[5] 

# print(result)

accumulateur  = 0

for items in my_list:
    accumulateur = accumulateur + items
    print(accumulateur)

print(accumulateur)    
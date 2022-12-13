# exo 6.3
# Ajoutez la chaîne de caractères 'toto' à la fin de la liste `my_list` (sans modfier le code d'initialisation) et affichez le résultat

my_list = ['foo', 'bar', 'baz', 'lorem', 'ipsum']

# réponse 6.3
print(my_list)
print(len(my_list))

my_list.insert(0, "bonjour")
print(len(my_list))
print(my_list)

print(my_list)

# Ou append

my_list.append("toto")
print(my_list)
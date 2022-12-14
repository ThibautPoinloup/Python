# exo 6.7
# Inversez la position des valeurs `bar` et `lorem` puis affichez le résultat

my_list = ['foo', 'bar', 'baz', 'lorem', 'ipsum']

# réponse 6.7

print(my_list)

lorem = my_list[3]
bar = my_list[1]

my_list.pop(3)
my_list.pop(1)

my_list.insert(1, lorem)
my_list.insert(3, bar)

print(my_list)
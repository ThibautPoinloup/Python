# Opérateur d'affection = permet d'injecter une valeur dans une variable !
my_number_one = 123
my_number_two = -100

print(type(my_number_one))
print(my_number_two)

# String, chaine de caractère, saut de ligne
my_text_one = "Ceci est une chaine de caractère"
my_text_two = 'Ceci est aussi une chaine de caractère'
my_text_3 = "Voici ma premiere ligne\n Voici ma deusieme \"ligne\" "

print(type(my_text_one))
print(my_text_two)
print(my_text_3)

# Nombres à virgules flottantes
my_number_3 = 3.14
my_number_4 = -2.71
my_number_5 = 0.0

print(type(my_number_3))
print(my_number_4)
print(my_number_5)

# Les valeurs Booléenne
my_boolean_1 = True
my_boolean_2 = False

print(type(my_boolean_1))
print(my_boolean_1)
print(my_boolean_2)

#la valeur Null/None/NoneType
my_none = None

print(type(my_none))
print(my_none)

#Permutation de variable
a = 123
b = 321

a, b = b, a 

print(a, b)

a = 12
b = 32

c = b
b = a
a = c

print(a, b)

foo = "123"
print(type(foo))

#Permet de changer le type (str ---> int)
foo = int(foo)
print(type(foo))

# Permet d'afficher un nombre entier
foo = 2.5
foo = int(foo)
print(foo)

foo = 2.71
a = int(foo)
b = foo - a

print(a)
print(b)

# exo 6.14
# Créez une deuxième liste nommée `new_list` ne contenant que les nombres entiers de la liste

my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.14

for i in range(len(my_list)):
   if my_list[i] == int(my_list[i]):
    new_list = my_list[i]
    print(new_list)
    

   



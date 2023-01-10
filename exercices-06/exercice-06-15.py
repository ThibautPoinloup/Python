# exo 6.15
# Trouvez la chaîne de caractères la plus longue dans une liste.
# Affichez son index, sa valeur et sa longueur.

my_list = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit']

# réponse 6.15

for i in my_list:
    #J'ai fais un print pour pouvoir comparer la valeur la plus grande (11)
    print(len(i))
    #Si la taille de mes items sont plus grandes que 10 
    if len(i) > 10:
        #tu me donne sa longueur
        longueur = len(i)
        #Sa valeur
        valeur = i
        # print(longueur, valeur)

        #J'ai refait une bloucle cette fois ci pour comparer la 'valeur' à son index 
        for index in range(len(my_list)):
            if my_list[index] == valeur:
                print(f"L'index du caractère le plus long est {index}, sa longueur est de {longueur}, le mot est '{valeur}'")
        

    
    
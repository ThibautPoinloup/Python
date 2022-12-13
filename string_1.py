#option 1
text1 = """texte
multi-ligne
abcd
foo
bar"""
print(text1)

#Option 2
text2 = "ceci\nest un\ntexte\nmulti-ligne"
print(text2)

#chaines de caractère Avec des nombres (interpolation) Meilleur solution !
number1 = 123
text3 = f"Nombre = {number1}"
print(text3)

text4 = f"""
le nombre est
{number1}
foo"""
print(text4)

#la contaténation
number2 = "le nombre de PI est " + str(3.14)
print(number2)

#tronquer un float
number3 = 1 / 3
text5 = f"1 / 3 ~= {number3:.4f}"
print(text5)

#L'ecriture de documentation pour une fonction
def hello(name: str) -> None:
    """Cette fonction dit bonjour à quelqu'un

    name str indique le nom de la personne à salué
    return None
    """
    print(f"salut {name}")

#definition d'une fonction utilisateur
hello("toto")

#Longueur de la string
text6 = "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quod nulla rerum dolor culpa eius porro reprehenderit tempore iure quia eaque, voluptatem nihil aliquid expedita esse numquam nisi. Distinctio ut temporibus dolorem!"
number4 = len(text6)
print(number4)

# trouver la position de la string dans une autre string 
number4 = text6.find("dolor") 
print(number4)

number4 = text6.find("dolor", number4 +1) 
print(number4)

# compte le nombre d'occurence d'une string (str) dans une autre string 
number5 = text6.count("elit")
print(number5)

# Remplacer du texte ou un mot dans un string (Attention la variable reste inchanger)
print(text6.replace('Lorem', 'foo'))

# remplacer definitivement du texte ou un mot dans un string 
text6 = text6.replace('dolor', 'Coucou')
print(text6)

# supprimer un texte ou un mot 
text6 = text6.replace('.', '')
print(text6)
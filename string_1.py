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


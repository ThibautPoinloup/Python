#Création d'une fonction appelé "addition"
from collections.abc import Callable
import random


def addition(a: float, b:float) -> float:
    """cette fonction sert à additionner deux nombres
    
    a float le premier nombre à additionner
    b float le deusième nombre à additionner
    return float le resultatde l'addition 
    """

    result = a + b
    
    return result
    print(result)

#Utilisation de la fonction "addition"
my_number_1 = 1
my_number_2 = 2
result = addition(my_number_1, my_number_2)
print(result)


def calculer(calcul1: Callable, calcul2: Callable, a:float, b:float, c:float) -> float:
    result = calcul1(a,b)
    result = calcul2(result ,c)

    return result

result = calculer(addition,addition,123,42,3.14)
print(result)

def randint_list(lower_value, higher_value):
    number = random.randint(lower_value, higher_value)


my_list = randint_list(0,100)
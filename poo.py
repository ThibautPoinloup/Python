#POO (Programation Orienté Objet)
class Voiture:
    #constructeur
    #en JS, on utilise "this" au lieu de "self"
    #le mot "self" désigne l'instance en cours d'utilisation
    def __init__(self):
        self.passagers = 0
        self.vitesse = 0
    def getPassagers(self):
        return self.passagers

    def setPassagers(self):
        if type(passagers) is int and passagers >= 0:
         self.passagers = passagers    



#v est une instance de la classe Voiture
#v est un objet de la classe Voiture
v1 = Voiture()
print(v1.passagers)
print(v1.vitesse)
v1.passagers = 3
v1.vitesse = 50
print(v1.passagers)
print(v1.vitesse)

v2 = Voiture()
print(v2.passagers)
print(v2.vitesse)
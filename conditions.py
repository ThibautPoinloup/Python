import random

if True:
    print("La condition est vraie")
    print("ce code est executé")

if False:
    print("La condition est fausse !")
    print("le code n'est pas executé")

condition_vente = True

if condition_vente:
    print("L'utilisateur a accepté les conditions")
else: 
    print("L'utilisateur n'at pas accepté les conditions")

if not condition_vente:
    print("L'utilisateur n'at pas accepté les conditions")


emails = random.randint(0, 3)

if emails == 1:
    print("vous avez un nouveau mail")
elif 1 > 0:
    print(f"vous avez {emails} nouveaux messages")
else:
    print("vous n'avez pas de nouveaux messages")    

windows_closed = True
electricity_off = True

if windows_closed and electricity_off:
    print("windows are closed !")
    print("electricity is closed !")
elif not windows_closed and electricity_off:
    print("windows are not closed")
    print("electricity is closed")
elif windows_closed and not electricity_off:
    print("windows are closed !")
    print("electricity is not closed")
else:
    print("windows are not closed")
    print("electricity is not closed")


windows_closed = bool(random.randint(0, 1))
electricity_off = bool(random.randint(0, 1))

windows_closed = print(f'{windows_closed = }')
electricity_off = print(f'{electricity_off = }')

# Coupure electrique et fermeture des fenetres

if windows_closed and electricity_off:
    print("windows are closed !")
    print("electricity is closed !")
elif not windows_closed and electricity_off:
    print("windows are not closed")
    print("electricity is closed")
elif windows_closed and not electricity_off:
    print("windows are closed !")
    print("electricity is not closed")
else:
    print("windows are not closed")
    print("electricity is not closed")

# Carte Bancaire

bank_card = True
cash = False

#Si j'ai la carte bancaire OU le cash
if bank_card or cash:
    print("on a un moyen de paiement")

# Savoir si j'ai une carte bancaire ET du cash
if bank_card and cash:
    print("on a un moyen de paiement")
elif bank_card:
    print("j'ai la carte")
elif cash:
    print("jai du cash")
else:
    print("je n'ai pas de moyen de paiement")



ticket = True
vip = False
registration = False

print(f'{ticket = }')
print(f'{vip = }')
print(f'{registration = }')

if (ticket or vip) and registration:
    print("access authorized !")
else:
    print("access No authorized !")



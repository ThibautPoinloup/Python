#Fonctions while

while False :
    print('cette boule ne sera pas affichée')

# while True :
#     print('Ce message sera affichée en boucle')

#incrémentation avec while
counter = 0
print(f"{counter = }")

while counter <= 10:
    print(f"{counter = }")
    counter += 3
 
#décrémentation avec while
counter = 10

while counter >= 0:
    print(f'{counter = }')
    counter -= 1

for counter in range(0,10):
    print(f"{counter = }")

fruits =['abricot', 'baies', 'cerise']

for i, fruits in enumerate(fruits):
    print(f'{i + 1}: {fruits}')
    
#incrémentation avec for
for counter in range(0, 10, 2):
    print(f"{counter = }")

#décrémentation avec for
for counter in range(10, 0, -1):
    print(f"{counter = }")

my_list = [2.71, 42, 123, 2, 3.14, 1.61, 3.14]

for item in my_list:
    if item == 3.14:
        print(item)     

#Liste a 2 dimentions
for i in range(0, 10):
    for j in range(0,10):
        print(i, j)


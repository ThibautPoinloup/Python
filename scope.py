#La portée des variables

foo = 123 #scope global

def bar():
    foo = 42 #scope local
    print(foo)
  
print(foo) #123, scope global
bar() #42, scope local de la fonction bar()
print(foo) #123, scope global

def baz():
    print('baz', foo) #scope global



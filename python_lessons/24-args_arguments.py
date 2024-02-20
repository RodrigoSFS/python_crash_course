# *args = parâmetro que irá acoplar todos os argumentos em um tuple, útil para um função que aceita vários argumentos

# args é um nome, pode ser qualquer nome
# tuples são imutáveis, se quiser mudar, deverá ser feito um casting para outra coleção/estrutura de dado
def func(*args):
    print(args)
    print(type(args))
    

func(10,20,30,40,50)

def add(*args):
    sum = 0
    for i in args:
        sum += i
    
    return sum

print(add(1,2,3,4,5))

print()

def add(*args):
    sum = 0
    args = list(args)
    args[0] = 0
    for i in args:
        sum += i
    
    return sum

print(add(1,2,3,4,5))
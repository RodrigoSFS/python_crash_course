'''
Exercício 3

'''

num= float(input("Digite um número(x): "))

def func(x):
    x = x**0.5 + (x/2) + x**x
    return x

print (func(num))
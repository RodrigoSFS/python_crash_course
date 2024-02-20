'''
Exercício 10

'''

x = input("Digite um numero: ")
y = input("Digite outro numero: ")
operador = input("Digite um operador aritimético: ")

def operacao(operador, x, y):
  if operador == "+":
    print(x + y)
  elif operador == "-":
    print(x - y)
  elif operador == "/":
    print(x / y)
  elif operador == "*":
    print(x * y)
  elif operador == "**":
    print(x ** y)
  elif operador == "%":
    print(x % y)
  else:
    print("Operador invalido")
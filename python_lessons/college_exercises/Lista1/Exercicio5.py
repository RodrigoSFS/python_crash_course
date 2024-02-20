'''
Exercício 5

'''

import math


a = float(input("Digite o lado A do triângulo: "))
b = float(input("Digite o lado B do triângulo: "))
c = float(input("Digite o lado C do triângulo: "))

if a < b + c and b < a + c and c < a + b:
  if a == b == c:
      print("Equilátero")
  elif a == b or a == c or b == c:
    print("Isósceles")
  else:
    print("Escaleno")
  
  s = (a + b + c) / 2
  result = math.sqrt (s*(s-a)*(s-b)*(s-c))
  print("Área do triângulo: ", result)
  
else:
  print("Não pode formar um triangulo")
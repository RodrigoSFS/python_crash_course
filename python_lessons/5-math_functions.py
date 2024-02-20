# no python, basta usar o import, e o nome do módulo
import math

pi = 3.14
negative_number = -5
num = 4


# para arredondar, basta usar o round.
print(round(pi))

# para arredondar para cima
print(math.ceil(pi))

# para arredondar para baixo
print(math.floor(pi))

# para dar o valor absoluto de um número, o quão longe o valor está de 0
print(abs(negative_number))

# potenciação, <numero> <expoente>
print(pow(num,2))

# radiciação, squareroot
print(math.sqrt(num))

# char o maior valor, entre alguns
x, y, z = 1, 2, 3
print(max(x,y,z))

# achar o mínimo
print(min(x,y,z))

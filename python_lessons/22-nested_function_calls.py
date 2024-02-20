# chamdas de funções dentro de chamada de funções, isso é possíel porque podemos usar o valor retornado por uma função, como argumento na chamada da próxima função

# num = input("escreva um numero: ")
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)

# exemplo extremo, mas é possível
print(round(abs(float(input("Escreva um número: ")))))
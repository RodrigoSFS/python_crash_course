# f é o nome da função, antes dos : são os parâmetros, tudo depois é oque vai ser executado

f = lambda x: x**2
print (f) # endereço de memória para a função
print(f(2)) # o dois será copiado para x, e o x será elevado ao quadrado

print()

sum = lambda x, y : x + y
print(sum)
print(sum(3, 4))
# multiple assinements

nome, idade, atrativo = "Rodinelson", 19, True

print(type(nome), type(idade), type(atrativo))

# multiple assinements with some variables that have the same value

numero1 = numero2 = numero3 = 3

print(numero1, numero2, numero3)

# String methods

name = "Teste"

# mostra a quantidade de chars tem uma String
print(len(name))

# Mostra em qual posição da String está um determinado char, como uma String é um array de Char, ele mostra em que posição do Array está, começando por zero(0)
print (name.find("T"))

print (name.find("e"))

# respectivamente descreve a String em caracteres maiúsculos e minúsculos
print(name.upper())
print(name.lower())

# descreve se a String descreve números

numeros_string = "1"
numeros_string2 = "123"
numeros_string3 = "teste123"

print(numeros_string.isdigit())
print(numeros_string2.isdigit())
print(numeros_string3.isdigit())

# devolve se a String contém apenas caracteres(se conter espaço, ele já desconsidera)
print(name.isalpha())

# conta quantas vezes certo caracter aparece em uma String
print(name.count("e"))
print(len(name))

# subistitui o caracter de uma determinada posição, por um caracter específico
print (name.replace("e", "a"))

# coisa maniera do python, eu posso simplesmente escrever a quantidade de vezes que uma string seja mostrada na tela, simplesmente por multiplicar a String por um valor específico.
print(name*3)


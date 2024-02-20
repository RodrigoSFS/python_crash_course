# slicing, create a substring by extracting elements from another string
# podemos usar o operador indexing [] ou a função slice(), para criar um objeto slice
#               [start:stop:step] <start é em que slot do array começa>
#                                 <stop é em que slot do array termina>
#                                 <step é o rítmo>

name = "Rodrigo de Souza Fernandes Silva"
first_name = name[0:7]
#first_name = name[:7]
#last_name = name[8:]
last_name = name[8:32]
funny_name = name[::3]

print(first_name)
print(last_name)
print(funny_name)

#como reverter a string usando o slicing

reversed_name = name[::-1]

print(reversed_name)

# agora usando a função slice()

website1 = "http://google.com"
website2 = "http://Wikipedia.com"

#criar o objeto slice, com o parênteses chamamos o contrutor e colocamos os argumentos
#todos os arrays tem os index positivos e negativos, os negativos começando da parte oposta do array dos positivos
slice = slice(7, -4)

print(website1[slice])
print(website2[slice])


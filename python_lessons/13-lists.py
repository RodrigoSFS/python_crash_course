# lists são usadas para guardar multiplos valores em uma única variável
# se declara como as []
# a lista é completamente dinâmica, pode ter mais de um tipo de dado na mesma lista, e pode ser substituida e tudo mais

food = ["pizza", "hamburguer", "Pão"]

print(food[1])

print(type(food[1]))
print(type(food[2]))

for i in food:
    print(i)

# adiciona no final
food.append("sorvete")

# remove um dado da lista
food.remove("hamburguer")

# remove o último elemento da lista
food.pop()

# insere um valor em um dado index
food.insert(0, "bolo")

# ordenará a lista em ordem alfabética
food.sort()

for i in food:
    print(i)

# remove todos os elementos da lista
food.clear()
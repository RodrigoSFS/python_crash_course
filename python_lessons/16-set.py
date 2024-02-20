# Coleção que é desordenada, não há index, e não há valores duplicados.

# para usar a estrutura de dado set, basta usar {} ao invés de () e []

# o set é mais rápido do que uma lista, até porque, não há ordem na qual os valores ficam armazenados, eles podem aparecer em diferentes ordens, é útil para quando se quer saber se há o valor requerido dentro do set

set_list = {"Rodrigo", "Rodrigo2"}
objetos = {"garfo", "faca", "prato"}

# adiciona valor ao setList
set_list.add("Rodinelson")

# remove valor do set list
set_list.remove("Rodrigo2")
# o primeiro não tem efeito se o valor já estiver lá, e o último não tem efeito se o valor não estiver lá

# remove todos os itens do setList
#set_list.clear()

# adicionar uma setList em outra setList
set_list.update(objetos)
#objetos.update(set_list)

#for x in set_list:
#    print(x)

print()

#for x in objetos:
#    print(x)    

# unir múltiplas setLists em apenas um setList
tudo = set_list.union(objetos)

#for x in tudo:
#    print(x)

# mostra o que um tem, que o outro não tem
# print(objetos.difference(set_list))

# devolve o que as setLists tem em comum

print(set_list.intersection(objetos))
# tuples,  collections wich are ordered and unchangeable, used to group together related data

# para criar tuples, ao invés de [] basta usar ()

estudante = ("Rodrigo", 19, "homem")

# mostra quantas vezes certo valor aparece
print(estudante.count("Rodrigo"))

# mostra o index do valor, dentro da lista, no caso, 2
print(estudante.index("homem"))

for x in estudante:
    print (x)

if "Rodrigo" in estudante:
    print("Rodinelson esteve aqui")





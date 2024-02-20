# um laço de repetição dentro de outro

for lin in range(10):
    for col in range(10):
        if col < lin:
            print("* ", end="") # para não ir em um outro bloco direto
    print()
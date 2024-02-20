# a diferença de um while loop para um for loop, é que normalmente utilizamos o while para quando não tempos certeza da quantidade de repetições, para que seja repetido por quanto for possível.
# enquanto o for loop normalmente é utilizado para descrever a quantidade exata de fezes que será repetido

import time

# sempre começa pelo zero, isso pode ser mudado somando o range com um <range(10+1)> ou somando no print <print(i+1)>


#for i in range(10):
    #print(i+1)


# Pode-se também, passar no argumento, o número de início
#for i in range(50, 100+1):
    #print(i)

# O terceiro argumento poderá ser o ritmo

#for i in range(50, 100+1, 2):
    #print(i)

# dá para  fazer o for percorrer os caracteres de uma str 
#for i in "Rodrigo":
    #print(i)

for i in range(10, 0, -1):
    print(i)
    time.sleep(1) # quantos segundo o sistema vai dormir

print("feliz aniversário")
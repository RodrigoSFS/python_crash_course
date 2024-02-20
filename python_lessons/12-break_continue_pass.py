# loop control statements, change a loopsexecutio from it's normal sequence

# break = usado para terminar um loop definitivamente
# continue = pula para a próxima etapa do loop
# pass = faz nada, age como um placeholder

# o break termina o execução do while loop
#while True:
    #name = input("Entre o seu nome")
    #if name != "":
        #break


#phone_number = "123-456-7890"

#for i in phone_number:
#    if i == "-": # o continue passa para o prócimo valor da sequência
#        continue
#    print(i, end="")

# o pass é não fazer nada

for i in range(1, 21):
    if i == 13:
        pass
    else:
        print(i)


# uma porção de código que só é executada quando chamada
# nos impede de repetir código desnecessariamente

def soma(num1, num2):
    return num1 + num2

def hello(primeiro_nome, segundo_nome, idade):
    #pass (pass é tipo um placeholder)
    print("ola " + primeiro_nome + " " + segundo_nome + " " + str(idade))

#hello("Rodinelson")
meu_primiero_nome = "Rodinelson"
meu_segundo_nome = "da Silva"
hello(meu_primiero_nome, meu_segundo_nome, 19)

print(soma(1, 2))

#resultado = soma(1,2)
#print(resultado)




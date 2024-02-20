# exeption é um evento que é detectado durante a exeução que interormpe o fluxo do programa
# É interessante escrever as exeções expecíficas primeiro, e depois o except Exception, para capturar todas as exeções que não se pode pensar.

try:
    numerador = int(input("Escreva o numero para dividir"))
    denominador = int(input("Escreva por quanto o valor será dividido"))
    resultado = numerador / denominador
except ValueError as erro:
    print(erro)
    print("Digite apenas numeros")
except ZeroDivisionError as erro:
    print(erro)
    print("Não é possível dividir por zero")
except Exception as erro: # colocar o except Exception no final, para pegar qualquer exeção que não se pôde pensar até então
    print(erro)
    print("Algo deu errado")
else: # executado quando não houver erro
    print(resultado)
finally: # executado sempre, sempre no fim, independente se um erro foi capturado.
    print("Fim do programa")
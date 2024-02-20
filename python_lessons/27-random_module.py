import random

# faz que seja gerando um valor inteiro aletório entre 1 e 6
#x = random.randint(1, 6)
#print(x)

# gerar um valor aletório do tipo float
#y = random.random()
#print(y) 

# também temos o método shuffle para embaralhar a Lista
#cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
#random.shuffle(cards)
#print(cards)

# também podemos gerar escolhas aleatórios entre items em qualquer coleção
pedra_papel_tesoura = ['pedra', 'papel', 'tesoura']
#z = random.choice(pedra_papel_tesoura)
#print(z)

primeiro_jogador = random.choice(pedra_papel_tesoura)
segundo_jogador = random.choice(pedra_papel_tesoura)

if primeiro_jogador == segundo_jogador:
    print("Primeiro jogador escolheu: " + primeiro_jogador)
    print("Segundo jogador escolheu: " + segundo_jogador)
    print(" O resultado foi empate")
elif primeiro_jogador == 'pedra' and segundo_jogador == 'papel':
    print("Primeiro jogador escolheu: " + primeiro_jogador)
    print("Segundo jogador escolheu: " + segundo_jogador)
    print(" O segundo jogador venceu")
elif primeiro_jogador == 'pedra' and segundo_jogador == 'tesoura':
    print("Primeiro jogador escolheu: " + primeiro_jogador)
    print("Segundo jogador escolheu: " + segundo_jogador)
    print(" O primeiro jogador venceu")
elif primeiro_jogador == 'papel' and segundo_jogador == 'pedra':
    print("Primeiro jogador escolheu: " + primeiro_jogador)
    print("Segundo jogador escolheu: " + segundo_jogador)
    print(" O primeiro jogador venceu")
elif primeiro_jogador == 'papel' and segundo_jogador == 'tesoura':
    print("Primeiro jogador escolheu: " + primeiro_jogador)
    print("Segundo jogador escolheu: " + segundo_jogador)
    print(" O segundo jogador venceu")
elif primeiro_jogador == 'tesoura' and segundo_jogador == 'pedra':
    print("Primeiro jogador escolheu: " + primeiro_jogador)
    print("Segundo jogador escolheu: " + segundo_jogador)
    print(" O segundo jogador venceu")
elif primeiro_jogador == 'tesoura' and segundo_jogador == 'papel':
    print("Primeiro jogador escolheu: " + primeiro_jogador)
    print("Segundo jogador escolheu: " + segundo_jogador)
    print(" O primeiro jogador venceu")
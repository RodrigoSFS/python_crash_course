'''
Exercício 9

'''

sexo = input("Digite o sexo (M/F): ")
sexo = sexo.upper()
idade = int(input("Digite a idade: "))
tempo_contribuicao = int(input("Digite o tempo de contribuição (em anos): "))

aposentavel = False
    
if sexo == 'M':
    if (idade >= 65 and tempo_contribuicao >= 10) or (idade >= 63 and tempo_contribuicao >= 15):
        aposentavel = True
elif sexo == 'F':
    if (idade >= 63 and tempo_contribuicao >= 10) or (idade >= 61 and tempo_contribuicao >= 15):
        aposentavel = True
    
if aposentavel:
    print("Aposentável")
else:
    print("Não Aposentável")

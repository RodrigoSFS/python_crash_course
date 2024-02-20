# dictionary = Mutável, desordenada coleção com uma chave única:valores pares
# são rápidas porque usam hashing, permite que seja acessado valores com rapidez

# para criar os dictionaries, é similar com os sets

capitals = {'USA': 'Washington DC',
            'India': 'New Dehli',
            'China': 'Beijing',
            'Russia': 'Moscow'}

# Ao invés de usar o index, se usa a keu daquele valor, então, se quiser saber o valor 'Moscow' basta pedir para que seja exibido o valor que está guardado com a key 'Russia'
# print(capitals['Russia'])

# Caso seja expresso uma key que não existe no dictionary, o prgrama interrompe o seu fluxo, uma melhor maneira para se visualizar os itens com suas keys, é utilizando o método get da esturtura de dado dictionary
print(capitals.get('Germany'))

# devolve todas as keys
#print(capitals.keys())

# devolve todos os valores
#print(capitals.values())

# devolve todos
#print(capitals.items())

# uma outra forma de exibir todos os valores com um for loop

for key, value in capitals.items():
    print(key, value)

# como o dictionary é mutável, pode se adicionar par de keys e valores com o método update
capitals.update({'Germany':'Berlin'})

# também é possível atualizar valores associados em uma determinada key

capitals.update({'USA':'Las Vegas'})

# retira um par key e valor
capitals.pop('China')

# limpa o dictionary
capitals.clear()

print(capitals.items())
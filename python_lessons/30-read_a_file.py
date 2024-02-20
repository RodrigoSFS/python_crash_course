# seria necessário passar a URL, mas como o arquivo está no mesmo diretório que o projeto, não é necessário

path = 'C:\\Users\\rodri\\OneDrive\\Área de Trabalho\\Mídia\\Facul\\curso_de_python\\primeira_aula\\test.txt'

try:
  with open(path) as file:
    print (file.read())
except FileNotFoundError:
  print("Esse arquivo não foi encontrado")


print(file.closed)
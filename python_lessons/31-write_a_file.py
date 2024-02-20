# a função open tem os seguintes parâmetros:
# o nome do arquivo com o seu determinado tipo, e também o modo de abertura, r ou w, respectivamente, para leitura e escrita.

# é possível sobrescrever o arquivo, basta usar o modo de abertura w para sobrescrever, tendo o mesmo nome do arquivo.

# também é possível acrescentar texto ao arquivo, basta usar o modo de abertura "a", de "append" para acrescentar.
text = "Isso foi acrescentado!"
with open('teste_escrita.txt', 'a') as file:
    file.write(text)
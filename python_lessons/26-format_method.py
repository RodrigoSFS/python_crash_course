# str.format() = é um método opicional que nos dá mais controle para devolver o output

animal = "cow"
item = "moon"

# os {} são placeholders, e com o método format, podem ser inclusos variáveis, ou informações 
#print("The {} jumped over the {}".format("cow","moon"))

# é de forma sequencial, são argumetos posicionais, a ordem dos argumetos fazem diferença no resultado final
#print("The {} jumped over the {}".format(animal, item))

# outra forma de especificarmos a ordem seria com argumentos posicionais, para isso, no {} basta passar o index do argumento que se quer aparecer em uma determinada posição
#print("The {1} jumped over the {1}".format(animal, item))

# uma terceira forma, seria com um argumento keyword
#print("The {animal} jumped over the {item}".format(animal='cow', item='moon'))

#print("The {animal} jumped over the {animal}".format(animal='cow', item='moon'))

#text = "The {} jumped over the {}"

#print(text.format(animal, item))

name = "Rodrigo"

# há uma maneira de colocar algum preenchimento, em ambos os lados
#print("Hello, meu nome é {}".format(name))
#print("Hello, meu nome é {:10}. Que bom te conhecer".format(name))

# agora para o outro lado
#print("Hello, meu nome é {:>10}. Que bom te conhecer".format(name))

# para centralizar
#print("Hello, meu nome é {:^10}. Que bom te conhecer".format(name))

# Como formatar números

#number = 3.14159
number = 1000

# para apenas motras os primeiros 4 dígitos, primeiros 2 dígitos depois do decimal
# f significa flooting point numbers
#print("O número de pi é {:.2f}".format(number))

# automaticamente colocará uma vírgula na posição do mil
#print("O número é {:,}".format(number))

# Mostra o número em binário
print("O número é {:b}".format(number))

# Mostrar o número em octagonal
print("O número é {:o}".format(number))

# Mostrar o número em hexadecimal, x minúsculo para mostrar em minúsculo, e maiúsculo para maiúsculo
print("O número é {:x}".format(number))
print("O número é {:X}".format(number))

# Mostrar o número em notação científica, e ou E para maiúculo e minúsculo
print("O número é {:E}".format(number))
print("O número é {:e}".format(number))
# key arguments, os identificadores são predecessores dos argumentos, quando estes são passados na função, a ordem dos argumentos não importa, diferentemente dos argumentos posicionais, na qual a ordem depende de como ela foi passado função

# positional arguments
def ola(primeiro, segundo, terceiro):
    print("ola " + primeiro + " " + segundo + " " + terceiro)

#ola("Rodrigo", "de", "Souza")
ola("Rodrigo", "Souza", "de")

# key arguments
ola(terceiro="Souza",segundo="de",primeiro="Rodrigo")


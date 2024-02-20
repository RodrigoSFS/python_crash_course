import os

# we need 2 arguments, a src, and a destination
# since the file is on the same directory, we can just type the file name, otherwise, we have to type the path
# you can rename it aswell, for that, you have to type the name in the path
# the scape sequence to type a slash on the String, is by using the double backslashes. like this: "C:\\Users\\rodri\\OneDrive\\Área de Trabalho"

# that can be used to move a destination as well
source = "teste_escrita.txt"
destination = "C:\\Users\\rodri\\OneDrive\\Área de Trabalho//teste_escrita.txt"

try:
  if os.path.exists(destination):
    print("There is already a file with that name")
  else:
    os.replace(source,destination)
    print(source+" was moved to "+destination)
except FileNotFoundError:
  print(source+" não foi encontrado")
# index são representados por pelas [] = dão acesso a uma sequência de elementos (str, list, tuples)

name = "rodrigo!"

#if(name[0].islower()):
#    name = name.capitalize()

first_name = name[:2].upper()
#last_name = name[2:].lower()
last_name = name[2:7].lower()
last_character = name[-1]

print(first_name)
print(last_name)
print(last_character)
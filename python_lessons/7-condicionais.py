# condicionais, executará apenas se a condição for verdadeira
# a identação é importante toda a parte identada abaixo do if, é o que acontecerá se a condicional for atendida

age = int(input("qual a sua idade"))

if age == 100:
    print("Você é velho, bastante")
elif age >= 18:
    print("você é maior de idade")
elif age < 0:
    print("Você não nasceu ainda")

else:
    print("Você é menor de idade")

print("teste")


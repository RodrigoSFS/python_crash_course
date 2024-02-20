# operadores lógicos (and, or, not)

temp = int(input("What is the temperatura outside? "))

# para o operador and, ambas as condições devem ser verdadeiras
# para o operador or, uma das condições devem ser verdadeiras
# para o operador not, pode envolver uma condição, para que caso ela for verdadeira, tonará-se falsa, e se for falsa, tornará-se verdadeira
if temp >= 0 and temp <= 30:
    print("the temperature is good today")
    print("go outside")
elif temp < 0 or temp > 30:
    print("the temperature is bad today")
    print("don't go outside")

if not(temp >= 0 and temp <= 30):
    print("the temperature is bad today")
    print("don't go outside")
elif not(temp < 0 or temp > 30):
    print("the temperature is good today")
    print("go outside")


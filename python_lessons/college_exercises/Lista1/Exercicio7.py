'''
Exercício 7

'''

unidade = input("Digite 'F' para Fahrenheit ou 'C' para Celsius: ")

unidade = unidade.upper()

if unidade == 'F':
  temp_fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
  temp_celsius = (temp_fahrenheit - 32) * 5 / 9
  print(f"A temperatura em Celsius é: {temp_celsius:.2f} °C")
elif unidade == 'C':
  temp_celsius = float(input("Digite a temperatura em Celsius: "))
  temp_fahrenheit = (temp_celsius * 9 / 5) + 32
  print(f"A temperatura em Fahrenheit é: {temp_fahrenheit:.2f} °F")
else:
  print("Opção inválida. Digite 'F' ou 'C'.")

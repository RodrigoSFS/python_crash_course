from Data import Data

try:
  primeira_data = Data(12,1,2023)
  segunda_data = Data(20,1,2022)
  print(primeira_data == segunda_data)
  terceira_data = primeira_data + segunda_data
  quarta_data = primeira_data - segunda_data
except ValueError as e:
  print(str(e) + " Data inválida" )
else :
  print(primeira_data)
  print(segunda_data)
  print(terceira_data)
  print(quarta_data)
  print("Data válida")


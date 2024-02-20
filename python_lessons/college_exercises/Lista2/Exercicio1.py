opcao = 0

while opcao != 5:
  print()
  print("- Menuzin do Maroto -:")
  print("1 - Pizza Marguerita")
  print("2 - Pizza de Calabresa")
  print("3 - Pizza de Pepperoni")
  print("4 - Pizza de Mussarela")
  print("5 - Sair")
  opcao = int(input())
  if opcao == 1:
    print("Pizza Marguerita")
  elif opcao == 2:
    print("Pizza de Calabresa")
  elif opcao == 3:
    print("Pizza de Pepperoni")
  elif opcao == 4:
    print("Pizza de Mussarela")
  elif opcao == 5:
    print("Saindo...")
    break
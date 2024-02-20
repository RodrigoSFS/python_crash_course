class Data():
  def __init__(self, dia, mes, ano):
    if (dia < 1 or dia > 31):
      raise ValueError("Dia inválido.")
    elif mes < 1 or mes > 12:
      raise ValueError("Mes inválido.")
    elif ano < 0:
      raise ValueError("Ano inválido.")
    
    self.dia = dia
    self.mes = mes
    self.ano = ano

  def __str__(self):
    return (f"{self.dia}/{self.mes}/{self.ano}") # dd/mm/aaaa

  def __add__(self, other):
    dia = self.dia + other.dia
    mes = self.mes + other.mes
    ano = self.ano + other.ano
    print(f"{dia}/{mes}/{ano}")

    if dia > 31:
      mes = mes + dia // 30
      dia = dia % 30
    if mes > 12:
      ano = ano + mes // 12
      mes = mes % 12

    return Data(dia, mes, ano)
  
  def __sub__(self, other):
    dia = self.dia - other.dia
    mes = self.mes - other.mes
    ano = self.ano - other.ano

    if dia < 1:
      mes -= 1
      dia += 30
    if mes < 1:
      ano -= 1
      mes += 12

    if ano < 0:
      raise ValueError("Resultado resultaria em um ano negativo.")

    return Data(dia, mes, ano)
  
  def __eq__(self, other):
        return (self.dia, self.mes, self.ano) == (other.dia, other.mes, other.ano)

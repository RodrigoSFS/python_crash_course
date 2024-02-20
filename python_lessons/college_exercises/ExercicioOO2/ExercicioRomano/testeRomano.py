from NumeroRomano import NumeroRomano

try:
  numero_decimal = NumeroRomano(19)
  numero_romano = NumeroRomano("xii")
  print()
  print(numero_decimal.para_romano())
  print(numero_romano.para_decimal())
  terceiro_objeto = NumeroRomano.de_romano("XII")
  print(terceiro_objeto.para_decimal())
except:
  pass

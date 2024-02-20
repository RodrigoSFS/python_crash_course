import os
# detecção de arquivos básico, programinha para verificar se um arquivo existe

path = 'C:\\Users\\rodri\\OneDrive\\Área de Trabalho\\Mídia\\Facul\\curso_de_python\\primeira_aula\\29-file_detection.py'

if os.path.exists(path):
  print("Arquivo existe")
  if os.path.isfile(path):
    print("Arquivo é um arquivo")
  elif os.path.isdir(path):
    print("Arquivo é um diretorio")
else:
  print("Arquivo não existe")
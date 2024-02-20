import os
import shutil
path = "test.txt"

# isso não remove pastas vazias
try:
    #os.remove(path)      # delete a file
    #os.rmdir(path)       # delete an empty directory
    #shutil.rmtree(path)  # delete a directory containing files
    shutil.rmtree(path) # isso é perigoso, já que remove o diretório e todos os arquivos contidos nele
except FileNotFoundError:
    print("Arquivo não encontrado")
except PermissionError:
    print("Permissão negada para deletar isso") # não é possível deletar pastas vazias
except OSError:
    print("Nao se pode deletar isso utilizando essa funcao") # não é possível deletar pastas contendo arquivos com essa função
else:
    print(path+ " foi deletado")
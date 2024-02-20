# copyfile()    = copies contents of a file
# copy()        = copyfile() + permission mode + destination can be a direcotry
# copy2()       = copy() + copies metadata (file's creation and modification times)

import shutil

# in that funcion, you have 2 arguments, a src, and a destination
# if the path is on the same directory of the python file, you can just type the file name, otherwise, you have to type the path
# the copy will appear on the project folder, witch is the folder where the python file is.
# you can copy to a different destination, for that, you have to type the path on the 'dest'.
# the arguments ar exacly the same for the other funcitons aswell, but witch of this funcions will copy in a differenet way, depending on your necessities your project.
shutil.copyfile('teste_escrita.txt', 'copy.txt') # 'src', 'dest'
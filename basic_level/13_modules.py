# modules

# un modulo es un archivo que contiene código python, para utilizarlo en otro archivo python debemos importarlo
# podemos importar un modulo entero o solo una parte de el
# para importar un modulo entero utilizamos la palabra reservada import seguida del nombre del modulo
# para importar solo una parte de un modulo utilizamos la palabra reservada from seguida del nombre del modulo, la palabra reservada import y el nombre de la parte del modulo que queremos importar

# import math
# from math import pi
#
# print(math.pi)

# Ahora por ejemplo voy a traer una funcion del fichero de funciones que he creado en el mismo directorio que este fichero
from 10_functions import suma

print(suma(5, 5))
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
# import  10_functions #no va a funcionar por su nombre, porque no es un nombre valido para una variable, pero si que va a funcionar si lo importamos como un modulo y luego llamamos a la funcion con el nombre del modulo y el nombre de la funcion

from my_module import suma # importamos la funcion suma del modulo my_module, antes no  

print(suma(5, 5))

# podemos importar un modulo con un alias, para ello utilizamos la palabra reservada as seguida del alias que queremos utilizar

import math as m

print(m.pi)

# podemos importar una funcion con un alias, para ello utilizamos la palabra reservada as seguida del alias que queremos utilizar

from my_module import suma as s

print(s(5, 5))

# podemos importar todas las funciones de un modulo utilizando el asterisco

from my_module import *

print(suma(5, 5))

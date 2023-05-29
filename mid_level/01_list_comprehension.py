# List comprehension

#  es una forma de crear listas de forma rapida y sencilla
#  se puede usar para crear listas, diccionarios y sets
#  se puede usar para filtrar listas
#  se puede usar para modificar listas
#  se puede usar para crear listas de listas
#  se puede usar para crear listas de tuplas
#  se puede usar para crear listas de diccionarios
#  se puede usar para crear diccionarios de listas
#  se puede usar para crear diccionarios de diccionarios
#  se puede usar para crear diccionarios de tuplas
#  se puede usar para crear diccionarios de sets
#  se puede usar para crear sets de listas
#  se puede usar para crear sets de diccionarios
#  se puede usar para crear sets de tuplas
#  se puede usar para crear sets de sets
#  se puede usar para crear tuplas de listas
#  se puede usar para crear tuplas de diccionarios
#  se puede usar para crear tuplas de tuplas
#  se puede usar para crear tuplas de sets

my_original_list = [0,1,2,3,4,5,6,7]

my_list = [i for i in my_original_list] # crea una lista con los elementos de my_original_list
print(my_list) # [1, 2, 3, 4, 5, 6, 7]

my_list = [i for i in range(7)] # crea una lista con los elementos de my_original_list
print(my_list) # [0,1, 2, 3, 4, 5, 6]

my_list = [i + 1 for i in range(7)] # crea una lista con los elementos de my_original_list y les suma 1 antes de agregarlos a la lista

my_list = [i * i for i in range(7)]





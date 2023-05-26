# diccionarios

my_dict = dict() # Diccionario vacio
my_other_dict = {} # Diccionario vacio
print(type(my_dict))
print(type(my_other_dict))


my_other_dict = {"nombre":"Juan", "apellido":"Lopez", "edad":32,1:"Python"} # Diccionario con valores
print(my_other_dict)

my_dict = {
    "nombre":"Juan", 
    "apellido":"Lopez", 
    "edad":32,
    "lenguajes":{"Python","Java","C#"}, 
    1: 1.77
    }

print(my_dict)
print(my_dict["nombre"]) # Devuelve el valor de la clave nombre

print(len(my_dict)) # Devuelve la cantidad de elementos del diccionario, en este caso 5

print(my_dict["nombre"]) # Devuelve el valor de la clave lenguajes

my_dict["nombre"] = "Pepe" # Modifica el valor de la clave nombre
print(my_dict["nombre"]) # Devuelve el valor de la clave nombre

my_dict["provincia"] = "Alicante" # Agrega una nueva clave con su valor al diccionario
print(my_dict) # Devuelve el diccionario con la nueva clave y su valor

my_dict.pop("provincia") # Elimina la clave y su valor del diccionario
print(my_dict) # Devuelve el diccionario sin la clave y su valor

del my_dict[1] # Elimina la clave y su valor del diccionario
print(my_dict) # Devuelve el diccionario sin la clave y su valor

# La diferencia entre pop y del es que pop devuelve el valor de la clave eliminada y del no devuelve nada

print("Pepe" in my_dict) # Devuelve True si la clave esta en el diccionario, False si no esta, comprueba la clave no el valor
print("nombre" in my_dict) # Devuelve True si la clave esta en el diccionario, False si no esta, comprueba la clave no el valor

print(my_dict.items()) # Devuelve una lista de tuplas con las claves y los valores del diccionario
print(my_dict.keys()) # Devuelve una lista con las claves del diccionario
print(my_dict.values()) # Devuelve una lista con los valores del diccionario

print(my_dict.fromkeys(("nombre","apellido"))) # Devuelve un diccionario con las claves y los valores del diccionario, 
# pero con los valores vacios, es decir se ha creado un diccionario nuevo con las claves del diccionario original pero sin valores
# fromkeys es útil para crear diccionarios nuevos a partir de otros diccionarios, 
# por ejemplo para crear un diccionario nuevo con las claves de otro diccionario pero con valores vacios
# este sería un ejemplo
my_dict = {"nombre":"Juan", "apellido":"Lopez", "edad":32,1:"Python"}
my_new_dict = my_dict.fromkeys(my_dict.keys())
print(my_new_dict)

# Observa lo que pasa cuando lo transformamos en lista
print(list(my_dict)) # Devuelve una lista con las claves del diccionario, en este caso devuelve una lista con los valores de las claves
print(list(my_dict.values())) # Devuelve una lista con los valores del diccionario, en este caso devuelve una lista con los valores de las claves


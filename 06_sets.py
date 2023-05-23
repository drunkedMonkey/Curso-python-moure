# Sets
my_set = set() # Set vacio
my_other_set = {} # Esto no es un set, es un diccionario vacio
my_other_set = {"Pepe","Ibanez", "32"} # Set con valores
print(my_set)
print(type(my_set))

# la  única forma de crear un set vacío es con la función set(), con los corchetes se crea un diccionario vacío, no hay ottra forma de crear un set vacío

print(len(my_other_set)) # Devuelve la cantidad de elementos del set

# print(my_other_set[0]) # Esto da error porque los sets no tienen indice

# Los sets son utiles para eliminar duplicados  y para hacer operaciones de conjuntos (union, interseccion, diferencia, etc) 

my_other_set.add("Mi empresa") # Agrega un elemento al set
print(my_other_set) # Devuelve el set con el nuevo elemento de forma desordenada ya que los sets no tienen orden

my_other_set.add("Mi empresa") # Agrega el mismo elemento al set, pero como ya existe no lo agrega
print(my_other_set) # En esa ocasion no agrega el elemento duplicado

print("Mi empresa" in my_other_set) # Devuelve True si el elemento esta en el set, False si no esta

my_other_set.remove("Mi empresa") # Elimina el elemento del set
print(my_other_set) # Devuelve el set sin el elemento eliminado

# my_other_set.clear() # Elimina todos los elementos del set
print(len(my_other_set)) # Devuelve 0 porque el set esta vacio

# del my_other_set # Elimina el set
# print(my_other_set) # Da error porque el set ya no existe

my_list = list(my_other_set) 
# Convierte el set en lista y ahora es posible acceder a los elementos por indice ya que es una estructura ordenada, esto es  arriesgado porque los sets no tienen orden 
# y no vamos a conocer el orden de los elementos en la lista 
 
print(my_list[0]) # Devuelve el primer elemento de la lista

my_set = {'Juan', 'Lopez', '32'}
my_new_set = my_other_set.union(my_set) # Devuelve un nuevo set con la union de los dos sets
print(my_new_set)

print(my_new_set.difference(my_set)) # Devuelve un nuevo set con la diferencia entre los dos sets






# Tuplas

my_tuple = tuple() # Tupla vacia
my_other_tuple = () # Tupla vacia
print(my_tuple)
print(my_other_tuple)

my_tuple = (35, 1.80, 'Pepe', 'Ibanez')
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count('Pepe')) # Cuenta cuantas veces aparece un elemento en la tupla
print(my_tuple.index('Pepe')) # Devuelve el indice de la primera aparicion del elemento

#La  diferencia entre tuplas y listas es que las tuplas son inmutables, no se pueden modificar
# my_tuple[0] = 15 # Esto da error

my_other_tuple = (15, 1.79, 'Manu', 'Diaz')

my_sum_tuple= my_tuple + my_other_tuple # Concatenacion de tuplas  (no modifica las tuplas originales) 
print(my_sum_tuple[3:4]) # Devuelve una tupla con los elementos de la posicion 3 y 4

my_tuple =list(my_tuple) # Convertimos la tupla en lista (Ahora sí se puede modificar)
print(my_tuple)


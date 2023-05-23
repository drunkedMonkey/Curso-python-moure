# Listas

my_list= list() #crea una lista vacia
my_other_list = [] #crea una lista vacia  también

print(len(my_list)) #devuelve la longitud de la lista

my_list = ['hola', 'mundo', 'python', 3, 5.6, True] #crea una lista con los valores que le pasas

print(len(my_list)) #devuelve la longitud de la lista
print(my_list) #devuelve el primer elemento de la lista

my_other_list =  [35,1.77,'Pepe']

print(type(my_other_list)) #devuelve el tipo de la lista

print(my_other_list[0]) #devuelve el primer elemento de la lista
print(my_other_list[1]) #devuelve el segundo elemento de la lista
print(my_other_list[-1]) #devuelve el ultimo elemento de la lista

print(my_other_list.count('Pepe')) #devuelve el numero de veces que aparece el valor "Pepe" en la lista



age, height, name = my_other_list #desempaqueta la lista en las variables
print(name)

print(my_list + my_other_list) #concatena las listas

my_other_list.append('Nombre Empresa SL') #añade un nuevo valor a la lista
print(my_other_list)

my_other_list.insert(1, 'Azul') #añade un nuevo valor a la lista en la posicion 1
print(my_other_list)

my_other_list[1] = 'Rojo'



my_list.pop() #elimina el ultimo valor de la lista
print(my_list)
print(my_list.pop()) #elimina el ultimo valor de la lista y lo devuelve
print(my_list.pop(2)) #elimina el valor de la posicion 2 de la lista y lo devuelve

del my_list[2] #elimina el valor de la posicion 2 de la lista
print(my_list)

my_other_list.remove('Rojo') #elimina el valor "Rojo" de la lista
print(my_other_list)

my_new_list = my_list.copy() #copia la lista
my_list.clear() #elimina todos los valores de la lista
print(my_new_list)
print(my_list)

my_new_list.reverse() #invierte la lista
print(my_new_list)
my_new_list.sort() #ordena la lista
print(my_new_list)










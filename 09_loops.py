# Loops

# While loop
my_condition = 0

while my_condition < 10: # while es un bucle que se ejecuta mientras la condición sea verdadera
    if my_condition == 5:
        print("my_condition is 5")
        break # break rompe el bucle
    print("my_condition is: ", my_condition)
    my_condition += 1
print("La ejecución continua fuera del bucle...")

# For loop 
# con él podemos iterar sobre una secuencia de elementos
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9] # una lista es una secuencia de elementos
for element in my_list: # element es una variable que toma el valor de cada elemento de la lista
    print(element)

# podemos iterar sobre un string
my_string = "Hola Python"
for letter in my_string:
    print(letter)

    







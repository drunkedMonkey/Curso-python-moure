# Functions

# las funciones son bloques de codigo que se pueden ejecutar varias veces
# para evitar repetir codigo

def my_funcion(): # definimos la funcion
    print("Hello World")

my_funcion() # llamamos a la funcion

def saludo(nombre): # definimos la funcion con un parametro
    print("Hola " + nombre)

saludo("Juan") # llamamos a la funcion con un argumento

def suma(num1, num2): # definimos la funcion con dos parametros
    suma = num1 + num2
    return suma # retornamos el valor de la suma

print(suma(5, 10)) # llamamos a la funcion con dos argumentos

valor_almacenado = suma(5, 10) # almacenamos el valor de la funcion en una variable
print(valor_almacenado) # imprimimos el valor almacenado


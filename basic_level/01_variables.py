# Creando variables
# Las variables se definen por  convenciones con minusculas o snake case
my_string_variable = "My string variable" # esto  es snake case
print(my_string_variable);

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable= str(my_int_variable) # la funcion str convierte su argumento a string
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

print(my_string_variable,my_int_variable,my_int_to_str_variable,my_bool_variable) # Print acepta varios  argumentos

# Algunas funciones del sistema

print(len(my_string_variable)) # la función len() indica la longitud

# Variables en una  sola línea
name, surname, alias, age = 'Pepe', 'Ibañez', 'drunkedMonkey', 32
print('Me llamo',name, surname, 'mi alias es', alias, 'y mi edad es', age,'años')

# Inputs
first_name = input('¿Como te llamas?') #Con input() podemos solicitar información al usuario  por el terminal y almacenarla en variables
age = input('¿Cuantos años tienes?')

print('Bienvenido', first_name)

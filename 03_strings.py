#Srings

my_string = 'hola'

print(len(my_string))

my_new_line_string="Hola\nmundo"
print(my_new_line_string)

my_new_tab_string="\tHola\tmundo"
print(my_new_tab_string)

my_new_scape_string="\\tHola \\nmundo" #Poniendo una barra delante de la secuencia de escape permite imprimirla
print(my_new_scape_string)

# Formateo
name, surname, age = 'Jose Jesus', 'Ibanez',32
print("Me llamo {} {} y mi edad es {} años".format(name, surname, age)) # con format sustituye  las llaves por lo que pasas como parametro, en el mismo orden
print("Me llamo %s %s y mi edad es %d años" %(name,  surname, age)) #  es parecido a format,  cuadno es un string se pone %s y cuando es un entero %d+
print(f"Me llamo {name} {surname} y mi edad es {age} años".format(name, surname, age)) # esto es inferencia de datos, añadimos una f delante del texto, aasi infiere el valor de las variables

# Desempaquetado de caracteres
language  = 'python'
a,b,c,d,e,f = language  #se asigna una letra a cada variable
print(a)
print(b)

# División

language_slice = language[1:3] #da las letras de  la 1 a la 3 sin incluir la 3, es decir yt
print(language_slice)

language_slice = language[1:] #da las letras de  la 1 al final
print(language_slice)

language_slice = language[-2] #da la letra 2  empezando por el final
print(language_slice)

# Reverse
reversed_language = language[::-1] # devuelve la cadena alreves
print(reversed_language)

# Funciones
print(language.capitalize()) #pone la primera letra en mayuscula
print(language.count('t')) #cuenta las veces que aparece la letra t
print(language.isnumeric()) #devuelve true si es un numero
print(language.lower()) #pone todo en minuscula
print(language.upper()) #pone todo en mayuscula
print(language.upper().isupper()) #pone todo en mayuscula y comprueba si es mayuscula
print(language.startswith('py')) #comprueba si empieza por py


# classes

# Una clase es un modelo que se utiliza para crear objetos que comparten un mismo comportamiento, estado e identidad.

# Imagina que queremos hacer un programa para gestionar los empleados de una empresa. Podríamos guardar los datos de cada empleado en una lista:

# empleado1 = ["Juan", 53, 1500, True]
# empleado2 = ["Ana", 43, 2000, False]

# Esto funciona bien, pero ¿qué pasa si tenemos que gestionar a 100 empleados? Sería muy difícil acordarse de qué índice tiene cada dato. Además, si queremos pasar los datos de un empleado a una función, 
# tendríamos que pasar todos los datos en el orden correcto, y sería muy fácil equivocarse.

# Para solucionar estos problemas, podemos crear una clase Empleado, que nos permitirá crear objetos de tipo empleado, con sus propios atributos (nombre, edad, sueldo, etc.) y métodos (caminar, comer, etc.).

# Para crear una clase, utilizamos la palabra reservada class, seguida del nombre de la clase y dos puntos:

# class Empleado:

# El nombre de la clase debe empezar por mayúscula, y se recomienda usar CamelCase (las palabras se escriben juntas, y cada palabra empieza por mayúscula).

# A continuación, podemos definir los atributos de la clase. Para ello, utilizamos el método especial __init__(), que se ejecuta automáticamente al crear un objeto.

class Empleado:
    def __init__(self, nombre, edad, sueldo, casado): # self es una referencia al objeto que se está creando
        self.nombre = nombre
        self.edad = edad
        self.sueldo = sueldo
        self.casado = casado

# Como puedes ver, el método __init__() recibe como primer parámetro self, que es una referencia al objeto que se está creando. A continuación, se definen los atributos del objeto, precedidos de self.

# Ahora podemos crear objetos de tipo Empleado, pasando los datos que necesita el método __init__():

empleado1 = Empleado("Juan", 53, 1500, True)
empleado2 = Empleado("Ana", 43, 2000, False)

# Para acceder a los atributos de un objeto, utilizamos la sintaxis objeto.atributo:

print(empleado1.nombre)
print(empleado1.edad)
print(empleado1.sueldo)
print(empleado1.casado)

# También podemos modificar los atributos de un objeto:

empleado1.sueldo = 2000
print(empleado1.sueldo)

# Para crear métodos, simplemente definimos funciones dentro de la clase. Por ejemplo, podemos crear un método para mostrar los datos de un empleado:

class Empleado:
    def __init__(self, nombre, edad, sueldo, casado):
        self.nombre = nombre
        self.edad = edad
        self.sueldo = sueldo
        self.casado = casado

    def mostrar_datos(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Sueldo:", self.sueldo)
        print("Casado:", self.casado)

# Ahora podemos llamar al método mostrar_datos() de un objeto:

empleado1 = Empleado("Juan", 53, 1500, True)
empleado1.mostrar_datos()

# También podemos crear métodos para modificar los atributos de un objeto:

class Empleado:

    def __init__(self, nombre, edad, sueldo, casado):
        self.nombre = nombre
        self.edad = edad
        self.sueldo = sueldo
        self.casado = casado

    def mostrar_datos(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Sueldo:", self.sueldo)
        print("Casado:", self.casado)

    def aumentar_sueldo(self, porcentaje):
        self.sueldo += self.sueldo * porcentaje / 100

# Ahora podemos llamar al método aumentar_sueldo() de un objeto:

empleado1 = Empleado("Juan", 53, 1500, True)
empleado1.aumentar_sueldo(10)
empleado1.mostrar_datos()

# También podemos crear métodos para eliminar un objeto. Para ello, utilizamos la palabra reservada del:

class Empleado:

    def __init__(self, nombre, edad, sueldo, casado):
        self.__nombre = nombre # Los atributos privados se definen con dos guiones bajos al principio, sirven para que no se puedan modificar desde fuera de la clase
        self.__edad = edad
        self.__sueldo = sueldo
        self.__casado = casado

    def mostrar_datos(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Sueldo:", self.sueldo)
        print("Casado:", self.casado)

    def setNombre(self, nombre):
        self.__nombre = nombre

    def aumentar_sueldo(self, porcentaje):
        self.sueldo += self.sueldo * porcentaje / 100

    def eliminar_empleado(self):
        del(self)



empleado1.nombre = "Alfonso" # como vemos al imprimirlo el valor no se ha modificado porque el atributo es privado
print(empleado1.nombre)

empleado1.setNombre("Alfonso") # para modificar el atributo privado tenemos que usar un método que lo modifique
print(empleado1.nombre)

# También podemos crear métodos para eliminar un objeto. Para ello, utilizamos la palabra reservada del:
empleado1.eliminar_empleado()
print(empleado1.nombre) # al imprimirlo nos da error porque el objeto ya no existe
# Para controlarlo podemos usar un try except o un hasattr
try:
    print(empleado1.nombre)
except:
    print("El objeto ya no existe")

if hasattr(empleado1, "nombre"): # hasattr nos devuelve un booleano si el objeto existe o no
    print(empleado1.nombre)
else:
    print("El objeto ya no existe")
# exception handling

# print(5 + "5") # Esto genera un error de tipo TypeError, porque no se pueden sumar un entero y una cadena de caracteres.

# Para evitar que el programa se detenga, podemos utilizar un bloque try-except:

try:
    print(5 + "5")
    print("Ha salido bien")
except:
    print("Se produjo un error")

# Si queremos que el programa se detenga cuando se produzca un error, podemos utilizar la palabra reservada raise:

try:
    print(5 + "5")
    print("Ha salido bien")
except:
    print("Se produjo un error")
    # raise

# También podemos utilizar la palabra reservada finally para ejecutar un bloque de código, independientemente de si se produjo un error o no:

try:
    print(5 + "5")
    print("Ha salido bien")
except:
    print("Se produjo un error")
finally:
    print("Esto se ejecuta siempre")

# Podemos utilizar la palabra reservada else para ejecutar un bloque de código si no se produjo un error:

try:
    print(5 + 5)
    print("Ha salido bien")
except TypeError: # podemos especificar el tipo de error que queremos controlar, si queremos controlar errores de forma  general ponemos solo except como en los ejemplos anteriores
    print("Se produjo un error")
except ValueError:
    print("Se produjo un error")
except Exception as error: # podemos guardar el error en una variable para utilizarlo en el bloque de código, con Exception controlamos todos los errores y con as error guardamos el error en la variable error
    print("Se produjo un error:", type(error).__name__)
else:
    print("Esto se ejecuta si no se produjo un error")


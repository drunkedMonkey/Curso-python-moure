# Conditionals
# encontramos tres tipos de condicionales: if, elif y else
# if: si se cumple la condición se ejecuta el bloque de código
# else: si no se cumple la condición se ejecuta el bloque de código
# else if: si no se cumple la condición se ejecuta el bloque de código

my_condition = False

if my_condition:
    print("my_condition is True")

print("La ejecución continua...")

my_condition = 5 * 2

if my_condition == 11:
    print("Se ejecua cuando el valor es 11")

if my_condition >= 10:
    print("Se ejecuta cuando el valor es 10 o mayor")
else:
    print("Se ejecuta cuando el valor es menor que 10")

if my_condition >= 10 and my_condition <= 20:
    print("Se ejecuta cuando el valor es 10 o mayor y 20 o menor")
    print('estoy dentro del if') # pertenece al if porque está identado
elif my_condition >= 10 or my_condition <= 20:
    print("Se ejecuta cuando el valor es menor que 10 o mayor que 20")
    print('estoy dentro del else') # pertenece al else porque está identado
else:
    print("Se ejecuta cuando el valor es menor que 10 y mayor que 20")


print('estoy fuera del else') # no pertenece al else porque no está identado







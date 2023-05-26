#  Dates

from datetime import datetime 

now = datetime.now() # devuelve la fecha y hora actual
print(now)
print(now.year) # devuelve el año actual
print(now.month) # devuelve el mes actual
print(now.day) # devuelve el día actual
print(now.hour) # devuelve la hora actual
print(now.minute) # devuelve los minutos actuales
print(now.second) # devuelve los segundos actuales
print(now.microsecond) # devuelve los microsegundos actuales

timestamp = datetime.timestamp(now) # devuelve la fecha y hora actual en formato timestamp
print(timestamp)

year_2023 = datetime(2023, 1, 1) # crea un objeto datetime con la fecha y hora especificadas

print(year_2023)

def print_date(date): # función que recibe un objeto datetime y muestra sus atributos
    print(date)
    print(date.year) # devuelve el año actual
    print(date.month) # devuelve el mes actual
    print(date.day) # devuelve el día actual
    print(date.hour) # devuelve la hora actual
    print(date.minute) # devuelve los minutos actuales
    print(date.second) # devuelve los segundos actuales
    print(date.microsecond) # devuelve los microsegundos actuales
    print(date.timestamp())

print_date(year_2023)

from datetime import time # importamos la clase time

current_time = time() # crea un objeto time con la hora
print(current_time.hour)
print(current_time.min)
print(current_time.second) 

from datetime import date # importamos la clase date

current_date = date.today() # crea un objeto date con la fecha actual
print(current_date.year)
print(current_date.month)
print(current_date.day)

# current_date.year = 2028 # no se puede modificar un objeto date
# print(current_date.year)

from datetime import timedelta # importamos la clase timedelta, timedelta sirve para crear objetos que representan una cantidad de tiempo determinada (horas, minutos, segundos, etc.)
start_timedelta = timedelta(200,100,100,weeks=10) # crea un objeto timedelta con los parámetros especificados
end_timedelta = timedelta(weeks=10) # crea un objeto timedelta con los parámetros especificados
print(start_timedelta-end_timedelta)
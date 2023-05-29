#  Challenges for the mid-level python course
#  Challenge extraidos de 

# Challenge 1
"""
    Escribe un programa que muestre por consola (con un print) los
    números de 1 a 100 (ambos incluidos y con un salto de línea entre
    cada impresión), sustituyendo los siguientes:
    - Múltiplos de 3 por la palabra "fizz".
    - Múltiplos de 5 por la palabra "buzz".
    - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""
def fizzbuzz(numb):
    if((numb % 3 == 0) and (numb % 5 == 0)):
        print ("fizzbuzz")
    elif(numb % 3 == 0):
        print ("fizz")
    elif((numb % 5 == 0)):
        print ("buzz")
    



list_numbers = list(range(1,100)) # crea una lista con los números del 1 al 100

for i in list_numbers:
    fizzbuzz(i)

# Challenge 2
"""
    Escribe una funcion quue reciba dos palabras y retorne true o false segun sean o no anagramas
    - un anagrama consiste en formar una parabra reordenando todas las letras de otra parabra inicial
    - no hace falta comprobar que ambas palabras existan
    - dos palabras exactamente iguales NO son anagramas
"""

def isAnagram(word_one, word_two):
    if(word_one == word_two):
       False

    return sorted(word_one.lower()) == sorted(word_two.lower())
    
    


print(isAnagram("roma", "amor")) # True   
print(isAnagram("rusia", "ser")) # False  

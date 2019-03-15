# inicio del archivo
# Autor: Erne
# Cuvalles
# club algoritmia

import math

# inicio del programa
# como obtener el factorial de cualquier numero

print("Introduce el numero:")

# asignamos a n la entrada del usuario 
n = int(input())

# la funcion "factorial" produce el factorial de un numero
# utilizando la biblioteca "math"

def factorial():
   f = math.factorial(n)
   print(f)

# ejecucion de la funcion "factorial"
factorial()


'''
Esta es otra forma de obtener el factorial
de cualquier numero
Para ello usamos una funcion recursiva
'''

print("Introduce un numero otra vez")
m = int(input())

def fact(m):
    if m == 0:
        return 1
    else:
        return m * fact(m-1)

print(fact(m))

# Fin del archivo


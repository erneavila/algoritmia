# inicio del archiv
# autor: Erne
# CUValles

import math
print("Introduce el valor para m:")
m = int(input())
print("Introduce el valor para n:")
n = int(input())


def factorial(m):
    f = math.factorial(m)
    return f

print("La variacioin es: ")
print(factorial(m)/factorial(m-n))





import math
import os
import random
import re
import sys

#
# Complete the 'andXorOr' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#
def andXorOr(a):
    pila = []
    mejor_resultado = 0

    for numero_actual in a:
        while pila:
            resultado_actual = numero_actual ^ pila[-1]
            if resultado_actual > mejor_resultado:
                mejor_resultado = resultado_actual

            if pila[-1] > numero_actual:
                pila.pop()
            else:
                break

        pila.append(numero_actual)

    return mejor_resultado


cantidad = int(input().strip())
arreglo = list(map(int, input().split()))

print(andXorOr(arreglo))
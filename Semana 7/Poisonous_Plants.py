
import math
import os
import random
import re
import sys

#
# Complete the 'poisonousPlants' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY p as parameter.
def poisonousPlants(niveles_pesticida):
    pila_plantas = []
    mayor_cantidad_dias = 0

    for pesticida_actual in niveles_pesticida:
        dias_para_morir = 0

        while pila_plantas and pesticida_actual <= pila_plantas[-1][0]:
            pesticida_izquierda, dias_izquierda = pila_plantas.pop()
            dias_para_morir = max(dias_para_morir, dias_izquierda)

        if not pila_plantas:
            dias_para_morir = 0
        else:
            dias_para_morir += 1

        mayor_cantidad_dias = max(mayor_cantidad_dias, dias_para_morir)
        pila_plantas.append((pesticida_actual, dias_para_morir))

    return mayor_cantidad_dias


cantidad_plantas = int(input().strip())
niveles_pesticida = list(map(int, input().split()))

print(poisonousPlants(niveles_pesticida))
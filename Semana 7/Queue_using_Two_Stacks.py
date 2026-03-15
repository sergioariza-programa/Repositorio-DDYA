pila_entrada = []
pila_salida = []

cantidad_consultas = int(input().strip())

for _ in range(cantidad_consultas):
    consulta = list(map(int, input().split()))

    if consulta[0] == 1:
        pila_entrada.append(consulta[1])

    elif consulta[0] == 2:
        if not pila_salida:
            while pila_entrada:
                pila_salida.append(pila_entrada.pop())
        pila_salida.pop()

    elif consulta[0] == 3:
        if not pila_salida:
            while pila_entrada:
                pila_salida.append(pila_entrada.pop())
        print(pila_salida[-1])
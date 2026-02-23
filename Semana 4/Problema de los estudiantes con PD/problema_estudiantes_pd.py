def leer_entrada():
    """Lee n, tamaño máximo de grupo opcional y los pares (nombre, nota).
    (str) -> (int, int, list, list)
    """
    datos = input().split()

    if len(datos) == 0:
        raise ValueError("Entrada vacía")

    cantidad_estudiantes = int(datos[0])

    if cantidad_estudiantes == 0:
        return 0, 0, [], []

    posicion_actual = 1
    tamaño_maximo_grupo = None

    if posicion_actual < len(datos):
        try:
            tamaño_maximo_grupo = int(datos[posicion_actual])
            posicion_actual += 1
        except ValueError:
            tamaño_maximo_grupo = None

    if tamaño_maximo_grupo is None:
        tamaño_maximo_grupo = cantidad_estudiantes

    if cantidad_estudiantes < 0:
        raise ValueError("La cantidad de estudiantes debe ser positiva o cero")

    if tamaño_maximo_grupo <= 0 or tamaño_maximo_grupo > cantidad_estudiantes:
        raise ValueError("El tamaño máximo de grupo no es válido")

    if len(datos) < posicion_actual + 2 * cantidad_estudiantes:
        raise ValueError("Faltan datos para leer los estudiantes")

    lista_nombres = []
    lista_notas = []

    for _ in range(cantidad_estudiantes):
        nombre_estudiante = datos[posicion_actual]
        nota_estudiante = float(datos[posicion_actual + 1])

        if nota_estudiante < 0.0 or nota_estudiante > 5.0:
            raise ValueError("Nota fuera de rango")

        lista_nombres.append(nombre_estudiante)
        lista_notas.append(nota_estudiante)

        posicion_actual += 2

    return cantidad_estudiantes, tamaño_maximo_grupo, lista_nombres, lista_notas


def calcular_valor_grupo(lista_notas, indice_inicio, indice_fin):
    """Calcula promedio y valor del grupo entre dos índices.
    (list, int, int) -> (float, float)
    """
    suma_notas = 0.0
    cantidad_elementos = indice_fin - indice_inicio + 1

    for indice in range(indice_inicio, indice_fin + 1):
        suma_notas += lista_notas[indice]

    promedio_grupo = suma_notas / cantidad_elementos
    valor_grupo = promedio_grupo * (cantidad_elementos * cantidad_elementos)

    return promedio_grupo, valor_grupo


def programacion_dinamica_agrupacion(lista_nombres, lista_notas, tamaño_maximo_grupo):
    """Encuentra la mejor agrupación consecutiva usando programación dinámica.
    (list, list, int) -> (float, list)
    """
    cantidad_estudiantes = len(lista_nombres)

    lista_mejores_valores = []
    lista_indices_previos = []

    for _ in range(cantidad_estudiantes + 1):
        lista_mejores_valores.append(-1000000000)
        lista_indices_previos.append(-1)

    lista_mejores_valores[0] = 0.0

    for indice_actual in range(1, cantidad_estudiantes + 1):

        mejor_valor_encontrado = -1000000000
        mejor_indice_anterior = -1

        if tamaño_maximo_grupo < indice_actual:
            tamaño_limite = tamaño_maximo_grupo
        else:
            tamaño_limite = indice_actual

        for tamaño_grupo in range(1, tamaño_limite + 1):

            indice_anterior = indice_actual - tamaño_grupo

            promedio_grupo, valor_grupo = calcular_valor_grupo(
                lista_notas,
                indice_anterior,
                indice_actual - 1
            )

            valor_total = lista_mejores_valores[indice_anterior] + valor_grupo

            if valor_total > mejor_valor_encontrado:
                mejor_valor_encontrado = valor_total
                mejor_indice_anterior = indice_anterior

        lista_mejores_valores[indice_actual] = mejor_valor_encontrado
        lista_indices_previos[indice_actual] = mejor_indice_anterior

    lista_grupos = []
    indice_recorrido = cantidad_estudiantes

    while indice_recorrido > 0:
        indice_anterior = lista_indices_previos[indice_recorrido]

        indice_inicio = indice_anterior
        indice_fin = indice_recorrido - 1

        promedio_grupo, valor_grupo = calcular_valor_grupo(
            lista_notas,
            indice_inicio,
            indice_fin
        )

        lista_grupos.append(
            (indice_inicio, indice_fin, promedio_grupo, valor_grupo)
        )

        indice_recorrido = indice_anterior

    lista_grupos.reverse()

    return lista_mejores_valores[cantidad_estudiantes], lista_grupos


def imprimir_resultados(valor_total_maximo, lista_grupos, lista_nombres):
    """Imprime el valor total y los grupos formados.
    (float, list, list) -> None
    """
    print("valor_maximo", round(valor_total_maximo, 4))

    numero_grupo = 1

    for grupo in lista_grupos:

        indice_inicio = grupo[0]
        indice_fin = grupo[1]
        promedio_grupo = grupo[2]
        valor_grupo = grupo[3]

        lista_integrantes = []

        for indice in range(indice_inicio, indice_fin + 1):
            lista_integrantes.append(lista_nombres[indice])

        print("grupo_" + str(numero_grupo), "tamaño=" + str(indice_fin - indice_inicio + 1), 
              "promedio=" + str(round(promedio_grupo, 4)),"valor=" + str(round(valor_grupo, 4)), "->",
            " ".join(lista_integrantes)
        )

        numero_grupo += 1


def main():
    """Ejecuta el programa completo.
    (None) -> None
    """
    try:
        cantidad_estudiantes, tamaño_maximo_grupo, lista_nombres, lista_notas = leer_entrada()

        if cantidad_estudiantes == 0:
            print("valor_maximo", 0.0)
            return

        valor_total_maximo, lista_grupos = programacion_dinamica_agrupacion(
            lista_nombres,
            lista_notas,
            tamaño_maximo_grupo
        )

        imprimir_resultados(valor_total_maximo, lista_grupos, lista_nombres)

    except ValueError as error:
        print("Error:", error)


main()
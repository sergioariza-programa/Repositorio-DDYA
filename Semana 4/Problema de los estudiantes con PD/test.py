import sys
import io

def leer_entrada_desde_stream(stream):
    """Lee UNA línea: n, k opcional, y luego (nombre, nota)*n.
    Retorna: (n, k, lista_nombres, lista_notas)
    """
    linea = stream.readline()
    if linea is None or linea == "":
        raise ValueError("Entrada vacía")

    datos = linea.split()

    if len(datos) == 0:
        raise ValueError("Entrada vacía")

    cantidad_estudiantes = int(datos[0])

    if cantidad_estudiantes == 0:
        return 0, 0, [], []

    if cantidad_estudiantes < 0:
        raise ValueError("La cantidad de estudiantes debe ser positiva o cero")

    posicion_actual = 1
    tamaño_maximo_grupo = None

    # k opcional
    if posicion_actual < len(datos):
        try:
            tamaño_maximo_grupo = int(datos[posicion_actual])
            posicion_actual += 1
        except ValueError:
            tamaño_maximo_grupo = None

    if tamaño_maximo_grupo is None:
        tamaño_maximo_grupo = cantidad_estudiantes

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
    """Promedio y valor: promedio * (tamaño^2)"""
    suma_notas = 0.0
    cantidad_elementos = indice_fin - indice_inicio + 1

    for indice in range(indice_inicio, indice_fin + 1):
        suma_notas += lista_notas[indice]

    promedio_grupo = suma_notas / cantidad_elementos
    valor_grupo = promedio_grupo * (cantidad_elementos * cantidad_elementos)

    return promedio_grupo, valor_grupo


def programacion_dinamica_agrupacion(lista_nombres, lista_notas, tamaño_maximo_grupo):
    """Maximiza el valor total agrupando consecutivos con tamaño <= k."""
    cantidad_estudiantes = len(lista_nombres)

    lista_mejores_valores = [-1e18] * (cantidad_estudiantes + 1)
    lista_indices_previos = [-1] * (cantidad_estudiantes + 1)

    lista_mejores_valores[0] = 0.0

    for indice_actual in range(1, cantidad_estudiantes + 1):
        mejor_valor_encontrado = -1e18
        mejor_indice_anterior = -1

        tamaño_limite = min(tamaño_maximo_grupo, indice_actual)

        for tamaño_grupo in range(1, tamaño_limite + 1):
            indice_anterior = indice_actual - tamaño_grupo

            _, valor_grupo = calcular_valor_grupo(
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

    # reconstrucción
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

        lista_grupos.append((indice_inicio, indice_fin, promedio_grupo, valor_grupo))
        indice_recorrido = indice_anterior

    lista_grupos.reverse()

    return lista_mejores_valores[cantidad_estudiantes], lista_grupos


def imprimir_resultados(valor_total_maximo, lista_grupos, lista_nombres):
    """Imprime valor máximo y cada grupo."""
    print("valor_maximo", round(valor_total_maximo, 4))

    numero_grupo = 1
    for (ini, fin, prom, val) in lista_grupos:
        integrantes = " ".join(lista_nombres[ini:fin + 1])
        print(
            "grupo_" + str(numero_grupo),
            "tamaño=" + str(fin - ini + 1),
            "promedio=" + str(round(prom, 4)),
            "valor=" + str(round(val, 4)),
            "->",
            integrantes
        )
        numero_grupo += 1



def ejecutar_programa_con_entrada_texto(texto_entrada):
    """Entrada (str) -> salida completa (str). No usa consola real."""
    entrada = io.StringIO(texto_entrada + "\n")
    salida = io.StringIO()

    stdout_original = sys.stdout
    sys.stdout = salida

    try:
        n, k, nombres, notas = leer_entrada_desde_stream(entrada)

        if n == 0:
            print("valor_maximo", 0.0)
            return salida.getvalue()

        valor_total, grupos = programacion_dinamica_agrupacion(nombres, notas, k)
        imprimir_resultados(valor_total, grupos, nombres)
        return salida.getvalue()

    except ValueError as error:
        print("Error:", error)
        return salida.getvalue()

    finally:
        sys.stdout = stdout_original

def run_file_tests(path_tests_in):
    """Lee tests.in con formato: <entrada> => <esperado>"""
    total = 0
    ok = 0
    fallos = []

    with open(path_tests_in, "r", encoding="utf-8") as f:
        for linea in f:
            raw = linea.rstrip("\n")

            # permitir comentarios o líneas vacías
            if not raw.strip():
                continue
            if raw.lstrip().startswith("#"):
                continue

            if "=>" not in raw:
                total += 1
                fallos.append((total, "FORMATO", raw, "Falta '=>'", ""))
                continue

            entrada, esperado = raw.split("=>", 1)
            entrada = entrada.strip()
            esperado = esperado.strip()

            total += 1
            salida = ejecutar_programa_con_entrada_texto(entrada)

            # Validación estable: SOLO la primera línea
            primera = salida.strip().splitlines()[0] if salida.strip() else ""

            if esperado.startswith("Error:"):
                if primera.startswith("Error:"):
                    ok += 1
                else:
                    fallos.append((total, "ERROR", entrada, esperado, primera))
            else:
                if primera == esperado:
                    ok += 1
                else:
                    fallos.append((total, "SALIDA", entrada, esperado, primera))

    print(f"Tests ejecutados: {total}")
    print(f"OK: {ok}")
    print(f"FALLOS: {total - ok}")

    if fallos:
        print("\n--- Detalle de fallos ---")
        for num, tipo, entrada, esp, obt in fallos:
            print(f"[{num}] {tipo}")
            print("  Entrada:  ", entrada)
            print("  Esperado: ", esp)
            print("  Obtenido: ", obt)




def main():
    try:
        n, k, nombres, notas = leer_entrada_desde_stream(sys.stdin)

        if n == 0:
            print("valor_maximo", 0.0)
            return

        valor_total, grupos = programacion_dinamica_agrupacion(nombres, notas, k)
        imprimir_resultados(valor_total, grupos, nombres)

    except ValueError as error:
        print("Error:", error)




if len(sys.argv) >= 3 and sys.argv[1].lower() == "filetest":
    run_file_tests(sys.argv[2])
else:
    main()
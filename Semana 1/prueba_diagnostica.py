# Prueba diagnostica
# Sergio Alejandro Ariza Ocampo

def main():

    datos = input().split()

    n = int(datos[0])

    del datos[0]

    estudiantes = []

    notas = []

    for i in range(n * 2):

        if i % 2 == 0:

            estudiantes.append(datos[i])

        else:

            notas.append(float(datos[i]))

    for i in range(n):

        if notas[i] >= 3:

            print(estudiantes[i], end = " ")

main()
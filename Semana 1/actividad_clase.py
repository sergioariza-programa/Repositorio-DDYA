# Programa que calcula si un numero es positivo,
# si un numero es primo y si un numero esta en la serie fibonacci

def valor(n):

    """Determina si un numero es positivo, negativo o cero
    (int) -> None"""

    if n > 0:

        print("el numero es positivo")

    elif n < 0:

        print("el numero es negativo")

    else:

        print("el numero es cero")

def es_primo(n):
    
    """Calcula si un numero es primo
    (int) -> None"""

    n = abs(n)
 
    i = n - 1

    while i > 1:

        if n % i == 0:

            print("EL numero no es primo")

            return 
        
        i -= 1
        
    print("el numero es primo")
        
def esta_en_fibonacci(n):

    """Calcula si n esta en la serie fibonacci
    (int) -> none"""

    serie = fibonacci(n)

    print(serie)

    for i in serie:

        if n == i:

            print("Esta en la serie fibonacci")

            return 
        
    print("no esta en la serie fibonacci")        

def fibonacci(n):

    """Serie de Fibonacci
    (n) -> list"""

    serie = []

    a, b = 0, 1

    while a <= n:

        serie.append(a)

        # Esto lo saque de internet (entiendo que hace)
        a, b = b, a + b

    return serie


def main():
    
    n = int(input())

    valor(n)

    es_primo(n)

    esta_en_fibonacci(n)

main()
def potencia(a, n):
    """Calcula el exponente de un numero a^n
    (int, int) -> float"""
    
    if n < 0:
    
        return 1 / potencia(a, -n)
    
    if n == 0:
    
        return 1
    
    if n == 1:
    
        return a

    mitad = potencia(a, n // 2)
    
    if n % 2 == 0:
    
        return mitad * mitad
    
    else:
    
        return mitad * mitad * a

def main():
    
    a = int(input())
    
    n = int(input())
    
    exponente = potencia(a, n)
    
    print(exponente)

main()
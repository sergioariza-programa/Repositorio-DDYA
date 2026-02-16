def encontrar_faltante(N):
    """Encuentra el numero faltante de un arreglo N"""
   
    l = 0
    
    r = len(N) - 1

    while l <= r:
        
        mitad = (l + r) // 2
     
        esperado = mitad + 1
        
        if N[mitad] == esperado:
      
            l = mitad + 1
     
        else:
     
            r = mitad - 1

    return l + 1

def main():
    
    N = list(map(int, input().split(",")))

    faltante = encontrar_faltante(N)
    
    print(faltante)
    
main()
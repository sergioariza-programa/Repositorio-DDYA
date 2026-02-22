def encontrar_mayor(N):
    
    l = 0
    
    r = len(N) - 1

    while l < r:
        
        mitad = (r+l) // 2
        
        if N[mitad] < N[mitad + 1]: 
            
            l = mitad  + 1
            
        else:
            
            r = mitad
            
    return N[l]
        
def main():

    N = list(map(int, input().split(",")))
 
    mayor_valor = encontrar_mayor(N)

    print(mayor_valor)

main()
def contar_bits_hasta(N):
    
    total = 0
    
    bit = 0

    while (1 << bit) <= N:
        
        bloque = 1 << (bit + 1)
        
        completos = N // bloque
        
        total += completos * (1 << bit)

        resto = N % bloque
        
        total += max(0, resto - (1 << bit) + 1)

        bit += 1

    return total

def encontrar_N(X):
    
    l = 1
    
    r = 10**18 

    while l < r:
        
        m = (l + r) // 2
        
        if contar_bits_hasta(m) >= X:
            
            r = m
            
        else:
            
            l = m + 1

    return l

def main():
    
    n = int(input().strip())
    
    resultado = encontrar_N(n)
    
    print(resultado)

main()
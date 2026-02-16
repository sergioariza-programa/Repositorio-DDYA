def merge_sort(A):
    
    A = list(A)
    
    if len(A) <= 1:
        
        return A
    
    mitad = len(A) // 2
    
    izquierda = merge_sort(A[:mitad])
    
    derecha = merge_sort(A[mitad:])
    
    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    
    nuevo = []
    
    i = 0
    
    j = 0
    
    while i < len(izquierda) and j < len(derecha):
        
        if izquierda[i] <= derecha[j]:
            
            nuevo.append(izquierda[i])
            
            i += 1
        
        else:
            
            nuevo.append(derecha[j])
            
            j += 1  
            
    nuevo.extend(izquierda[i:])
       
    nuevo.extend(derecha[j:])

    return nuevo
    
def main():
    
    texto = input().strip()
    
    texto_ordenado = merge_sort(texto)

    print(*texto_ordenado, sep = "")
    
main()    
            
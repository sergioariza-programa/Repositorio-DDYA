"""def encontrar_menor(N):
    Encuentra el menor valor de un arreglo cuyos
     valeres van en decremento y luego incremento
    (List) -> int
    print(N)
    valor_actual = N[0]

    for i in range(1,len(N)):

        if valor_actual < N[i]:

            return valor_actual

        valor_actual = N[i - 1]"""

def encontrar_menor(N):
    l = 0
    r = len(N) - 1


    while l < r:
        mitad = (r+l) // 2
        if N[mitad] > N[mitad + 1]: #es decreciente
            l = mitad  + 1
        else:
            r = mitad
    return N[l]
        
def main():

    N = list(map(int, input().split(",")))
    #2,1,2,3,4
    #8,5,4,3,4,10
    
    menor_valor = encontrar_menor(N)

    print("El menor valor es", menor_valor)

main()
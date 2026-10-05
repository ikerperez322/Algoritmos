import math

#MÁXIMO recibe un arreglo no necesarianmente ordenado para encontrar el elemento máximo
def maximo(arreglo):
    max = arreglo[0]

    for i in range(1, len(arreglo)):
        if arreglo[i] > max:
            max = arreglo[i]

    return max

#MÍNIMO recibe un arreglo no necesarianmente ordenado para encontrar el elemento mínimo
def minimo(arreglo):
    min = arreglo[0]

    for i in range(1, len(arreglo)):
        if arreglo[i] < min:
            min = arreglo[i]

    return min


#BUSQUEDABINARIA recibe un arreglo ordenado A, un elemento k a buscar y dos índices i,j que indican el rango de búsqueda, devuelve el índice que ocupa k en A.
# En la llamada original: i=0, k=len(A)-1
def busqueda_binaria(A, k, i, j):
    media = math.floor((i + j) / 2)

    if A[media] == k:
        return media

    if k < A[media]:
        return busqueda_binaria(A, k, i, media - 1)

    else:
        return busqueda_binaria(A, k, media + 1, j)
    



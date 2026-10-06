from math import floor

#Implementación de MERGE_SORT que recibe un arreglo a ordenar A
def merge_sort(A):

    if len(A) <= 1:
        return A

    media = floor(len(A) / 2)
    
    A1 = []
    A2 = []
    
    for i in range(0, media):
        A1.append(A[i])

    for i in range(media, len(A)):
        A2.append(A[i])

    A1 = merge_sort(A1)
    A2 = merge_sort(A2)

    return mezcla(A1, A2)

#Algoritmo auxiliar MEZCLA de MERGESORT que recibe dos arreglos a mezclar
def mezcla(A1, A2):

    ordenada = []

    i = 0
    j = 0
    
    while i < len(A1) and j < len(A2):
        if A1[i] <= A2[j]:
            ordenada.append(A1[i])
            i = i + 1

        else:
            ordenada.append(A2[j])
            j = j + 1

    while i < len(A1):
        ordenada.append(A1[i])
        i = i + 1

    while j < len(A2):
        ordenada.append(A2[j])
        j = j + 1

    return ordenada


#Implementación de QUICK_SORT que recibe un arreglo a ordenar A y 2 índices que indican el tamaño del subarreglo
# En la primera iteración p=0 y r=len(A)-1
def quick_sort(A, p, r):
    if p < r:
        q = particion(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)


#Algoritmo auxiliar de quick_sort. Tomamos el elemento al extremo derecho como el pivote
def particion(A, p, r):
    x = A[r]
    i = p - 1

    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            intercambia(A, i, j)

    intercambia(A, i + 1, r)
    return i + 1
    

#Algoritmo auxiliar que recibe un arreglo y dos índices loa sucales van a intercambiar elementos
def intercambia(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

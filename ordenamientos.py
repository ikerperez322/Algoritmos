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
    

        

from random import randrange

numeros = [randrange(0, 200) for i in range(10)]

def trocar(indice1, indice2, lista):
    memoria = lista[indice1]
    lista[indice1] = lista[indice2]
    lista[indice2] = memoria

def bubble_sort(lista):
    for i in range(len(lista) -1):
        for j in range(i+1, len(lista)):
            if lista[i] > lista[j]:
                trocar(i, j, lista)
    return lista


print(bubble_sort(numeros))
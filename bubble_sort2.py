from random import randrange, choice
import string

#esse código engloba duas questões: 9 e 10
#ele se encontra na questão 10
#para alterar para questão 9 basta trocar as variavel letras por numeros nas linhas 36 e 38

numeros = [randrange(0, 200) for i in range(10)]

def letra_aleatoria():
    return choice(string.ascii_uppercase)

def palavra_aleatoria(qtd_letras):
    palavra = ""
    for i in range(qtd_letras):
        palavra+=letra_aleatoria()
    return palavra

letras = [palavra_aleatoria(3) for i in range(10)]


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


print("Desordenado: ")
print(letras)
print("Ordem alfabética: ")
print(bubble_sort(letras))
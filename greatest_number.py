lista = [ 5, 6 , 10, 89, 56, 821, 89, 78, 57, 2 ,7,101, 234, 466, 115]

def achar_maior_valor(array):
    maior_valor = array[0];
    for i in range(1, len(array)):
        if array[i] > maior_valor:
            maior_valor = array[i]
    return maior_valor

print(achar_maior_valor(lista))
from random import randrange

espadas = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

def embaralhar(lista):
    for indice in range(len(lista)*2):
        #para passar por todo o baralho 2x sem ultrapassar o último indice da lista
        if indice >= len(lista):
            indice -= len(lista)
        
        memoria = lista[indice]
        
        #a carta aleatória não pode ser a mesma do indice para que haja  a troca
        aleatorio = randrange(0, len(lista))
        while indice == aleatorio:
            aleatorio = randrange(0, len(lista))

        carta_aleatoria = lista[aleatorio]
        
        #troca da carta aleatória pela carta em que o indice está passando
        lista[indice] = carta_aleatoria
        lista[aleatorio] = memoria
        
    
    return lista
    
lista_ordenada = []
def selection_sort(lista):
    global lista_ordenada
    #vai retirando o menor número da lista até ela ficar vazia
    while len(lista) != 0:
        indice_menor = 0;
        for indice in range(len(lista)):
            numero_atual = converter_carta_numero(lista[indice])
            numero_menor = converter_carta_numero(lista[indice_menor])
            if numero_atual < numero_menor:
                indice_menor = indice
        #adiciona sempre o menor número da lista fazendo que ela vá sendo preenchida ordenadamente
        lista_ordenada.append(lista.pop(indice_menor))
        #chamada recursiva da função até que a lista embaralhada esteje vazia
        selection_sort(lista)
        
    return lista_ordenada


#retorna o valor que cada carta não numérica tem no baralho para comparar com as cartas numéricas
def converter_carta_numero(carta: str):
    match carta:
        case "A":
            return 1
        case "J":
            return 11
        case "Q":
            return 12
        case "K":
            return 13
        case _:
            return int(carta)


print("Cartas embaralhadas: ")
embaralhado = embaralhar(espadas)
print(embaralhado)
print("")
print("Cartas ordenadas: ")
print(selection_sort(embaralhado))


tabuleiro = {}
#o tabuleiro de xadrez contém 64 casas, portanto vai de 1 a 64
#a cada casa dobra-se o número de grãos colocados sobre a casa
def espalhar_graos():
    global tabuleiro
    graos = 1
    for i in range(1, 65):
        if(i != 1):
            graos *= 2
        tabuleiro[graos] = i

def buscar_casa(qtd_graos):
    global tabuleiro
    if tabuleiro.get(qtd_graos) == None:
        print("Não há nenhuma casa no tabuleiro com essa quantidade de grãos.")
    else:
        print(tabuleiro.get(qtd_graos))


espalhar_graos()
buscar_casa(16)
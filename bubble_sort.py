from random import randrange
class Questao8():

    def __init__(self):
        self.__a = [randrange(0, 150) for i in range(10)]
        self.__nItems = len(self.__a)
    
    def __str__(self):
        print(self.__a)

    def par(self):
        if self.__a % 2 == 0:
            return True
        else:
            return False
    
    def swap(self, indice1, indice2):
        memoria = self.__a[indice1]
        self.__a[indice1] = self.__a[indice2]
        self.__a[indice2] = memoria
       
    def bubbleSort(self):                        
        #variaveis para otimizacao, diminuindo o tamanho da lista pelas extremidades à medida em que vai sendo ordenada
        _inner = 0
        last = self.__nItems -1
        #loop com metade do número de itens na lista pois há dois outros loops dentro deste, um de ida e um de volta
        for i in range(self.__nItems // 2): 
            #loop de ida, do início ao fim do array
            for inner in range(last):      
                if self.__a[inner] > self.__a[inner+1]:  
                    self.swap(inner, inner+1) 
            last -= 1 
            #loop de volta, do fim até o início do array
            for _last in range(self.__nItems -1, _inner, -1):
                if self.__a[_last-1] > self.__a[_last]:
                    self.swap(_last-1, _last)
            _inner += 1
   


questao8 = Questao8()
print("Desordenada: ")
questao8.__str__()
questao8.bubbleSort()
print("Ordenada: ")
questao8.__str__()


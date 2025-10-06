class Camisa:
    def __init__(self):
        self.__tamanho: str = ""

    def getTamanho(self):
        return self.__tamanho

    def setTamanho(self, tamanho: str):
        if tamanho != "PP" \
            and tamanho != "P" \
            and tamanho != "M" \
            and tamanho != "G" \
            and tamanho != "GG" \
            and tamanho != "XG" :
            print("fail: erro no tamanho")
            return

        self.__tamanho = tamanho

camisa = Camisa() 
while camisa.getTamanho() == "": 
    print("Digite seu tamanho de roupa")
    tamanho = input() 
    camisa.setTamanho(tamanho) 

print("Parabens, você comprou uma roupa tamanho", camisa.getTamanho())


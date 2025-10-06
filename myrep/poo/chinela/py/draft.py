class Chinela:
    def __init__(self):
        self.__tamanho = 0

    def getTamanho(self):
        return self.__tamanho

    def setTamanho(self, tamanho: int):
        if tmanho > 50 or tamanho < 20:
            print("fail: deu erro amigo")
            return
        self.__tamanho = tamanho

chinela = Chinela()
while chinela.getTamanho() == 0:
    print("Digite seu tamanho de chinela")
    tamanho = int(input())
    chinela.setTamanho(tamanho)

print("Parabens, você comprou uma chinela tamanho", chinela.getTamanho())

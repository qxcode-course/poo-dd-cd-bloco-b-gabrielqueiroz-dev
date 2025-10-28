class Bateria:
  def __init__(self, capacidade: int):
    self.__carga: int = capacidade
    self.__capacidade: int = capacidade

  def setCarga(self, carga: int):
    if 0 > carga:
      print("erro: carga inválida")
      return
    
    if carga > self.__capacidade:
      self.__carga = self.__capacidade
      return

    self.__carga = carga

  def getCarga(self):
    return self.__carga
  
  def mostrar(self):
    print(self)
  
  def __str__(self):
    return f"({self.__carga}/{self.__capacidade})"
  


class Carregador:
  def __init__(self, potencia: int):
    self.__potencia: int = potencia

  def getPotencia(self):
    return self.__potencia
  
  def setPotencia(self, potencia: int):
    self.__potencia = potencia

  def mostrar(self):
    print(self)

  def __str__(self):
    return f"(Potência {self.__potencia})"



class Notebook:
  def __init__(self):
    self.__ligado: bool = False
    self.__bateria: Bateria | None = None
    self.__carregador: Carregador | None = None

  def setLigado(self, ligado: bool):
    self.__ligado = ligado

  def getLigado(self):
    return self.__ligado
  
  def setBateria(self, bateria: Bateria):
    self.__bateria = bateria

  def getBateria(self):
    return self.__bateria

  def setCarregador(self, carregador: Carregador):
    self.__carregador = carregador

  def getCarregador(self):
    return self.__carregador

  def rmBateria(self):
    bateria_removida = self.__bateria
    self.__bateria = None
    print("bateria removida")
    return bateria_removida
  
  def ligar(self):
    if self.getBateria() == None and self.getCarregador() == None:
      print("erro: não foi possível ligar")
      return

    if self.getBateria() != None and self.getBateria().getCarga() == 0 and self.getCarregador() == None:
      print("erro: bateria sem carga")
      return

    self.setLigado(True)
    print("Notebook ligado")

  def desligar(self):
    self.setLigado(False)
    print("Notebook desligado")
  
  def usar(self, minutes: int):
    if not self.getLigado():
      print("erro: notebook desligado")
      return
    
    if self.getBateria().getCarga() < minutes and self.getCarregador() == None:
      print(f"Usando por {self.getBateria().getCarga()} minutos")
      self.getBateria().setCarga(0)
      self.setLigado(False)
      return
    
    if self.getCarregador() != None:
      print(f"Usando por {minutes} minutos")
      self.getBateria().setCarga(
        self.getCarregador().getPotencia() * minutes + self.getBateria().getCarga()
      )
      return

    print(f"Usando por {minutes} minutos")
    self.getBateria().setCarga(self.getBateria().getCarga() - minutes)

  def mostrar(self):
    print(self)

  def __str__(self):
    return f"Status: {"Ligado" if self.getLigado() else "Desligado"}, " + \
           f"Bateria: {"Nenhuma" if self.getBateria() == None else self.getBateria()}, " + \
           f"Carregador: {"Desconectado" if self.getCarregador() == None else self.getCarregador()}"

notebook = Notebook() # criando notebook
notebook.mostrar()    # msg: Status: Desligado, Bateria: Nenhuma, Carregador: Desconectado
notebook.ligar()      # msg: não foi possível ligar
notebook.usar(10)     # msg: notebook desligado

bateria = Bateria(50) # criando bateria que suporta 50 minutos e começa carregada
bateria.mostrar()     # (50/50)
notebook.setBateria(bateria) # coloca a bateria no notebook

notebook.mostrar() # msg: Status: Desligado, Bateria: (50/50), Carregador: Desconectado
notebook.ligar()   # msg: notebook ligado
notebook.mostrar() # msg: Status: Ligado, Bateria: (50/50), Carregador: Desconectado
notebook.usar(30)  # msb: Usando por 30 minutos
notebook.mostrar() # msg: Status: Ligado, Bateria: (20/50), Carregador: Desconectado
notebook.usar(30)  # msb: Usando por 20 minutos, notebook descarregou
notebook.mostrar() # msg: Status: Desligado, Bateria: (0/50), Carregador: Desconectado

bateria = notebook.rmBateria() # msg: bateria removida
bateria.mostrar()  # (0/50)
notebook.mostrar() # msg: Status: Desligado, Bateria: Nenhuma, Carregador: Desconectado

carregador = Carregador(2) # criando carregador com 2 de potencia
carregador.mostrar() # (Potência 2)

notebook.setCarregador(carregador) # adicionando carregador no notebook
notebook.mostrar() # msg: Status: Desligado, Bateria: Nenhuma, Carregador: (Potência 2)
notebook.ligar()   # msg: notebook ligado
notebook.mostrar() # msg: Status: Ligado, Bateria: Nenhuma, Carregador: (Potência 2)

notebook.setBateria(bateria)
notebook.mostrar() # msg: Status: Ligado, Bateria: (0/50), Carregador: (Potência 2)
notebook.usar(10)  # msg: Notebook utilizado com sucesso
notebook.mostrar() # msg: Status: Ligado, Bateria: (20/50), Carregador: (Potência 2)

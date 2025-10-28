class Bateria:
  def __init__(self, capacidade: int):
    self.__carga: int = capacidade
    self.__capacidade: int = capacidade

  def setCarga(self, carga: int):
    if 0 > carga:
      print("fail: carga inválida")
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
    return f"{self.__carga}/{self.__capacidade}"
  


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
    return f"{self.__potencia}W"



class Notebook:
  def __init__(self):
    self.__ligado: bool = False
    self.__bateria: Bateria | None = None
    self.__carregador: Carregador | None = None
    self.__uso: int = 0

  def setLigado(self, ligado: bool):
    self.__ligado = ligado

  def getLigado(self):
    return self.__ligado
  
  def setBateria(self, bateria: Bateria):
    self.__bateria = bateria

  def getBateria(self):
    return self.__bateria

  def setCarregador(self, carregador: Carregador):
    if self.getCarregador() != None:
      print("fail: carregador já conectado")
      return
    self.__carregador = carregador

  def getCarregador(self):
    return self.__carregador
  
  def rmCarregador(self):
    if self.getCarregador() == None:
      print("fail: Sem carregador")
      return
    
    if self.getBateria() == None:
      self.desligar()

    carregador_removido = self.getCarregador()
    self.__carregador = None
    return carregador_removido

  def rmBateria(self):
    bateria_removida = self.getBateria()

    if bateria_removida == None:
      print("fail: Sem bateria")
      return
    
    if self.getCarregador() == None:
      self.desligar()

    self.__bateria = None
    return bateria_removida
  
  def ligar(self):
    if self.getBateria() == None and self.getCarregador() == None:
      print("fail: não foi possível ligar")
      return

    if self.getBateria() != None and self.getBateria().getCarga() == 0 and self.getCarregador() == None:
      print("fail: bateria sem carga")
      return

    self.setLigado(True)

  def desligar(self):
    self.setLigado(False)
  
  def usar(self, minutes: int):
    if not self.getLigado():
      print("fail: desligado")
      return

    if self.getBateria() != None and \
        self.getBateria().getCarga() <= minutes and \
        self.getCarregador() == None:
      self.__uso += self.getBateria().getCarga()
      self.getBateria().setCarga(0)
      self.desligar()
      print("fail: descarregou")
      return
    
    if self.getCarregador() != None and self.getBateria() != None:
      self.getBateria().setCarga(
        self.getCarregador().getPotencia() * minutes + self.getBateria().getCarga()
      )
      self.__uso += minutes
    elif self.getCarregador() != None and self.getBateria() == None:
      self.__uso += minutes
    elif self.getBateria() != None:
      self.getBateria().setCarga(self.getBateria().getCarga() - minutes)
      self.__uso += minutes

  def getUso(self):
    return self.__uso

  def mostrar(self):
    print(self)

  def __str__(self):
    finalString = ""

    finalString += f"Notebook: {f"ligado por {self.getUso()} min" if self.getLigado() else "desligado"}"

    if self.getCarregador() != None:
      finalString += f", Carregador {self.getCarregador()}"
    
    if self.getBateria() != None:
      finalString += f", Bateria {self.getBateria()}"
    
    return finalString

notebook = Notebook() # criando notebook
carregador = None
bateria = None

while True:
  comando = input()
  print(f"${comando}")
  args = comando.split()

  if args[0] == "end":
    break

  elif args[0] == "init":
    notebook = Notebook()
    print("notebook criado")

  elif args[0] == "show":
    notebook.mostrar()

  elif args[0] == "turn_on":
    notebook.ligar()

  elif args[0] == "turn_off":
    notebook.desligar()

  elif args[0] == "use":
    notebook.usar(int(args[1]))

  elif args[0] == "bateria":
    bateria = Bateria(int(args[1]))
    print("bateria criada")

  elif args[0] == "set_battery":
    bateria = Bateria(int(args[1]))
    notebook.setBateria(bateria)

  elif args[0] == "rm_battery":
    bateria = notebook.rmBateria()
    if bateria != None:
      print(f"Removido {bateria}")

  elif args[0] == "set_charger":
    carregador = Carregador(int(args[1]))

    notebook.setCarregador(carregador)

  elif args[0] == "rm_charger":
    carregador = notebook.rmCarregador()
    if carregador != None:
      print(f"Removido {carregador}")
  
  else:
    print("fail: comando inválido")
    
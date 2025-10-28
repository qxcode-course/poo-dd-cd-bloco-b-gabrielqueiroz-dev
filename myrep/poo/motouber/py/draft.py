class Pessoa:
  def __init__(self, nome: str, dinheiro: int):
    self.__nome = nome
    self.__dinheiro = dinheiro

  def getNome(self):
    return self.__nome

  def getDinheiro(self):
    return self.__dinheiro
  
  def setDinheiro(self, valor: int) -> bool:
    self.__dinheiro = valor
  
  def __str__(self):
    return f"{self.getNome()}:{self.getDinheiro()}"
  
class Moto:
  def __init__(self):
    self.__passageiro: Pessoa | None = None
    self.__motorista: Pessoa | None = None
    self.__custoCorridaAtual: int = 0

  def getMotorista(self) -> Pessoa | None:
    return self.__motorista

  def setMotorista(self, motorista: Pessoa):
    self.__motorista = motorista

  def getPassageiro(self) -> Pessoa | None:
    return self.__passageiro
  
  def setPassageiro(self, passageiro: Pessoa):
    if self.getMotorista() is None:
      print("Não é possível adicionar passageiro sem motorista.")
      return
  
    self.__passageiro = passageiro

  def getCustoCorridaAtual(self) -> float:
    return self.__custoCorridaAtual

  def setCustoCorridaAtual(self, custo: float):
    self.__custoCorridaAtual = custo

  def drive(self, cost: int):
    if self.getMotorista() is None or self.getPassageiro() is None:
      print("Não é possível dirigir sem motorista e passageiro.")
      return

    self.setCustoCorridaAtual(
      self.getCustoCorridaAtual() + cost
    )

  def removePassageiro(self):
    if self.getPassageiro() is None:
      print("Não há passageiro para remover.")
      return None
    
    passageiro = self.getPassageiro()

    if self.getCustoCorridaAtual() > self.getPassageiro().getDinheiro():
      print("fail: Passenger does not have enough money")
      self.getMotorista().setDinheiro(
        self.getMotorista().getDinheiro() +
        self.getCustoCorridaAtual()
      )
      self.setCustoCorridaAtual(0)
      self.getPassageiro().setDinheiro(0)
      self.setPassageiro(None)
      return passageiro

    self.getPassageiro().setDinheiro(
      self.getPassageiro().getDinheiro() -
      self.getCustoCorridaAtual()
    )

    self.getMotorista().setDinheiro(
      self.getMotorista().getDinheiro() +
      self.getCustoCorridaAtual()
    )

    self.setPassageiro(None)
    self.setCustoCorridaAtual(0)
    return passageiro

  def __str__(self):
    return f"Cost: {self.getCustoCorridaAtual()}, Driver: {self.getMotorista()}, Passenger: {self.getPassageiro()}"


moto = Moto()
motorista = Pessoa("", 0.0)
passageiro = Pessoa("", 0.0)

while True:
  comando = input()
  print("$" + comando)
  args = comando.split()

  if args[0] == "end":
    break
  elif args[0] == "show":
    print(moto)
  elif args[0] == "setDriver":
    nome = args[1]
    dinheiro = int(args[2])
    motorista = Pessoa(nome, dinheiro)
    moto.setMotorista(motorista)
  elif args[0] == "setPass":
    nome = args[1]
    dinheiro = int(args[2])
    passageiro = Pessoa(nome, dinheiro)
    moto.setPassageiro(passageiro)
  elif args[0] == "drive":
    custo = int(args[1])
    moto.drive(custo)
  elif args[0] == "leavePass":
    passageiro = moto.removePassageiro()
    if passageiro is not None:
      print(f"{passageiro} left")
  else:
    print("comando inválido")
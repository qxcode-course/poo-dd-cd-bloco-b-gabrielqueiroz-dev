class Lead:
  def __init__(self, thickness: float, hardness: str, size: int):
    self.__thickness = thickness
    self.__hardness = hardness
    self.__size = size

  def usagePerSheet(self) -> float:
    usage = {
      "HB": 1,
      "2B": 2,
      "4B": 4,
      "6B": 6
    }
    return usage.get(self.getHardness(), 0)
    
  def getThickness(self) -> float:
    return self.__thickness

  def getHardness(self) -> str:
    return self.__hardness

  def getSize(self) -> int:
    return self.__size

  def setSize(self, size: int):
    self.__size = size

  def __str__(self):
    return f"[{self.getThickness()}:{self.getHardness()}:{self.getSize()}]"


class Pencil:
  def __init__(self, thickness: str):
    self.__thickness = thickness
    self.__lead: Lead | None = None

  def writePage(self) -> bool:
    if not self.hasGraffite():
      print("fail: nao existe grafite")
      return False
    
    grafite = self.__lead
    usage = grafite.usagePerSheet()

    if grafite.getSize() <= 10:
      print("fail: tamanho insuficiente")
      grafite.setSize(10)
      return False
    
    if grafite.getSize() - usage < 10:
      print("fail: folha incompleta")
      grafite.setSize(10)
      return False
  
    grafite.setSize(grafite.getSize() - usage)
    return True

  def hasGraffite(self) -> bool:
    return self.__lead is not None
  
  def remove(self) -> Lead | None:
    if not self.hasGraffite():
      print("fail: nao existe grafite")
      return None
    removed = self.__lead
    self.__lead = None
    return removed
  
  def insert(self, lead: Lead) -> bool:
    if self.hasGraffite():
      print("fail: ja existe grafite")
      return False
    if lead.getThickness() != self.getThickness():
      print("fail: calibre incompativel")
      return False
    self.__lead = lead
    return True

  def getThickness(self) -> str:
    return self.__thickness

  def setThickness(self, thickness: str):
    self.__thickness = thickness

  def __str__(self):
    return f"calibre: {self.getThickness()}, grafite: {self.__lead if self.hasGraffite() else 'null'}"
  
pencil = Pencil("0.5")
lead = Lead(0.5, "HB", 50)

while True:
  command = input().split()
  print("$" + " ".join(command))

  if command[0] == "end":
    break
  elif command[0] == "init":
    pencil = Pencil(float(command[1]))
  elif command[0] == "insert":
    lead = Lead(float(command[1]), command[2], int(command[3]))
    pencil.insert(lead)
  elif command[0] == "show":
    print(pencil)
  elif command[0] == "remove":
    pencil.remove()
  elif command[0] == "write":
    pencil.writePage()
  else:
    print("fail: comando invalido")
class Tamagochi:
  def __init__(self, energyMax, cleanMax):
    self.__energyMax = energyMax
    self.__cleanMax = cleanMax
    self.__energy = energyMax
    self.__clean = cleanMax
    self.__age = 0
    self.__alive = True
  
  def setEnergy(self, energy):
    if energy <= 0:
      self.__energy = 0
      self.__alive = False
      return
  
    if energy > self.__energyMax:
      self.__energy = self.__energyMax
      return
    
    self.__energy = energy

  def setClean(self, clean):
    if clean <= 0:
      self.__clean = 0
      self.__alive = False
      return
  
    if clean > self.__cleanMax:
      self.__clean = self.__cleanMax
      return
    
    self.__clean = clean

  def setAge(self, age):
    if age < 0:
      self.__age = 0
      return
    
    self.__age = age

  def getEnergy(self):
    return self.__energy
  
  def getEnergyMax(self):
    return self.__energyMax

  def getClean(self):
    return self.__clean

  def getCleanMax(self):
    return self.__cleanMax

  def getAge(self):
    return self.__age

  def isAlive(self):
    return self.__alive
  
  def __str__(self):
    return f"E:{self.getEnergy()}/{self.getEnergyMax()}, L:{self.getClean()}/{self.getCleanMax()}, I:{self.getAge()}"
  

class Game:
  def __init__(self, tamagochi):
    self.__tamagochi = None
    self.__turnos = 1
    self.setPet(tamagochi)

  def setPet(self, tamagochi):
    self.__tamagochi = tamagochi
    self.__turnos = 1

  def testAlive(self) -> bool:
    return self.getPet().isAlive()

  def getPet(self):
    return self.__tamagochi
  
  def show(self):
    self.__turnos += 1
    return str(self.getPet())

  def play(self):
    if not self.testAlive():
      print("fail: pet esta morto")
      return

    self.getPet().setEnergy(self.getPet().getEnergy() - 2)
    self.getPet().setClean(self.getPet().getClean() - 3)
    self.getPet().setAge(self.getPet().getAge() + 1)
    self.__turnos += 1

    if not self.testAlive():
      if self.getPet().getEnergy() <= 0:
        print("fail: pet morreu de fraqueza")
      elif self.getPet().getClean() <= 0:
        print("fail: pet morreu de sujeira")
  
  def sleep(self):
    if not self.testAlive():
      print("fail: pet esta morto")
      return
    
    minToSleep = 5
    if self.getPet().getEnergyMax() - self.getPet().getEnergy() < minToSleep:
      print("fail: nao esta com sono")
      return

    self.getPet().setEnergy(self.getPet().getEnergyMax())
    self.getPet().setAge(self.getPet().getAge() + self.__turnos)
    self.__turnos += 1

  def shower(self):
    if not self.testAlive():
      print("fail: pet esta morto")
      return 

    self.getPet().setEnergy(self.getPet().getEnergy() - 3)
    self.getPet().setClean(self.getPet().getCleanMax())
    self.getPet().setAge(self.getPet().getAge() + 2)
    self.__turnos += 1
  
pet = Tamagochi(0, 0)
game = Game(pet)

while True:
  command = input()
  print("$"+command)
  args = command.split()

  if args[0] == "init":
    pet = Tamagochi(int(args[1]), int(args[2]))
    game.setPet(pet)
  elif args[0] == "show":
    print(game.show())
  elif args[0] == "end":
    break
  elif args[0] == "play":
    game.play()
  elif args[0] == "sleep":
    game.sleep()
  elif args[0] == "shower":
    game.shower()
  else:
    print("Invalid command")

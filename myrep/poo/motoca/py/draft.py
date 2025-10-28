class Person:
  def __init__(self, name, age):
    self.__name = name
    self.__age = age

  def getName(self):
    return self.__name

  def getAge(self):
    return self.__age

  def setName(self, name):
    self.__name = name

  def setAge(self, age):
    self.__age = age

  def __str__(self):
    return f"{self.getName()}:{self.getAge()}"
  
class Motorcycle:
  def __init__(self, power: int = 1):
    self.__power: int = power
    self.__time: int = 0
    self.__person: Person | None = None

  def getPower(self) -> int:
    return self.__power

  def getTime(self) -> int:
    return self.__time

  def getPerson(self) -> Person | None:
    return self.__person

  def setPower(self, power: int):
    self.__power = power

  def setTime(self, time: int):
    self.__time = time

  def insertPerson(self, person: Person) -> bool:
    if self.getPerson() is not None:
      print("fail: busy motorcycle")
      return False

    self.__person = person
    return True
    
  def remove(self) -> Person | None:
    if self.getPerson() is None:
      print("fail: empty motorcycle")
      return None

    person = self.getPerson()
    self.__person = None
    return person
  
  def buyTime(self, time: int):
    if time <= 0:
      print("fail: invalid time")
      return

    self.setTime(self.getTime() + time)

  def drive(self, time: int):
    if self.getTime() <= 0:
      print("fail: buy time first")
      return
    
    if self.getPerson() is None:
      print("fail: empty motorcycle")
      return

    if self.getPerson().getAge() > 10:
      print("fail: too old to drive")
      return
    
    if time > self.getTime():
      print(f"fail: time finished after {self.getTime()} minutes")
      self.setTime(0)
      return

    self.setTime(self.getTime() - time)

    if self.getTime() < 0:
      self.setTime(0)
      print(f"fail: time finished after {time} minutes")

  def honk(self):
    print("P" + "e" * self.getPower() + "m")

  def __str__(self):
    person_str = self.getPerson() if self.getPerson() is not None else "empty"
    return f"power:{str(self.getPower())}, time:{self.getTime()}, person:({self.getPerson() if self.getPerson() is not None else 'empty'})"

moto = Motorcycle()

while True:
  command = input().split()
  print(f"${' '.join(command)}")
  
  if command[0] == "end":
    break
  elif command[0] == "show":
    print(moto)
  elif command[0] == "enter":
    name = command[1]
    age = int(command[2])
    person = Person(name, age)
    moto.insertPerson(person)
  elif command[0] == "leave":
    removed = moto.remove()
    if removed is not None:
      print(removed)
  elif command[0] == "buy":
    time = int(command[1])
    moto.buyTime(time)
  elif command[0] == "drive":
    time = int(command[1])
    moto.drive(time)
  elif command[0] == "honk":
    moto.honk()
  elif command[0] == "init":
    power = int(command[1])
    moto = Motorcycle(power)
  else:
    print("fail: invalid command")
    
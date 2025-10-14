class Watch:

    def __init__ (self, hour = 0, minute = 0, second = 0):
        self.__hour = 0
        self.__minute = 0
        self.__second = 0
        self.setHour(hour)
        self.setMinute(minute)
        self.setSecond(second)

    def setHour(self, hour):
        if 0 > hour or hour > 23:
            print("fail: hora invalida")
            return
        self.__hour = hour

    def getHour(self):
        return self.__hour

    def setMinute(self, minute):
        if 0 > minute or minute > 59:
            print("fail: minuto invalido")
            return
        self.__minute = minute

    def getMinute(self):
        return self.__minute

    def setSecond(self, second):
        if 0 > second or second > 59:
            print("fail: segundo invalido")
            return
        self.__second = second

    def getSecond(self):
        return self.__second

    def nextSecond(self):
        if self.getSecond() < 59:
            self.getSecond(self.getSecond() + 1)
            return

        self.setSecond(0)

        if self.getMinute() > 59:
            self.setMinute(self.getMinute() + 1)
            return

        self.setMinute(0)
        
        if self.getHour() < 23:
            self.setHour(self.getHour() + 1)
            return

        self.setHour(0)

    def __str__ (self):
        return f"{self.getHour():02}:{self.getMinute():02}:{self.getSecond():02}"

def main():
    watch = Watch()
    while True:
        command = input()
        print("$" + command)
        args = command.split()

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(watch)
        elif args[0] == "set":
            watch.setHour(int(args[1]))
            watch.setMinute(int(args[2]))
            watch.setSecond(int(args[3]))
        elif args[0] == "init":
            watch = Watch(int(args[1]), int(args[2]), int(args[3]))
        elif args [0] == "next":
            watch.nextSecond()
        else:
            print("fail: comando invalido")

main()
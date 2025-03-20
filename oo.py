from colorama import init

class Main:
    def __init__(self, startCheck: bool = False):
        self.startCheck = startCheck

    def printStart(self):
        print(self.startCheck)

    def startTimer(self):
        self.startCheck = True

    def checkStart(self):
        self.startCheck = True

if __name__ == "__main__":
    main_instance = Main(startCheck=True)
    main_instance.printStart()
    main_instance.startTimer()
    main_instance.checkStart()
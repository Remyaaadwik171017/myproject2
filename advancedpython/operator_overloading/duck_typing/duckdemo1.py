#duck typing
# if a bird walking like a duck,quacks like a duck, then it must be a duck
#methods are important

class Pycharm:
    def open(self):
        print("pycharm open method")
    def run(self):
        print("pycharm funclty is running")
    def debug(self):
        print("pycharm debugging errors ")

class Vscode:
    def open(self):
        print("vscode open method")
    def run(self):
        print("vscode funclty is running")
    def debug(self):
        print("vscode debugging errors ")
class Person:
    def coding(self,idle):
        idle.open()
        idle.run()
        idle.debug()
py=Pycharm()
vs=Vscode()
p=Person()
p.coding(py)
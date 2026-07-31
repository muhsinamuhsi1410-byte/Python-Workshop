#car and engine composition

class Engine:
    def start(self):
        print("Engine is running")
class Car:
    def __init__(self,make,model):
        self.make=make
        self.model=model
        self.engine=Engine()
    def start_car(self):
        self.engine.start()
car=Car("Toyota","innova")
car.start_car()

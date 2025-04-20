class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def display(self):
        print(f"Car:{self.brand}{self.model}")
car1=Car("Toyota","Camry")
car2=Car("Honda","Civic")

car1.display()
car2.display()
class Car:
    def __init__(self, brand, speed, fuel):
        self.brand = brand
        self.speed = speed
        self.fuel = fuel

    def drive(self):
        self.fuel -= 5
        print(f"{self.brand} is driving. Fuel: {self.fuel}")

    def accelerate(self):
        self.speed += 10
        print(f"{self.brand} speed: {self.speed}")

    def show_info(self):
        print(f"Brand: {self.brand}")
        print(f"Speed: {self.speed}")
        print(f"Fuel: {self.fuel}")


car1 = Car("Toyota", 0, 50)
car2 = Car("BMW", 0, 60)

car1.drive()
car1.accelerate()
car1.show_info()

car2.drive()
car2.accelerate()
car2.show_info()
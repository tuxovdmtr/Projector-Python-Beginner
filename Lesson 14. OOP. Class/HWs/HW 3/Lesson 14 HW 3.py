# Create a Car class with the following attributes:
# brand, model, year, and speed.
# The Car class should have the following methods:
# accelerate, brake and display_speed.
# The accelerate method should increase the speed by 5,
# and the brake method should decrease the speed by 5.
# Remember that the speed cannot be negative.

class Car:
    def __init__(self, brand: str, model: str, year: int, speed: int):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed
        if self.speed < 0:
            raise ValueError("Speed can't be negative")
    
    def accelerate(self,):
        self.speed += 5
        return self.speed

    def brake(self,):
        self.speed -= 5
        if self.speed < 0:
            self.speed = 0
        else:
            return self.speed
        return self.speed

    def display_speed(self):
        print(f"Your speed is {self.speed}")
    
car = Car("Nissan", "ModelX", 2020, 0)
print(car.brand)
print(car.model)
print(car.year)
print(car.speed)
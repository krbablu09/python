class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"my car brand are {self.brand} and model {self.model}"
           

class ElectricCar(Car):
    def __init__(self,brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

my_tesla = ElectricCar("Tesla", "Model s", "85kwh")
print(f" {my_tesla.full_name()} and battery size {my_tesla.battery_size}")
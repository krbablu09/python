class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand + "!"   

    def full_name(self):
        return f"my car brand {self.__brand} and model {self.model}"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)  
        self.battery_size = battery_size

my_tesla = ElectricCar("Tesla", "Model S", "85kwh")

print(my_tesla.get_brand())
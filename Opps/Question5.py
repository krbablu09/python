class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand + " !" 

    def full_name(self):
        return f"my car brand {self.__brand} and model {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"    

my_tesla = ElectricCar("Tesla", "model s", "85kwh")

safari = Car("Tata", "Safari")

print(safari.fuel_type())
print(my_tesla.fuel_type())


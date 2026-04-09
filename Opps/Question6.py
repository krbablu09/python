class Car:
    total_car = 0
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_car += 1 

    def get_brand(self):
        return self.__brand + " !"    

    def full_name(self):
        return f"my car brand {self.__brand} and model {self.model}"
    
    def fuel_type(self):
        return f"Petrol and Diesal"
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return f"Elecric Charge"

my_tesla = ElectricCar("Tesla", "model s", "85kwh") 

safari = Car("TATA", "Safari")
safariThree = Car("TATA", "Nexon")
print(Car.total_car)
 




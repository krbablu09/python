class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = brand

    def get_brand(self):
        return self.brand + " !"

    def full_name(self):
        return f"my car brand {self.__brand} and Model {self.__model}"

    def fuel_type(self):
        return "Petrol and Diesal"

    @staticmethod
    def general_description():
        return "Cars are means of transport"

    @property
    def model(self):
        return self.__model  

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"  

class Battery:
    def battery_info(self):
        return "This is battery"

class Engine:  
    def engine_info(self):
        return "This is engine"


class ElectricCar2(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCar2("Tesla", "Model S")
print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())




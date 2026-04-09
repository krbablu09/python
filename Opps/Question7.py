class Car:
    total_car = 0
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand  + " !"

    def full_name(self):
        return f"my car brand {self.__brand} and Model {self.model}"

    def fuel_type(self):
        return "Petrol and Diesal"

    @staticmethod
    def general_description():
        return "Cars are means of transport"    

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"

my_tesla = ElectricCar("Tesla", "Model s", "85kwh")
my_car = Car("Tata", "Safari")


print(my_car.general_description())
print(Car.general_description())
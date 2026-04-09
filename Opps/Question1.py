class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


my_car = Car("Toyota", "Corolla") 
print(f"May car brand is {my_car.brand} and model is {my_car.model}") 

my_new_car = Car("TATA", "Safari")
print(f"May car brand is {my_new_car.brand} and model is {my_new_car.model}")
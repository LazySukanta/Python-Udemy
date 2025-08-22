class Car:
  def __init__(self,brand,model):
    self.brand = brand
    self.model = model

  def full_name(self):
    return f"{self.brand} {self.model}"


class ElectricCar(Car):
  def __init__(self,brand,model,battery_size):
    super().__init__(brand,model)
    self.battery_size = battery_size


# my_car = Car('Mercedes','Benz')
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())


my_new_car = ElectricCar('Tesla','ModelS','99KM')

print(my_new_car.full_name(), my_new_car.battery_size)
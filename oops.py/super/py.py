class car:
  def __init__(self,type):
    self.type=type

  @staticmethod
  def start():
    print("your car is started")

  @staticmethod
  def stop():
    print("your car is stoped")


class toyota(car):
  def __init__(self,brand,type):
    self.brand=brand
    super().__init__(type)


car1=toyota("toyota","petrol")
car1.start()
print(car1.type)
print(car1.brand)
 
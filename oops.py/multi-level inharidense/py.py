class car:
  @staticmethod
  def start():
    print("your car is started")

  @staticmethod
  def stop():
    print("your car is stoped")


class toyota(car):
  def __init__(self,brand):
    self.brand=brand

class fortuner(toyota):
  def __init__(self, type):
    self.type=type

car1=fortuner("petrol")
car1.start()

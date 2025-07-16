#when a class give there propertice and method to another class
#single inharidance 
class  car:
  @staticmethod
  def start():
    print("car is in good condition")

  @staticmethod
  def stop():
    print("car stop")

class toyotacar(car):
  def __init__(self,name):
    self.name=name

car1=toyotacar("p1")
car2=toyotacar("p2")

print(car1.start())
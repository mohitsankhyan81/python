class person:
  name = "anonymus"

  def changename(self,name):
    self.name=name

p1=person()
p1.changename("rahul kumar")
print(p1.name)
print(person.__name__)
#delete to use to delete properties and or object it self

class solution:
    def __init__(self,name):
        self.name=name

s1=solution("mohit sankhyan\nRobin is fudu banda")
print(s1.name)
del s1.name #delare the name attribute
print(sl.name)#show error because the s1. name is deleted

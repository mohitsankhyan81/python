# add function also in class / oops

class student:
    class_name="ABC collage"
    name="annonamas"
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        print("add element in class oops")

    def welcome(self):
        print("welcome Students")

s1=student("karan",43)
s1.welcome()
print(s1.name,s1.marks)

class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        
    def calavg(self):
            sum=0
            for val in self.marks:
                sum += val
            print("So your name is ", self.name,"\nand your avg is ", sum/3)


s1=student("mohit",[11,12,13])
s1.calavg()
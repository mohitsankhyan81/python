#property deceroter

class student:
  def __init__(self,phy,cme,math):
    self.phy=phy
    self.cme=cme
    self.math=math
    #self.persentage=str((self.phy+self.cme+self.math)/3)+"%"

  # def calculate(self):
  #   self.persentage=str((self.phy+self.cme+self.math)/3)+"%"

  @property
  def persentage(self):
    return str((self.phy+self.cme+self.math)/3)+"%"
    

stu1=student(91,91,81)
print(stu1.persentage)
stu1.phy=45
print(stu1.phy)
print(stu1.persentage)
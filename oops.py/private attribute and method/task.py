class account:
  def __init__(self,accNo,accPass):
    self.accNo=accNo
    self.accPass=accPass


per1=account("12345","abcde")
print(per1.accNo,per1.__accPass)

#we use __ double hash for concert any data to private

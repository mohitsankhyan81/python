class account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account = acc

    def devit(self, ammount):
        self.balance -= ammount
        print("Rs", ammount, "are devited")

    def credit(self, ammount):
        self.balance += ammount
        print("Rs", ammount, "are credited")

    def getbalance(self, ammount):
        return self.balance

person1 = account(10000, 12345)
person1.credit(500)
class account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account = acc

    def devit(self, ammount):
        self.balance -= ammount
        print("Rs", ammount, "are devited")

    def credit(self, ammount):
        self.balance += ammount
        print("Rs", ammount, "are credited")

    def getbalance(self, ammount):
        return self.balance

person1 = account(10000, 12345)
person1.credit(500)
person1.devit(1000)
person1.credit(40000)
person1.devit(5000)
print("Current balance is:", person1.getbalance(0))

print("Current balance is:", person1.getbalance(0))

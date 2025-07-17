class A:
  var1="A is good"

class B:
  var2="B is also good"

class C(A,B):
  var3="welcome to var c"


c1=C()

print(c1.var1)
print(c1.var2)
print(c1.var3)
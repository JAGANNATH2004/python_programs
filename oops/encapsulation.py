class base :
  def __init__(self):
    self.a="programming in python"
    self.c="programming in python"
class derived(base):
  def __init__(self):
    base.__init__(self)
    print('calling n number of base class : ')
    print(self.c)
obj1=base()
print(obj1.a)
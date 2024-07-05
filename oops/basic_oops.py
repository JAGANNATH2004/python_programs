class employee():
  def __init__(self,name,age,id,salary):
    self.name=name
    self.age=age
    self.salary=salary
    self.id=id
emp1=employee('harshith',22,1000,2234)
emp2=employee('arjun',23,2000,2234)
print(emp1.__dict__)
print(emp2.__dict__)
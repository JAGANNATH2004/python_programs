class person(object):
  def __init__(self,name,id,salary,post):
    self.name=name
    self.id=id
    self.salary=salary
    self.post=post
class employee(person):
  def __init__(self,name,id,salary,post):
    person.__init__(self,name,id,salary,post)
  def details(self):
    print('my name is ',self.name)
    print('id number is : ',self.id)
    print('post : ',self.post)
a=employee('smita : ',98568,50000,'intern')
a.details()
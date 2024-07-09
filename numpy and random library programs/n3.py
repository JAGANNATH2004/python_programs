import numpy as np
x=np.random.randint(0,10,40)
print("the original array is : ",x)
print("the most frequent value is : ",np.bincount(x). argmax())
print("the least frequent value is : ",np.bincount(x).argmin())
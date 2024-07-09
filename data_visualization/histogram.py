import matplotlib.pyplot as plt
emp_ages=[22,43,16,57,45,56]
bins=[0,10,20,30,40,50,60]
plt.hist(emp_ages,bins,rwidth= 0.8,color="green")
plt.xlabel('emp ages')
plt.ylabel('no. of employees')
plt.legend()
plt.show()
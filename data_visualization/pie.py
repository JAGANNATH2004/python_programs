import matplotlib.pyplot as plt
slices =[25,26,20,20,15,15]
depts=['sales','R and D','development team','production','HR','finance']
cols=['magenta','blue','green','cyan','brown','gold']
plt.figure(facecolor='orange')
plt.pie(slices,labels=depts, colors=cols,
        startangle = 90,shadow=True,explode=(0,0,0,0.2,0,0))
plt.title('INFOSYS')
plt.show()
import matplotlib.pyplot as plt
years=['2012','2013','2014','2015','2016','2017']
profits=[9,10,10.5,8.8,10.9,9.75]

plt.plot(years,profits)
plt.title('XYZ COMPANY')
plt.xlabel("YEARS")
plt.ylabel("PROFIT IN MILLION INR")
plt.legend()
plt.show()
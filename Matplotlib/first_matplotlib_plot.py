import matplotlib.pyplot as plt

x_values=[1,2,3,4,5]
y_values=[2,4,6,8,10]

plt.plot(x_values,y_values)

plt.xlabel("X axis value")
plt.ylabel("Y axis value")
plt.title("My first Matplotlib plot")
#plt.show()

plt.plot(x_values,y_values,color="yellow",marker="o")
#plt.show()

plt.grid()
plt.show()

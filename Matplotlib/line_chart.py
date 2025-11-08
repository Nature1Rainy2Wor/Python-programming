import matplotlib.pyplot as plt
days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]#x axis
vists=[250,450,560,780,774,568,789]#y axis

plt.plot(days,vists)
plt.xlabel("Days of a week")
plt.ylabel("Number of Visitors")
plt.ylabel("Score")
plt.title("Website Traffic Over a Week")

plt.show()
plt.plot(days,vists,color="rainbow",linestyle="doted dashed",linewidth=2)
plt.xlabel("Days of a week")
plt.ylabel("Number of Visitors")
plt.title("Website Traffic Over a Week")
plt.show()
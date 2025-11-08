import matplotlib.pyplot as plt
categories=["Maths","English","Chemistry","physics"]#x axis
scores=[93,80,90,99]#y axis

plt.bar(categories,scores ,color="Lavender")
plt.xlabel("Subjects")
plt.ylabel("Score")
plt.title("Exams scores by subjects")

plt.grid()
plt.show()
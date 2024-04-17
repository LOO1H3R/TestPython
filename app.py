import matplotlib.pyplot as plt

print("Esta es la app.py")
linear = []
cuadratic = []

for i in range(100):
    linear.append(i)

my_plot = plt.plot(linear)
plt.show()

for i in range(100):
    cuadratic.append(i**2)

my_plot = plt.plot(cuadratic)
plt.show()

print("Fin de la app.py")
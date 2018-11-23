import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

a, b = 5, 3

x = np.linspace(-5.0, 5.0, num=500)
y = (b**2*(1-(x**2)/(a**2)))**.5
# plt.axes(projection='3d')
plt.plot(x, y)
plt.plot(x, -y)
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
sint,cost=1,1
t=10
#teğetlik
def draw_my_curve():
    n=1000
    theta_max=8*np.pi
    theta=np.linspace(0,theta_max,n)
    z=theta
    x=np.sin(theta)
    y=np.cos(theta)

    theta_current=3*np.pi/2
    x_1=np.cos(theta_current)
    y_1=np.sin(theta_current)
    z_1=1

    x_2=np.sin(theta_current)
    y_2=-np.cos(theta_current)
    z_2=theta_current

    x_3 = x_1+x_2
    y_3 = y_1+y_2
    z_3 = z_1+z_2

    x_s=[x_3,x_2]
    y_s=[y_3,y_2]
    z_s=[z_3,z_2]
    ax = plt.axes(projection="3d")

    ax.plot(x, y, z, 'g', lw=2)
    ax.plot(x_s,y_s,z_s,'b',lw=2)


    plt.show()

def draw_b(a,b):
    n = 1000
    theta_max = 8 * np.pi
    theta = np.linspace(0, theta_max, n)
    z = theta
    x = a*np.sin(theta)
    y = b*np.cos(theta)

    theta_current = 3 * np.pi / 2
    x_1 = a*np.sin(theta_current)
    y_1 = b*np.cos(theta_current)
    z_1 = theta_current

    x_2 = a*np.cos(theta_current)
    y_2 = b*-np.sin(theta_current)
    z_2 = 1

    x_3 = x_1 + x_2
    y_3 = y_1 + y_2
    z_3 = z_1 + z_2

    x_s = [x_3, x_1]
    y_s = [y_3, y_1]
    z_s = [z_3, z_1]
    ax = plt.axes(projection="3d")

    ax.plot(x, y, z, 'g', lw=2)
    ax.plot(x_s, y_s, z_s, 'b', lw=2)
    plt.show()

#b) x = a cost y=b sint z=t olarak tanımlanmış eğrinin t=3*pi/2 deki teğer doğrusunu çiziniz
#c) x = 6t y=3tkare z=t olan eğrinin t=10 teğetini çizdiriniz


def draw_c():
    n = 1000
    theta_max = 8 * np.pi
    theta = np.linspace(0, theta_max, n)
    z = theta
    x = 6*theta
    y = 3*theta**2

    theta_current = 3 * np.pi / 2
    x_1 = 6*theta_current
    y_1 = 3*theta_current**2
    z_1 = theta_current

    x_2 = 6
    y_2 = 6*theta_current
    z_2 = 1

    x_3 = x_1 + x_2
    y_3 = y_1 + y_2
    z_3 = z_1 + z_2

    x_s = [x_3, x_1]
    y_s = [y_3, y_1]
    z_s = [z_3, z_1]
    ax = plt.axes(projection="3d")

    ax.plot(x, y, z, 'g', lw=2)
    ax.plot(x_s, y_s, z_s, 'b', lw=2)
    plt.show()
#draw_b(30,90)
#draw_c()

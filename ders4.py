#bir noktanın düzlemde iz düşümü
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
def plane_point(plane,point):
    #draw plane
    #drav two point
    #print distance
    plane_normal=[plane[0],plane[1],plane[2]]
    d=my_product(plane_normal,point)/my_length_func(plane_normal)
    t=-plane[3]-(my_product(plane_normal,point))
    t=t/my_product(plane_normal,plane_normal)

    p_0 = [0,0,0]
    p_0[0] = [point[0] + t * plane[0]]
    p_0[1] = [point[1] + t * plane[1]]
    p_0[2] = [point[2] + t * plane[2]]
    return t,d,p_0

def my_product(a,b): #skaler çarpma
    return a[0] * b[0]+a[1] * b[1]+a[2] * b[2]
def my_length_func(a):
    return my_product(a,a)**.5
a = [1,2,3]
b = [4,2,10]
plane_1 = [1,2,3,-6]
point_1 = [4,2,10]
t, d, p_0 = plane_point(plane_1,point_1)

ax=plt.axes(projection="3d")
ax.scatter(p_0[0],p_0[1],p_0[2],color="green")
ax.scatter(1,2,3)
plt.show()

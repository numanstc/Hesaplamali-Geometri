import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
def draw_my_line(normal_vektor,point_on_line):
    #vektor üzerindeki noktayı bulmak
    a=normal_vektor[0]
    b=normal_vektor[1]
    c=normal_vektor[2]
    x0=point_on_line[0]
    y0=point_on_line[1]
    z0=point_on_line[2]
    x=[]
    y=[]
    z=[]
    for t in range(-1,10):
        x.append(x0+t*a)
        y.append(y0+t*b)
        z.append(z0+t*c)
    return (x,y,z)

# a transpose b nedir?
def my_scalar_product(a,b):
    return a[0]*b[0]+a[1]*b[1]+a[2]*b[2]

#other point labdayız vektor ç1 point on line ç1 üzerinde bir nokta bize en yakın noktayı söylüyor
def point_on_line(normal_vector,point_on_line,other_point):
    a_x = other_point[0] - point_on_line[0]
    a_y = other_point[1] - point_on_line[1]
    a_z = other_point[2] - point_on_line[2]  #otherpoint pointOnLine ikilisi
    b=[a_x,a_y,a_z]
    a=normal_vector

    c=my_scalar_product(a,b)/my_scalar_product(a,a)

    b_x=c*a[0]
    b_y=c*a[1]
    b_z=c*a[2]

    nearest_point_on_line=[b_x,b_y,b_z]
    return nearest_point_on_line
p=(0,0,0) #hattı tanımlayan iki parametre
n=(1,1,1)
other_point=[1,2,7] #bekleme noktası
#ilk uygulama
points=draw_my_line(n,p)
#ax=plt.axes(projection="3d")
#ax.plot3D(points[0],points[1],points[2],color="blue")

#ikincisi
n_p=point_on_line(n,p,other_point) #hat üzerinde ki bize en yakın nokta
ax=plt.axes(projection="3d")
ax.plot3D(points[0],points[1],points[2],color="blue")
ax.scatter(other_point[0],other_point[1],other_point[2],'*')
ax.scatter(n_p[0],n_p[1],n_p[2],'blue')
plt.show()

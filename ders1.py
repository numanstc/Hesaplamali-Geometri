import matplotlib.pyplot as plt

x=[4,0]
y=[0,3]
plt.plot(x,y)

x=[0,4,10]
y=[0,3,3]
plt.xlim(-10,125)
plt.ylim(-10,125)
plt.plot(x,y)

def my_draw_a_vector_from_origin(v):
    x=[0,v[0]]
    y=[0,v[1]]
    plt.xlim(-10,20) #x ve y nin kordinat düzlem gözükecek sınırları veriyor
    plt.ylim(-10,20)
    plt.plot(x,y)

my_draw_a_vector_from_origin([5,67])

def my_draw_a_vector_from_v_to_w(v,w):#vektor uzunlugu
    x=[v[0],w[0]]
    y=[v[1],w[1]]
    plt.xlim(-10,55)
    plt.ylim(-2,55)
    plt.plot(x,y)

my_draw_a_vector_from_v_to_w([5,6],[20,16])

def my_scalar_product(a,b):#vektorel carpım!!!!!!!
    return (a[0]*b[0]+a[1]*b[1])
v = [3,4]
w=[4,7]
my_scalar_product(v,w)

v = [0,4] # birbirine dik olan vektorlerin carpımı sıfır olur
w = [3,0]
my_scalar_product(v,w)

my_draw_a_vector_from_origin(v) # v nin ve w nun goruntuleri
my_draw_a_vector_from_origin(w)

my_draw_a_vector_from_v_to_w([5,5],[10,16])
my_draw_a_vector_from_origin([-7,5]) # öylesine goruntuler aldık

## fonksiyonlar
def distance(v,w):
    return (((v[0]-w[0])**2) + ((v[1]-w[1])**2))**.5
def my_vector_add(v,w):
    return [v[0]+w[0] , v[1] + w[1]]
def my_vector_sub(v,w):
    return [v[0]-w[0] , v[1] - w[1]]
def my_vector_mult_with_scalar(c,v):
    return [c*v[0] , c*v[1]]
a = [3,0]
b =[0,4]
print("toplam : ",my_vector_add(a,b))
print("fark : ",my_vector_sub(a,b))
print("b nin 5 katı :",my_vector_mult_with_scalar(5,b))
print("uzunluk : ",distance(a,b))

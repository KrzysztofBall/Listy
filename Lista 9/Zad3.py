import matplotlib.pyplot
import numpy
import math
g=9.81
v0=input("podaj predkość początkową: ")
a=input("Podaj kąt nachylenia: ")
z=(int(v0)*int(v0)*math.sin(2*(int(a)/180*math.pi)))/g                    
yMax=(int(v0)*int(v0)*math.sin(int(a)/180*math.pi)*math.sin(int(a)/180*math.pi))/(2*g)    
t=(2*int(v0)*math.sin(int(a)/180*math.pi))/g            
print(yMax,z,t)

czas=numpy.linspace(0,t,1000)                             
vx1=(math.cos(int(a)/180*math.pi)*int(v0))
vx=numpy.linspace(vx1,vx1,1000)
vy=(math.sin(int(a)/180*math.pi)*int(v0))-(g*czas)
x=vx*czas
y=(int(v0)*czas*math.sin(int(a)/180*math.pi))-((g*czas**2)/2)

matplotlib.pyplot.subplot(241)                                         
matplotlib.pyplot.plot(czas,vx)
matplotlib.pyplot.title('vx')
matplotlib.pyplot.xlabel("t[s]")
matplotlib.pyplot.ylabel("Vx[m]")
matplotlib.pyplot.subplot(242)
matplotlib.pyplot.plot(czas,vy)
matplotlib.pyplot.title("vy")
matplotlib.pyplot.xlabel("t[s]")
matplotlib.pyplot.ylabel("Vy[m/s]")
matplotlib.pyplot.subplot(243)
matplotlib.pyplot.plot(czas,x)
matplotlib.pyplot.title("xt")
matplotlib.pyplot.xlabel("t[s]")
matplotlib.pyplot.ylabel("x[m]")
matplotlib.pyplot.subplot(244)
matplotlib.pyplot.plot(czas,y)
matplotlib.pyplot.title("xt")
matplotlib.pyplot.xlabel("t[s]")
matplotlib.pyplot.ylabel("y[m]")
matplotlib.pyplot.subplot(245)
matplotlib.pyplot.plot(x,y)
matplotlib.pyplot.title("x")
matplotlib.pyplot.xlabel("x[m]")
matplotlib.pyplot.ylabel("y[m]")
matplotlib.pyplot.show()
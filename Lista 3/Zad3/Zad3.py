import cmath
a=int(input())
b=int(input())
c=int(input())
if a==0:
    print("Pajac")
trojkat=b*b-4*a*c
x1=(-b-cmath.sqrt(trojkat))/(2*a)
x2=(-b+cmath.sqrt(trojkat))/(2*a)
if x1==x2:
    print(x1)
else:
    print(x1,x2)
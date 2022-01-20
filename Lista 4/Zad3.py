import math
a=int(input("0 - stopnie na radiany\n1 - radiany na stopnie\n"))
if a==0:
    x=float(input("podaj:"))
    print(math.radians(x))
else:
    x=float(input("podaj:"))
    print(math.degrees(x))

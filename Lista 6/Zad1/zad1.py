import trojkat
a=int(input("Podaj a:"))
b=int(input("Podaj b:"))
c=int(input("Podaj c:"))
if ((a+b>c) and (a+c>b) and (b+c>a)):
    print("Obwód =",trojkat.obwod(a,b,c))
    print("Pole =",trojkat.pole(a,b,c))
    print("Trójkąt: ",trojkat.boki(a,b,c),trojkat.kąty(a,b,c))
else:
    print("Trójkąt nie spełnia warunku instnienia trójkąta.")
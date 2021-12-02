a=int(input("a:"))
b=int(input("b:"))
while 1>0:
    if b>a:
        x=a
        a=b
        b=x
    if b==0:
        print(a)
        break
    c=a%b
    a=b
    b=c

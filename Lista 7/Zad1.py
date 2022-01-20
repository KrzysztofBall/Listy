def srednifib(n):
    a=int(0)
    b=int(1)
    for i in range(n):
        c=a+b
        a=b
        b=c
    return a
def fibdladebili(n):
    if n==1:
        return 1
    if n==0:
        return 0
    return fibdladebili(n-1)+fibdladebili(n-2)
a=int(input("podaj numer: "))
if a<0:
    print("błąd, nie można liczby <0")
else:
    print(fibdladebili(a))
    print(srednifib(a))


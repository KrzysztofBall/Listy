N=input("Wprowadź N: ")
N=int(N)
a=int(0)
b=int(1)
print(0)
print(1)
for _ in range(N-1):
    print(a+b)
    if a<=b:
        a+=b
    else:
        b+=a
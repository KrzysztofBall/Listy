m=input("Podaj m: ")
n=input("Podaj n: ")
m=int(m)
n=int(n)
for i in range(m):
    a=""
    for c in range(n):
        a+=str((i+1)*(c+1))+","
    print(a)
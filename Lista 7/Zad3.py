def sortowaniedladebili(a):
    q=int(0)
    while q!=len(a)-1:
        q=0
        for i in range(len(a)-1):
            if a[i]>a[i+1]:
                b=a[i]
                a[i]=a[i+1]
                a[i+1]=b
            else:
                q+=1
                print(q)
    return a
a=[1,3,8,5,3,9,2]
print(sortowaniedladebili(a))


wynik=[]
for i in range(100,400):
    if (i%10)%2==0:
        b=i//10
        if (b%10)%2==0:
            c=b//10
            if (c%10)%2==0:
                wynik.append(i)
print(wynik)
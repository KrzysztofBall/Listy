x= [1,3,4,6]
a=input("1 - suma liczb\n2 - iloczyn liczb\n")
a=int(a) #python jak zwykle ma 200 iq i sam się domyśla o co mi chodzi (sarkazm)
if a==1:
    wynik=0
    for i in range(len(x)):
        wynik+=x[i]
    print(wynik)
elif a==2:
    wynik=1
    for i in range(len(x)):
        wynik*=x[i]
    print(wynik)


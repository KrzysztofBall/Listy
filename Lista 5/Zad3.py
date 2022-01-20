liczba=input()
liczba=list(liczba)
def FUNKCJA(liczba):
    wynik=0
    for _ in range(len(liczba)):
        if(liczba[_]=="M"):
            liczba[_]=int(1000)
        elif(liczba[_]=="D"):
            liczba[_]=int(500)
        elif(liczba[_]=="C"):
            liczba[_]=int(100)
        elif(liczba[_]=="L"):
            liczba[_]=int(50)
        elif(liczba[_]=="X"):
            liczba[_]=int(10)
        elif(liczba[_]=="V"):
            liczba[_]=int(5)
        elif(liczba[_]=="I"):
            liczba[_]=int(1)
    for _ in range(len(liczba)-1):
        if liczba[_]<liczba[_+1]:
            wynik-=liczba[_]
        else:
            wynik+=liczba[_]
    wynik+=liczba[len(liczba)-1]
    return wynik
print(FUNKCJA(liczba))

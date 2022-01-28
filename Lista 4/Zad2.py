n=int(input("Podaj rozmiar listy:"))
print("podaj elementy listy:")
a=[]
for n in range(n):
    a.append(input())
def czywystapila(lista,a):
    for i in range(len(lista)):
        if lista[i]==a:
            return 1
    return 0
def funkcja(lista):
    wystopienia=[]
    for i in range(len(lista)-1):
        if czywystapila(wystopienia,lista[i])==0:
            wystopienia.append(lista[i])
        else:
            del(lista[i])
funkcja(a)
print(a)


klucz={"a":"y","e":"i","i":"o","o":"a","y":"e"}
def szyfrowanie(tekst):
    zaszyfrowany=[]
    for i in range(len(tekst)):
       if tekst[i]=="a":
           zaszyfrowany.append(klucz["a"])
       elif tekst[i]=="e":
           zaszyfrowany.append(klucz["e"])
       elif tekst[i]=="i":
           zaszyfrowany.append(klucz["i"])
       elif tekst[i]=="o":
           zaszyfrowany.append(klucz["o"])
       elif tekst[i]=="y":
           zaszyfrowany.append(klucz["y"])
       else:
           zaszyfrowany.append(tekst[i])
    return zaszyfrowany
def deszyfrowanie(tekst):
    tekst=szyfrowanie(tekst)
    tekst=szyfrowanie(tekst)
    tekst=szyfrowanie(tekst)
    tekst=szyfrowanie(tekst)
    return tekst
tekst=input("wprowadź tekst:")
x=int(input("1 - szyfrowanie\n2 - deszyfrowanie\n")) #a ja się znowu zastanawiam co nie działa. Oczywiście 1 oraz 2 to są napisy
if x==1:
    x=szyfrowanie(tekst)
else:
    x=deszyfrowanie(tekst)
for i in range(len(x)):
    print(x[i],sep='',end='')
print("\n")

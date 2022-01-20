import datetime
import os
data = str(datetime.date.today())
while(1>0):
    sciezka = input("podaj ścieżkę pliku do zaszyfrowania: ")
    try:
        plik = open(sciezka, "r")
    except FileNotFoundError:
        print("Błąd. Zła ścieżka")
    except IOError:
        print("Błąd otwarcia pliku!")
    else:
        plik = open(sciezka, "r")
        break
while(1>0):
    klucz = int(input("Podaj klucz. Zakres 1 - 10:"))
    if (klucz > 0 and klucz < 11):
        break
tekst = str(plik.readlines())
def szyfrowanie(tekst, n):
    if n > 26:
        n = n % 26
    if n < -26:
        n = n % (-26)
    zasz = ""
    for i in tekst:
        i = ord(i)
        if (i < 65 or i > 90):
            i = chr(i)
            zasz += i
        else:
            i += n
            if i > 90:
                i = i - 26
            if i < 65:
                i = i + 26
            i = chr(i)
            zasz += i
    return zasz
tekst = tekst.upper()
wynik = szyfrowanie(tekst,klucz)
klucz = str(klucz)
plik.close()
while(1):
    katalog = input("podaj katalog w którym chcesz zapisać ")
    try:
        plik2 = open(katalog + "/" + "plik_zaszyfrowany" + klucz + "_" + data + ".txt","w")
    except FileNotFoundError:
        os.makedirs(katalog)
        plik2 = open(katalog + "/" + "plik_zaszyfrowany" + klucz + "_" + data + ".txt", "w")
        break
    except OSError:
        print("nie można zapisać takiego katalogu ")
    else:
        katalog = input("podaj katalog w którym chcesz zapisać ")
        plik2 = open(katalog + "/" + "plik_zaszyfrowany" + klucz + "_" + data + ".txt", "w")
        break
plik2.write(wynik)
plik2.close()

import os
import datetime
def odszyfrowanie(zasz, n):
    if n > 26:
        n = n % 26
    if n < -26:
        n = n % (-26)
    tekst = ""
    for i in zasz:
        i = ord(i) 
        if (i < 65 or i > 90):
            i = chr(i) 
            tekst += i 
        else:
            i -= n
            if i > 90:
                i = i - 26 
            if i < 65:
                i = i + 26 
            i = chr(i)  
            tekst += i 
    return tekst
while(1>0):
    sciezka = input("podaj ścieżkę do folderu: ")
    try:
        plik1 = ""
        plik = os.listdir(sciezka)
        for i in plik:
            plik1 += i
        n_miejsc = plik1[17]
        plikk = open(sciezka + "/" + plik1,"r")
    except FileNotFoundError:
        print("Nie znaleziono takiej ścieżki podaj inną.")
    except IOError:
        print("nie mogę otworzyć folderu")
    else:
        plik1 = ""
        plik = os.listdir(sciezka)
        for i in plik:
            plik1 += i
        n_miejsc = plik1[17]
        plikk = open(sciezka + "/" + plik1, "r")
        break
zawartosc = plikk.readlines()
zawartosc = str(zawartosc)
wynik = odszyfrowanie(zawartosc,int(n_miejsc))
data = str(datetime.date.today())
try:
    plik2 = open("plik_deszyfrowany" + data + ".txt", "w")
except OSError:
    print("nie można zapisać takiego folderu ")
plik2.write(wynik)
plik2.close()
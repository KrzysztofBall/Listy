import SzyfrCezara
tekst = input("podaj tekst do szyfrowania: ")
n = int(input("podaj klucz (o ile znaków przesunąć?):"))
SzyfrCezara.szyfrowanie(tekst,n)
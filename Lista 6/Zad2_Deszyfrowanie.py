import SzyfrCezara
tekst = input("podaj tekst do deszyfrowania: ")
n = int(input("podaj klucz jakim zaszyfrowano: "))
SzyfrCezara.odszyfrowanie(tekst,n)
rozmiar=int(input("W treści nie ma skąd ma być lista... Podaj ilość znaków:"))
znaki=[]
for _ in range(rozmiar):
    znaki.append(input("Pisz..."))
print("".join(znaki))
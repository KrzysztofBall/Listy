import math
a=int(input())
b=int(input())
c=int(input())
#Chciałbym tu pozdrowić wszystkich fanów Pythona, którzy notorycznie kłamią, że w Pythonie nie trzeba deklarować typów zmiennych, 
#bo mądry Python sam się domyśli. Ta, jasne...
c=math.radians(c)
P=1/2*a*b*math.sin(c)
print(P)

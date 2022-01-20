x=int(input("podaj liczbee:"))
def funkcja(x):
    if(x//1000!=0):
        print("tysiąc",end=" ")
        x=x%1000
    if(x//100==9):
        print("dziewięćset",end=" ")
        x=x%100
    if(x//100==8):
        print("osiemset",end=" ")
        x=x%100
    if(x//100==7):
        print("siedemset",end=" ")
        x=x%100
    if(x//100==6):
        print("sześćset",end=" ")
        x=x%100
    if(x//100==5):
        print("pięćset",end=" ")
        x=x%100
    if(x//100==4):
        print("czterysta",end=" ")
        x=x%100
    if(x//100==3):
        print("trzysta",end=" ")
        x=x%100
    if(x//100==2):
        print("dwieście",end=" ")
        x=x%100
    if(x//100==1):
        print("sto",end=" ")
        x=x%100
    if(x//10==9):
        print("dziewięćdziesiąt",end=" ")
        x=x%10
    if(x//10==8):
        print("osiemdziesiąt",end=" ")
        x=x%10
    if(x//10==7):
        print("siedemdziesiąt",end=" ")
        x=x%10
    if(x//10==6):
        print("sześćdziesiąt",end=" ")
        x=x%10
    if(x//10==5):
        print("pięćdziesiąt",end=" ")
        x=x%10
    if(x//10==4):
        print("czterdzieści",end=" ")
        x=x%10
    if(x//10==3):
        print("trzydzieści",end=" ")
        x=x%10
    if(x//10==2):
        print("dwadzieścia",end=" ")
        x=x%10
    if(x==19):
        print("dziewiętnaście",end=" ")
    if(x==18):
        print("osiemnaście",end=" ")
    if(x==17):
        print("siedemnaście",end=" ")
    if(x==16):
        print("szesnaście",end=" ")
    if(x==15):
        print("piętnaście",end=" ")
    if(x==14):
        print("czternaście",end=" ")
    if(x==13):
        print("trzynaście",end=" ")
    if(x==12):
        print("dwanaście",end=" ")
    if(x==11):
        print("jedenaście",end=" ")
    if(x==10):
        print("dziesięć",end=" ")
    if(x==9):
        print("dziewięć",end=" ")
    if(x==8):
        print("osiem",end=" ")
    if(x==7):
        print("siedem",end=" ")
    if(x==6):
        print("sześć",end=" ")
    if(x==5):
        print("pięć",end=" ")
    if(x==4):
        print("cztery",end=" ")
    if(x==3):
        print("trzy",end=" ")
    if(x==2):
        print("dwa",end=" ")
    if(x==1):
        print("jeden",end=" ")
funkcja(x)


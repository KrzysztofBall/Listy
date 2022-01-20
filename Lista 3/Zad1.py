a=input()
b=0
if a=="a":
    b=1
if a=="ą":
    b=1
if a=="e":
    b=1
if a=="ę":
    b=1
if a=="i":
    b=1
if a=="o":
    b=1
if a=="u":
    b=1
if a=="y":
    b=1
if(b==1):
    print("samogłoska")
else:
    print("spółgłoska")
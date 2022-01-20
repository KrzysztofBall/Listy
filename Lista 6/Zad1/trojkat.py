import math
def obwod(a,b,c):
    ob=a+b+c
    return ob
def pole(a,b,c):
    d=(a+b+c)/2
    p=math.sqrt(d*(d-a)*(d-b)*(d-c))
    return p
def boki(a,b,c):
    if (a==b==c):
        return "równoboczny"
    elif ((a==b) or(a==c) or (b==c)):
        return "równoramienny"
    else:
        return "różnoboczny"
def kąty(a,b,c):
    if ((round(a*a,2)+round(b*b,2)==round(c*c,2))or(round(a*a)+round(c*c)==round(b*b,2))or(round(c*c)+round(b*b)==round(a*a))):
        return "prostokątny"
    elif ((round(a*a,2)+round(b*b,2)<round(c*c,2))or(round(a*a,2)+round(c*c,2)<round(b*b,2))or(round(c*c,2)+round(b*b,2)<round(a*a,2))):
        return "rozwartokątny"
    else:
        return "ostrokątny"
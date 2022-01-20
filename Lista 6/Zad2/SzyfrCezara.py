def szyfrowanie(tekst, n):
    if n > 26:
        n = n%26
    if n < -26:
        n = n%(-26)
    zasz= ""
    for i in tekst:
        i = ord(i)
        if (i < 65 or i > 90):
            i = chr(i)
            zasz+=i
        else:
            i += n
            if i > 90:
                i = i - 26
            if i < 65:
                i = i + 26
            i = chr(i)
            zasz += i 
    print(zasz)
def odszyfrowanie(zasz,n):  
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
    print(tekst)

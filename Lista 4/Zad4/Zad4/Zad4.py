def funkcja(n,a1,q):
    if(n==1):
        return a1
    else:
        return funkcja(n-1,a1,q)*q
x=int(input("Załadować wartości domyślne, czy chcesz wprowadzić własne?\n1 - domyślne\n2 - własne\n"))
if x==1:
    a1=1
    q=2
else:
    a1=int(input("a1:"))
    q=int(input("\nq:"))
n=int(input("\nWprowadź n:"))
print(funkcja(n,a1,q))

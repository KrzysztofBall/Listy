import itertools
n=int(input("podaj długość listy:"))
a=[]
print("Podaj lelmenty listy:")
for i in range(n):
    a.append(input())
print(list(itertools.permutations(a)))

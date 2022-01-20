a=["Kasia","Basia","Marek","Darek"]
a.append("Józek")
b=["Ania","Basia"]
a.extend(b)
a.sort()
print(a[3])
print(a[0],a[1])
print(a[-2],a[-1])
i=a.count("Basia")
for c in range(i):
    a.remove("Basia")
print(len(a))
a=tuple(a)

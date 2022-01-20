a=input()
b=len(a)//2 #a ja się zastanawiam czemu mi nie działa. Oczywiście pod pojedynczy ukośnik musieli dać jakieś upośledzone dzielenie które jest useless
c=a[:b]
d=a[b:]
print(c+input("Wprowadź drugi napis:")+d)

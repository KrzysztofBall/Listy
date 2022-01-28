import itertools
class podlisty:
    def __init__(self,lista):
        self.lista=lista
    def pod(self):
        wynik=[]
        b=list(itertools.combinations(self.lista,3))
        for i in range(len(b)):
            if b[i][0]+b[i][1]+b[i][2]==0:
                wynik.append(b[i])
        return wynik
q=podlisty([1,-1,2,-3,0])
print(q.pod())
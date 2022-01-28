import itertools
class podlisty:
    def __init__(self,lista):
        self.lista=lista
    def pod(self):
        a=[]
        for i in range(len(self.lista)+1):
            a+=list(itertools.combinations(self.lista,i))
        return a
q=podlisty([1,2,3])
print(q.pod())
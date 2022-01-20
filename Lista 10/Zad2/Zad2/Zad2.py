import itertools
class podlisty:
    def __init__(self,lista):
        self.lista=lista
    def pod(self):
        a=combinations(self.lista)
        return a
q=podlisty([1,4,3,8,6,4,6])
print(q.pod())
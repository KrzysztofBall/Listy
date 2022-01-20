import math
class Koło:
    def __init__(self,r):
        self.r=r
    def pole(self):
        return self.r*self.r*math.pi
    def obwód(self):
        return 2*math.pi*self.r
a=Koło(5)
print(a.pole(),a.obwód())

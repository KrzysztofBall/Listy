import numpy
dzialania = numpy.array([[1,2,3,-2,-1],[3,5,5,-3,-9],[2,3,2,0,-8],
[2,6,7,-5,1],[1,2,6,-4,-10]])
wyniki = numpy.array([6,2,-5,17,12])
rozwiazania = numpy.linalg.solve(dzialania,wyniki)
print("X = ",rozwiazania[0])
print("y = ",rozwiazania[1])
print("Z = ",rozwiazania[2])
print("T = ",rozwiazania[3])
print("U = ",rozwiazania[4])

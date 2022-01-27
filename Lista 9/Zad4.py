import matplotlib.pyplot
jezyk=['Python','C','Java','C++','C#','Visual Basic','JavaScript','Asembler','SQL','Swift']
#SQL nie jest językiem programowania, ale widnieje w rankingu, więc i tu go umieszczam
popularnosc=[13.58,12.44,10.66,8.29,5.68,4.74,2.09,1.85,1.8,1.41]
matplotlib.pyplot.figure(figsize=(15,4))
matplotlib.pyplot.bar(jezyk,popularnosc)     
matplotlib.pyplot.title("10 Najpopularniejszych języków programowania")
matplotlib.pyplot.ylabel("Ocena(%)")
matplotlib.pyplot.show()
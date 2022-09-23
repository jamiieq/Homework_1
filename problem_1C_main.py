from queue import Queue
from threading import Thread

N = 6 
item = 3

def Reader(iq,qA,qC):
    while (True):
        In = iq.get("data")
        print( "Reader get iq:", In)
      
        d = [0,1, 2, 3, 4, 5]  
        for i in range(N):
          qA.put(d[i])
          print("Reader put qA")
        p = In          
        qC.put(p)
        print("Reader put qC")

def Conv(qA,qB):     
    while (True):
        x = qA.get()
        print("Conv get qA:", x)
        r1 = x
        qB.put(r1)
        print("Conv put qB")
        r2 = x + 1
        qB.put(r2)
        print("Conv put qB")
        
def Merge(qB,oq,qC):   
  while True:
    x = qC.get()
    print("Merge get qC: ", x)
    d = [0,0,0,0,0,0,0,0,0,0,0,0]  # modify
    for i in range(2*N):
      d[i] = qB.get()
      print("Merge get qB:", d[i])
    t = x
    oq.put(t)
    print("Merge put oq")


iq = Queue(1)
iq.put(item)
qA= Queue(maxsize=1)
qB= Queue(maxsize=2)
qC= Queue(maxsize=1)
oq = Queue()

t1 = Thread(target=Reader, args=(iq,qA,qC))
t2 = Thread(target=Conv, args=(qA,qB))
t3 = Thread(target=Merge, args=(qB,oq,qC))
t1.start()
t2.start()
t3.start()
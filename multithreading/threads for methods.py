from threading import Thread

class Easy:
    def display(self,n):
   
        for i in range(n):
            print("VADC")
e1=Easy()
t1=Thread(target=e1.display,args=(5,))
t1.start()
for i in range(5):
    print("hi")
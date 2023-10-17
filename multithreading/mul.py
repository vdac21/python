"""import threading
 
 
def print_cube(num):
    # function to print cube of given num
    print("Cube: {}" .format(num * num * num))
 
 
def print_square(num):
    # function to print square of given num
    print("Square: {}" .format(num * num))
 
 
if __name__ =="_main_":
    # creating thread
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))
 
    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()
 
    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()
 
    # both threads completely executed
    print("Done!")

word='Amazon access UaE'
x= ['a','e','i','o','u','A','E','I','O','U']
for i in x:
    if i in word:
      print(i)

x=[10,20,30,30,40,50,60,30,40,10,60,60]
dup=[]
for i in x:
    n=x.count(i)
    if n>1:
        if dup.count(i)==0:
            dup.append(i)
print(dup)
"""
x=[10,20,4,5,15,25,30]
sum=0
for i in x:
    if i%5 == 0:
        sum=sum+i
print(sum)

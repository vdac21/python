#import thread class
from threading import Thread
#creating a function contaning code to be executed parallaly
def display():
    for i in range(5):
        print("HI VDAC STUDENTS")
#create new thread class
t1=Thread(target=display)



#there are two ways of creating threads:-
"""
using thread class present in threading module
by extending ,thread class
Steps:
step1: import Thread class from Threading Module
step2: Create a function containing code to be executed parallaly
step3:Create an object of thread class
step4:Start created thread using start() method"""

from threading import Thread,current_thread
def display():
    print("t1 thread details:",current_thread())
    for i in range(4):
        print("VADC")
t1=Thread(target=display)
t1.start()


for i in range(6):
    print("hi")
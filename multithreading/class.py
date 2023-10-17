import threading 
import time

def calc_square(numbers):
    print('square_number: ')
    for number in numbers:
        time.sleep(0.2)
        print('square: ',number*number)
"""
def calc_cube(numbers):
    print('cube_number: ')
    for number in numbers:
        time.sleep(0.2)
        print('cube: ',number*number*number)
"""

initial_time=time.time()
x=[1,2,3,4]
t1=threading.Thread(target=calc_square,args=(1,))
#t2=threading.Thread(target=calc_cube,args=(1,))

t1.start()
#t2.start()

t1.join()
#t2.join()
print('Time taken: ',time.time()-initial_time)

        

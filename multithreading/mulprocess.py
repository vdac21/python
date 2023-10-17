import multiprocess

def print_cube(num):
    print(f"Cube = {num*num*num}")

def print_square(num):
    print(f"Cube = {num*num}")

if __name__=="__main__":

    p1=multiprocess.Process(target=print_square,args=(10,))
    p2=multiprocess.Process(target=print_cube,args=(10,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Done")

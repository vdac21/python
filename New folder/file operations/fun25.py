# Running python program from the command prompt
# Taking command line args


import sys


def add(x, y):
    return x+y


args = sys.argv[1:]

if len(args) != 2:
    # exit the program
    print("invaild command line args. USAGE : python <program.py> <args1> <args2>")
    sys.exit(0)

a = int(args[0])
b = int(args[1])
print(f"the args: {a}, {b}")

r = add(a, b)
print(f"the sum of a={a} and b={b} is {r}")

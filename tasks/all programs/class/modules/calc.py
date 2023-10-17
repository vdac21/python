# WAP implement basic caluculator application for two numbers
import sys

def add(x, y):
    c = x+y
    return c

def sub(x, y):
    c = abs(x-y)
    return c

def mul(x, y):
    c = x*y
    return c

def div(x, y):
    try:
        c = x//y
        return c
    except:
        print("In valid inputs")

args = sys.argv[1:]
if len(args) != 3:
    print("Invalid command line options:")
    print("USAGE:  python <program.py> <op> <arg1> <arg2>")
    print("Example :  python calc.py -a 10 20")
    print("Options values :\n  -a  ADD\n -s SUB\n -m MUL\n -d DIV")
    sys.exit(0)

op = args[0]
a = int(args[1])
b = int(args[2])
if op == '-a':
    print(add(a, b))
elif op == '-s':
    print(sub(a, b))
elif op == '-m':
    print(mul(a, b))
elif op == '-d':
    print(div(a, b))


"""
a = int(input("Enter 1st value : "))
b = int(input("Enter 2nd value: "))
op = input("Enter choise: ")
if op == '1':
    print(add(a, b))
elif op == '2':
    print(sub(a, b))
elif op == '3':
    print(mul(a, b))
elif op == '4':
    print(div(a, b))
"""






    




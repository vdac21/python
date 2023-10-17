# Python program to demonstrate
# command line arguments

import sys

# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)

# Arguments passed
print("\nName of Python script:", sys.argv[0])

print("\nArguments passed:", end = " ")
for i in range(1, n):
	print(sys.argv[i], end = " ")
	
# Addition of numbers
Sum = 0

for i in range(1, n):
	Sum += int(sys.argv[i])
	
print("\n\nResult:", Sum)

'''
import sys
  
  
print(sys.path)


import sys
  
a = 'Geeks'
  
print(sys.getrefcount(a))

import sys

print("You entered: ",sys.argv[1], sys.argv[2], sys.argv[3])
'''

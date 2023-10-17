"""
Write a program take two input strings of equal lengths and display the output with by representing same index value

Example:  #input1:  MOTHER
                 #input2:  PYTHON
#output:  [ [M, P], [O, Y], [T, T], [H, H], [E, O], [R, N]]

"""

# Solution-1
s1 = input("Enter 1st string :  ") # MOT
s2 = input("Enter 2nd string :  ") # PYT
output = []
if len(s1) == len(s2):
    for i in range(len(s1)):
        t = []
        t.append(s1[i])
        t.append(s2[i])
        output.append(t)
    print(output)
else:
    print("In valid inputs")
    

# Solution-2
s1 = input("Enter 1st string :  ") # MOTHER
s2 = input("Enter 2nd string :  ") # PYTHON
output = []
if len(s1) == len(s2):
    for i in range(len(s1)):
        output.append([s1[i], s2[i]])
    print(output)
else:
    print("In valid inputs")
    

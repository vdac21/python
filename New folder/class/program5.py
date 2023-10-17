"""
 Take two input strings , if two input string lengths
 are even length or odd length then combine first string and second
 string with the word SAME ,
 otherwise you can combine both the strings with the word DIFFERENT. 
"""

s1 = input("Enter 1st string : ")#"VDAC"
s2 = input("Enter 2nd string: ")# "CDAC"

n1 = len(s1)
n2 = len(s2)

# checking both lengthes are even or not
if n1 % 2 == 0 and n2 % 2 == 0:
    s = s1 + "-SAME:EVEN-" + s2
    print(s)
# checking both lengthes are odd or not  
elif n1 % 2 == 1 and n2 % 2 == 1:
    s = s1 + "-SAME:ODD-" + s2
    print(s)
else:
    s = s1 + "-DIFFERENT-" + s2
    print(s)
    



'''take two input strings,if two input string lengths are even length or odd length then
combine first string and second string with the word SAME, otherwise you can combine both the strings
with the word diffrent.'''

s1=input("Enter the 1st string: ")
s2=input("Enter the 2nd string: ")

n1=len(s1)
n2=len(s2)

#cecking both lengths are even or not
if n1%2==0 and n2%2==0:
    s=s1+"-SAME:EVEN-" +s2
    print(s)
#checking the both lengths are odd or not

elif n1%2==1 and n2%2==1:
    s=s1+"-SAME:ODD-"+s2
    print(s)

else:
    s=s1+"-DIFFERENT-"+s2
    print(s)

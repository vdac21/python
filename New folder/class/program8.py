"""
Write a program that takes string input from the user and filters out all the consonants from the strings and print all
respective ascii values in a list format. 
"""


s = "python is powerful language"

vowles = "aeiou"
output = []
for ch in s:
    if ch != ' ' and ch not in vowles:
        output.append(ord(ch))
print(output)



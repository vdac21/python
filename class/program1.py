"""
 Your program should take input as a string and display the total number
 vowels from the given string.
 Assume the input contains the lower case letters. 
"""

# Solution1
word = input("Enter a word: ")
counter = 0

for ch in word:
    if ch == 'a' or ch == 'e' or ch == 'i' or\
       ch == 'o' or ch == 'u':
        counter = counter + 1
print(f"Total number of vowels : {counter} from the given word: {word}")



# Solution2
word = input("Enter a word: ")
counter = 0
vowels = ('a', 'e', 'i', 'o', 'u')
for ch in word:
    if ch in vowels:
        counter = counter + 1
print(f"Total number of vowels : {counter} from the given word: {word}")





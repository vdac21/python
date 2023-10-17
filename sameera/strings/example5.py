#count total number of vowels

word=input("enter a word: ")
counter=0
for ch in word:
    if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
        counter=counter+1
print(f"Total number of vowels:{counter} from the given word:{word}")

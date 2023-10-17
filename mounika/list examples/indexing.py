x=["python","java","cpp","go"]
y=""
for word in x:
    print(word[0])
    y=y+word[0]
print(f"output:{y}")

#note: if any case we need to display string as an output
#we need to define empty string as a place holder to store the output

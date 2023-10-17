#X = ["PYTHON”, “JAVA”, “CPP”, “GO”]
#output :“PJCG”


x = ["PYTHON","JAVA","CPP","GO"] 
y = ""
print(f"Input: {x}")
for word in x:
    print(word[0])
    y = y+word[0]
print(f"Output: {y}")

# Note: If any case , we need to display string as an output
# we need to define empty string as a place holder to store the output

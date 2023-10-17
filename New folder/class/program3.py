"""
Combine all the characters from the given sentence which the respective indices are divisible by 5 and ignore the space in output.

Example : #input : Winners are not those who never fail but those who never quit
                #output:  Wreerlert
"""


sentence = "Winners are not those who never fail but those who never quit"
resp = ""

for i in range(0, len(sentence)):
    if i % 5 == 0:
        if sentence[i] != ' ':
            resp = resp + sentence[i]
print(resp)

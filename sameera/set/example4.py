#Update the first set with items that don't exist in the second set

s1={10,20,30,40,50}
s2={30,40,50,60,70}

s2.difference_update(s1)
print(s2)

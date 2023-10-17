#update the first set with items that don't exist in the second set



s1={10,20,30}
s2={20,40,50}


s1.difference_update(s2)
print(s1)

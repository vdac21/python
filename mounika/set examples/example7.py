#Remove items from set1 that are not common to both s1 and s2


s1={10,20,30,40,50,60}
s2={30,40,50,60,70}

s1.intersection_update(s2)
print(s1)

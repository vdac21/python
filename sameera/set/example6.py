#check if two sets have any elements in common if yes,display the common elements

s1={10,20,30}
s2={30,40,50,60,70}

if s1.isdisjoint(s2):
    print("two sets have no common items")
else:
    print("two sets have common items")
    print(s1.intersection(s2))

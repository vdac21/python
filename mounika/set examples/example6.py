#check if two sets have any elements in common.if yes,display the common elements


s1={10,20,30,40,50}
s2={60,70}


if s1.isdisjoint(s2):
    print("two sets have no items in common")

else:
    print("Two sets have items in common")
    print(s1.intersection(s2))



# Input List 
x=[450,540,1256,2506,15342,32424,20018,56300]

y=[]  # Place holder to store all the
      # numbers which are dibisible by 4
total=0  # Place holder to add all numbers from y
for e in x:
    if e%4==0:
        y.append(e)
        total=total+e

print(f"Given input : {x}")
print(f"Elements which are divisible by 4 : {y}")       
print(f"Sum of elements which are divisible by 4:{total}")

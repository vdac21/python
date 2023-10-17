

# Solution-1
x=[450,540,1256,2506,15342,32424,20018,56300]
y=[] # elements which are divisible by 4
z = [] # indexes for the elements which are divisible by 4
# To traverse the indexs we can use range() function
for i in range(0,len(x)):
    if x[i]%4==0:
        y.append(x[i])
        z.append(i)
        
print(f"Given input : {x}")
print(f"Elements which are divisible by 4 : {y}")       
print(f"Indexs for the elemets which are divisible by 4:{z}")


# Solution-2
x=[450,540,1256,2506,15342,32424,20018,56300]
d = {} 
# To traverse the indexs we can use range() function
for i in range(0,len(x)):
    if x[i]%4==0:
        d[i] = x[i]    
print(f"Given input : {x}")      
print(f"Indexs for the elemets which are divisible by 4:{d}")

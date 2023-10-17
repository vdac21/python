minimum = int(input("Enter the min : "))
maximum = int(input("Enter the max : "))
for n in range(minimum,maximum + 1):
 if n > 1:
    for i in range(2,n):
        if (n % i) == 0:
           break
    else:
      print(n)

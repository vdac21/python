"""
Write a program row and column size from the user  and construct 2 dimensional array  and  take all elements from the user 
Example :    row → 2   column → 2
#output :   [[10, 40], [60, 90]]

"""

row_size = int(input("Enter row size: "))
col_size = int(input("Enter col size: "))
matrix = []
for i in range(0, row_size):
    row = []
    for j in range(0, col_size):
        #print(i, j)
        s = input(f"Enter ({i} {j})th value: ")
        row.append(s)
    print(f"ROW {i} : {row}")
    matrix.append(row)
    
print(matrix)

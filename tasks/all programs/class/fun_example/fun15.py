# We can return multiple vaues from the function
"""
For example , if the function is returning two values
we need collect in two variables
"""

def get_total(st_marks):
    s = 0
    for e in st_marks:
        s = s+ e
    return s, s/len(st_marks)




marks = [64, 87, 68, 97, 68, 39]

print(f"Studnet Subject Marks {marks}")

# call function to get total
total, avg = get_total(marks)
print(f"Total Marks: {total}/{len(marks)*100}")

print(f"Avg : {avg}")

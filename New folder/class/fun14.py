# We can return multiple vaues from the function


def get_total(st_marks):
    s = 0
    for e in st_marks:
        s = s+ e
    return s




marks = [64, 87, 68, 97, 68, 39]

print(f"Studnet Subject Marks {marks}")

# call function to get total
total = get_total(marks)
print(f"Total Marks: {total}/{len(marks)*100}")

avg = total/len(marks)

print(f"Avg Score {avg} % ")

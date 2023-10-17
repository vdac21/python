def get_total(st_marks):
    s = 0
    for e in st_marks:
        s = s+ e
    return s, s/len(st_marks)




marks = [64, 87, 68, 97, 68, 39]

print(f"Studnet Subject Marks {marks}")

# call function to get total
output  = get_total(marks)

#print(type(output), output)
print(f"Total Marks: {output[0]}/{len(marks)*100}")

print(f"Avg : {output[1]}")





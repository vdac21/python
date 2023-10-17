# we can return multiple values from the function



def get_total(st_marks):
    s = 0
    for e in st_marks:
        s = s+e
        return s

marks = [64, 87, 68, 97, 68, 39]

print(f"student subject marks {marks}")


# call function to get total
total = get_total(marks)
print(f"total marks: {total}/{len(marks)*100}")

avg = total/len(marks)

print(f"avg score {avg}")

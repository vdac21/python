def get_total(st_marks):
    s = 0
    for e in st_marks:
        s = s+e
        return s,s/len(st_marks)

marks = [64, 87, 68, 97, 68, 39]

print(f"student subject marks {marks}")


output = get_total (marks)


-

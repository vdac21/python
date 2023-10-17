def get_total(st_marks):
    s=0
    for e in st_marks:
        s=s+e
    return s
marks=[56,87,97,80,68,70]
print(marks)
total=get_total(marks)
print(f"{total}/{len(marks*100)}")
avg=total/len(marks)

print(f"avg score{avg}%")

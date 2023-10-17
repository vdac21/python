x = [("A", 65), ("B", 66), ("C", 67), ("D", 68)]

print(f"Input: {x}")
d = {}
for item in x:
    k = item[0]
    v = item[1]
    d[k] = v
print(f"Output: {d}")

# "By using built-in function"
print(dict(x))

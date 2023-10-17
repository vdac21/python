#sort a tuple of tuples by 2nd item
sample = [('Jack', 76), ('Beneth', 78), ('Cirus', 77), ('Faiz', 79)]
sample.sort(key=lambda a: a[2])
print(sample)

"""
# Given an array of integers greater than zero, find if there is a way to
# split the array in two (without reordering any elements) such that the
# numbers before the split add up to the numbers after the split. If so,
# print the two resulting arrays.
# [5, 2, 3] ==> [5], [2, 3] ==> True
# [5, 1, 2, 3] ==> False
# [1, 4, 2, 3] ==> [1, 4] , [2, 3] ==> True
# [1, 1, 3, 2, 3] ==> [1, 1, 3], [2, 3] ==> True
# [1, 1, 3, 1, 1, 3] ==> [1, 1, 3], [1, 1, 3] ==> True
"""


def split_array(x):
    if len(x) <=2:
        return False
    y = []
    for i in range(0, len(x)):
        y.append(x[i])
        if sum(y)== sum(x[i+1:]):
            #print(y, x[i+1:])
            return True
            break
    else:
        return False
        
        

# [5, 2, 3] ==> [5], [2, 3] ==> True
print(split_array([4, 1, 1, 5]))
"""
print(split_array([5, 2, 3]))
print(split_array([5, 1, 2, 3]))
print(split_array([1, 4, 2, 3]))
print(split_array([1, 1, 3, 2, 3]))
print(split_array([1, 1, 3, 1, 1, 3]))
"""

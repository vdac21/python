#WAF find area of circle
#formula:pi*r*r


def area(r):
    pi=3.147
    a=pi*r*r
    return a


rad=10
a1=area(rad)
print(a1)


# function definition
def get_square(num):
    return num * num

for i in [1,2,3,4,5]:
    # function call
    result = get_square(i)
    print('Square of',i, '=',result)

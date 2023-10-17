"""
def add(x,y):
    c=x+y
    print(c)


add(10,20)

#WAF to sum two values 100 multiply


def add(x,y):
    c=x+y
    
    r=c*100
    print(r)

add(10,20)
print(c*100)

def myupper(word):
    word_upper=" "
    for ch in word:
        if ch>='a' and ch<='z':
            ch=chr(ord(ch)-32)
        word_upper=word_upper+ch
    return word_upper
s="ongole"
s=myupper(s)
print(s)

def myreverse(x_list):
    y= []
    for i in range(len(x_list)-1,-1-1):
        y.append(x_list[i])
    return y


x=[10,20,30,40]
print(f"Input list: {x}")
s=myreverse(x)
print(f"Reversed list: {s}")
        

def myreverse(x_list):
    y = []
    for i in range(len(x_list)-1, -1, -1):
        y.append(x_list[i])
    return y
        

x = [10, 20, 30, 40]
print(f"Input list: {x}")
s = myreverse(x)
print(f"Reversed list: {s}")
"""

#WAF find the area of circle
def area(r):
    pi=3.147
    a=pi*r*r
    return a

rad=11
a1=area(rad)
print(a1)

#WAF find the area of reactangle
def rect_area(l,b):
    a=l*b
    return a
ar=rect_area(10,20)
print(ar)



"""
syntax:
    try:
        #some code
    except:
        #Executed if error  in line
        #try block
    else:
        #execute if no exception
    finally:
        #some code....(always executed)



try:
    k=5//0
    print(k)
except ZeroDivisionError:
    print("can't divide by zero")
finally:
    print("this is failed")
"""



try:
    num=int(input("enter a number: "))
    assert num % 2 ==0
except:
    print("Not an even number!")
else:
    reciprocal=1/num
    print(" reciprocal ")
finally:
     print("this is failed")

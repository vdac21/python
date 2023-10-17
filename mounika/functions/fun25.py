def myFun(arg1,**kwargs):
    print("first arg: ",arg1)
    for key,value in kwargs.items():
        print("%s==%s",(key,value))
myFun('hi',first='great',mid='value',last='things')

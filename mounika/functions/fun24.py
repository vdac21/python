def myFun(**kwargs):
    for key,value in kwargs.items():
        print("%s==%s",(key,value))
myFun(first='great',mid='value',last='things')

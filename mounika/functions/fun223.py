def myFun(arg1,*argv):
    print("first argument: ",arg1)
    for arg in argv:
        print("next argument: ",arg)
myFun("hello","hi","welcome","my","home")
                

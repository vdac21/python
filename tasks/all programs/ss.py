def outer_fun():
    x=10
    y=20
    w=30
    def inner_fun():
        m=300
        n=400
        print(x,y,m,n)
    return inner_fun()

ifun = outer_fun()
ifun()


    
    

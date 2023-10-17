def print_args(*args):
    for arg in args:
        print(arg)
print_args('computer','laptop','tv','machine')
        
def print_kwargs(**kwargs):
    for kwarg in kwargs:
        print(kwarg)
print_kwargs(name:"kelly",age:28,village:"maddulur")

#decarators in python


def login_required(f1):
    def inner(name,is_login):
        if is_login==False:
            print('kindly login')
            return
        return f1(name,is_login)
    return inner

@login_required
def home(name,is_login):
    print("welcome home page")
@login_required
def orders(name,is_login):
    print("welcome orders page")

def about():
    print("welcome about page")

home('user',True)
orders('user',True)
about()

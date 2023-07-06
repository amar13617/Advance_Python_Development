#def f1():
#    print("Hello Amar")
    
#def f2(func):
#    return func()
    
#(f2(f1))

#def div(a,b):
#    print(a/b)
    
#def new_div(func):
    
#    def inner(a,b): # to change and update for old func.
#        if a < b:
#            a,b = b,a
#        return func(a,b)
    
#    return inner

#div1 = new_div(div)    
#div1(2,4)

#def welcome_user(func):
#    print("Welcome to my application!")
#    func()

#def say_hello():
#    user_name = input("Enter your name: ")
#    print(f"Hello, {user_name}!")

#welcome_user(say_hello) 

user = {'username': 'jose123', 'access_level': 'admin'}

def user_has_permission(func):
    def secure_func():
        if user.get('access_level') == 'admin':
            return func()
    return secure_func
    
def my_function():
    return 'Password for admin panel is 1234.'

my_secure_function = user_has_permission(my_function)

print(my_secure_function())
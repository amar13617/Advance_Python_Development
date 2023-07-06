import functools

user = {'username': 'jose123', 'access_level': 'guest'}

def user_has_permission(func):
    @functools.wraps(func)
    def secure_func(panel):
        if user.get('access_level') == 'admin':
            return func(panel)
    return secure_func

@ user_has_permission    
def my_function(panel):
    return f'Password for {panel} admin panel is 1234.'

@ user_has_permission
def another_func():
    pass

#print(my_function())
print(my_function.__name__)
#print(another_func.__name__)

#my_function = user_has_permission(my_function)
print(my_function('movies'))
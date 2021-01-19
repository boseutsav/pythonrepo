def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('wrapper executed this before {}'.format(original_function.__name__))
        original_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def display(name, age):
    print('Display Function Ran with {} and {}'.format(name,age))

# decorated_display = decorator_function(display)
# decorated_display()
display('john', 25)

class decorator_class(object):
    def __init__(self,original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('call method executed this before {}'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)

@decorator_class
def display2(name, age):
    print('Display2 Function Ran with {} and {}'.format(name,age))

display2('Kitty', 34)
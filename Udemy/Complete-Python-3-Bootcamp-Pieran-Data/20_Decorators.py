def hello():

    return 'Hi! My name is Gbenga'

greet = hello

print(greet())

print()


def hello():

    print('This is an Hello Function')

    def welcome():

        return '\t This is welcome() inside Hello'

    print('I am going to return a Function')

    return welcome

my_new_func = hello()

print(my_new_func())

print()


def new_decorator(original_func):

    def wrap_func():

        print('Some code, before the original function!')

        original_func()

        print('Some code, after the original function!')

    return wrap_func

@new_decorator
def func_needs_decorator():

    print("I want to be decorated!")

func_needs_decorator()

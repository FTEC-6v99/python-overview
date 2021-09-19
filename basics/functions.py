'''
Functions
'''
# a function is a block of code that is executed only when it's called
# you can create a new function using the def keyword


def function_example():
    print('This is an example of a function')


# to call a function refer to the function with its name followed by two parantheses
function_example()

# functions can receive parameters


def greet(first_name, last_name):  # fist_name and last_name are called function parameters
  # parameters can be referenced inside of the function code block
    print(f'Hello {first_name} {last_name}')


# arguments can be passed to functions when the functions are called
# in this case first_name variable will be assigned the value John and last_name variable will be assigned the value Doe
greet('John', 'Doe')

'''
Default arguments: a function can receive default values in case arguments where not provided when the
function is called
'''


def greet_with_defaults(first_name='John', last_name='Doe'):
    print(f'Hello {first_name} {last_name}')


# since no arguments where provided the function will use the default values John and Doe
greet_with_defaults()
# since arguments where provided, the function will override the default values
greet_with_defaults('James', 'Smith')

# Note: it is not allowed to define a positional argument after a default argument:
# def invalid_func_definition(fistname = 'John', lastname) <- not allowed

'''
Keyword arguments: arguments can be provided to a function out of order if they are directly refered to by their names
'''


def func(arg1, arg2, arg3):
    print(f'{arg1} {arg2} {arg3}')


# if arguments weren't provided using the parameter name, then the interpreter will match the
# position of the argument with the parameter
func(1, 2, 3)  # in this case arg1=1, arg2 = 2, and arg3 = 3 (because of the order)
# since the parameters were assigned using their names, the order doesn't matter
func(arg2=1, arg1=3, arg3=1)

'''
Arbitrary number of arguments: to send an arbitrary number of arguments use the * operator 
'''


# the convention is to use 'args' but it could be any other name (e.g., *x)
def func_with_arb_args(*args):
    for arg in args:  # args are passed to the function as a tuple
        print(arg)


func_with_arb_args(1, 2, 3, 4)
func_with_arb_args(1, 2, 3)

'''
Arbitrary number of keyword arguments: similar to *args, we can send an arbitrary number 
of keyword arguments using the ** operator
'''


# the convention is to use kwargs but it could be any other name e.g., **x
def func_with_arb_keyword_args(**kwargs):
    for k, v in kwargs:
        print(f'{k}, {v}')


func_with_arb_keyword_args(arg1=2, arg3=1, arg2=4)
func_with_arb_keyword_args(firstname='John', lastname='Doe', id=19274)

'''
A function can either return a value or nothing
a function that returns nothing (i.e., doesn't have a return keyword) actually returns None
None is a Python data type that is used to represent the absence of anything
to return a value in a function, use the return keyword
'''


def sum(a, b):
    return a + b  # this simple func takes two args and return their sum


def greet_with_no_return(first_name, last_name):
    # this argument doesn't return anything (no return keyword)
    print(f'Hello {first_name} {last_name}')

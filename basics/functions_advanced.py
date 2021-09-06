'''
Everything in Python is an object including functions. That means functions can:
1. assigned to variabled
2. be passed as arguments to other functions
3. be returned by other functions 
'''


def sum(a, b):
    return a + b


sum_func = sum  # functions can be assigned to variables
type(sum_func)  # this will return <class function>
sum_func()  # this will call the sum function since sum_func variable has the sum func as a value

'''
Function can be passed as arguments
'''


def execute(func):  # this function simply takes in a function as an argument and calls it
    func()


def simple_func():
    print('Hello world!')


# here the simple_func is passed as a parameter argument to execute function
execute(simple_func)

'''
Functions can be returned by other functions
'''


def get_printer():
    def print(message):
        print(message)
    return print


# since get_printer returns a function, the printer variable is a function
printer = get_printer()
type(printer)  # this will return <class function>
# since printer is a function, it can be called like any other function
printer('Hello world')

# a short hand to do the same is:
# this saves the step of assigned the returned function from get_printer to a variable and then calling that variable
get_printer()('Hello world')

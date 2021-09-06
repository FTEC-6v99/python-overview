'''
Handling Exceptions
'''
# Python program will termiante if it encounters an exception
# that it doesn't know how to handle.
# consider this example:


def bad_divide(a, b):
    return a / b  # this line will throw an exception if b = 0


# calling the bad_divide function with b = 0 will throw an exception
bad_divide(1/0)

# instead of allowing the program to terminate, we can handle the exception as follows


def divide(a, b):
    try:
        return a / b
    except:
        print('Oops an exception has been thrown! Can not complete the divide')


# This call will not cause the program to termiante, the error will be caught in the try block
# execution will then move to the except block where the print statement runs
divide(1 / 0)

####
# Multiple except
# a try block can have multiple except blocks for specific exceptions
####


def divide2(a, b):
    try:
        return a / b
    except ZeroDivisionError:  # this block will run only when the exception thrown is ZeroDivisionException
        print('Oops zero divisors are not allowed! Try again')
    # this block will run for all other exception (this is a catch-all exception block)
    except:
        print('An unknown exception has was thrown')

####
# The else block:
# You can add an else block with a try/except.
# Code in the else block will run if an exception is not thrown
####


def divide3(a, b):
    answer = None
    try:
        answer = a / b
    except:
        print('Oops! an exception is thrown')
    else:  # this code block will run only if there is no exception thrown in the try block
        return answer

####
# The finally block:
# you can add a finally block with a try/except:
# the finally block always runs whether an exception is thrown or not
####


def divide4(a, b):
    try:
        return a/b
    except:
        print('Oops! an error was thrown')
    finally:  # this code will always run whether an exception is thrown or not
        print('Thank you for using the divide function')

####
# Raising a custom exception:
# you can also raise a custom exception using the raise keyword
####


def divide5(a, b):
    try:
        if b == 0:
            # use the raise keyword to throw exceptions
            raise Exception('Zero is not allowed as a divisor')
        return a / b
    except:
        print('Oops an expcetion has been thrown')

####
# Reading an exception message:
# every exception object contians a message that explains the exception
# it is often helpful to print the exception message to the console for better
# troubleshooting
####


def divide6(a, b):
    try:
        return a / b
    except Exception as e:  # this assigns the exception object to a variable called e
        # str(e) converts the exception object to a string
        print(f'Oops! An exception is thrown. Error message: {str(e)}')

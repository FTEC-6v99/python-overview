"""
A function decorator is a design pattern that allows the ability to add
functionality to an existing function.


As an example assume we have a protected function (a function that only a limited
group of users can call), before the function is executed we should check whether
the caller is authorized to call the function or not. Let's also assume that the caller
is expected to send their username as the first argument when they call the function.
For this purpose we will create an Authorize decorator that, before calling the funtion,
checks on whether the caller is authorized or not.
"""
# list of usernames authorized to call the protected functions
authorized_users = ['akj2635', 'fab0623', 'mmi0410', 'akb0602']


def authorize(func):
    """
    This decorator takes in a function and checks whether the caller is authorized to execute the function.
    For the sake of this example, we are assuming that the caller passes their username as first positional argument
    """
    def wrapper(*args):  # the wrapper function calls the decorated function if the caller is authorized
        username = args[0]
        if username in authorized_users:
            func(*args)
        else:
            raise Exception('User not authorized to execute this function')
    return wrapper


@authorize  # adding this decorator to the greet function will cause the interpreter to check on whether the user is authorized to call the function
def greet(username, first_name, last_name):
    print(f'Hello {first_name} {last_name}')


# this will print Hello John Doe, since fab0623 is an authorized user
greet('fab0623', 'John', 'Doe')
# this will throw an Exception since invalid_user is not an authorized user
greet('invalid_user', 'Jane', 'Doe')

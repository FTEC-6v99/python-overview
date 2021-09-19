'''
Variables and Data types
'''
# a variable is a container that stores data
# variables have names and values
# to declare a variable use the = operator.
# Example:
name = 'John Doe'
id = 83746  # in this example id is the name of the variable and 83746 is the value
weight = 175.12
is_active = False

# variable names must start with a letter or an underscore
_name = 'John Doe'  # valid variable name

# multiple variables can be assigned at once
x, y, z = 1, 2, 3  # this is the same as x = 1, y = 2, z = 3

# one value can be assigned to multiple variables
x = y = z = 4  # this is the same as x = 4, y = 4, z = 4

# a collection of values can be unpacked to variables
fruits = ['apple', 'banana', 'mango']
# this is the same as apple = 'apple', banana = 'banana', mango = 'mango'
apple, banana, mango = fruits

# values that are assigned to variables can be of different types:
name = 'John Doe'  # this is a string data type, can also be instantied with double-quotes
id = 4485  # int (number without decimals)
weight = 174.3  # float (number with decimals)
is_active = False  # bool (a bool variable takes one two values True or False)

# the same variable can assume different values of different types throughout the life of a program
name = 'John Doe'  # name is str variable
name = 1837  # name is an int variable
name = False  # name is a bool variable

# in order to determine a variable's type you can use the built-in type function
name = 'John Doe'
type(name)  # this returns <class str> (i.e. the variable is of type str)
id = 13085
type(id)  # this return <class int>

# a constructor function is a function that creates a variable of a certain type
# every built-in data type has a constructor function
name = str('John Doe')  # equivelant to name = 'John Doe'
id = int(19385)  # equivelant to id = 19385
weight = float(154.4)  # equivelant to weight = 154.4
is_active = bool(False)  # equivelant to is_active = False
# all these statements are equivelant

# constructors can also be used to convert one data type to another
id = '12'
type(id)  # this will return <class str>
id = int(id)  # this converts the id variable from str to int
type(id)  # this will return <class int>
# example: convert from integer to string
id = 2764
type(id)  # this will return <class int>
id = str(id)
type(id)  # this will return <class str>
# example: convert from float to int
weight = 145.5
type(weight)  # this will return <class float>
# when converting from float to int, the variable loses decimals
weight = int(weight)
type(weight)  # this will return <class int>
# example: bad conversions (casting)
id = '12s'
int(id)  # this will throw an error because there is no way to convert 12s to a number

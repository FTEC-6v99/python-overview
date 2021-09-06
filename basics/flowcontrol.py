'''
  Flow control
'''
# if/else statement
if 1 == 1:
    print('duh!')
else:
    print('The world is ending!')

# an if statement controls whether a block of code will execute or not
# the code will execute only when the if statement condition evaluates to True
# syntax: if <condition> : <code>

# common conditional operators:
# == :  equals
# != :  does not equal
# > :   greater than
# >= :  greater than or equal
# < :   less than
# <=    less than or equal
# and:  combine two conditions with and
# or:   comines two conditions with or

animal = 'dog'
if animal == 'cat':
    print('a cat!')
elif animal == 'fish':  # use elif to nest if statements. Like if, elif expects a condition which determines whether the code block will execute
    print('a fish!')
else:
    print('It must be a dog!')

'''
Loops
Conditional control whether a code block should execute or not.
Loops control how many times a code block should execute
'''

# for loop
for x in range(10):  # range is a built-in function (widely used in for loops) that returns an array from 0 to the number provided to the function as argument
    print(x)  # in every iteration x will be assigned a value from 0 to 10

# loop over list contents using the in keyword
fruits = ['apple', 'banana', 'mango']
for fruit in fruits:
    print(f'Yummy! a {fruit}')

# while loop
# a while look accepts a condition and will continue to loop over its code block
# as long as the condition evalues to true
i = 10
while i > 0:
    print(i)
    i += 1  # this is shorthand for i = i + 1

# DANGER: be careful not to write infinite loops with while (i.e., a while loop where the condition never evaluates to false)

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

'''
The continue keyword with loops:
'''
# use continue to skip an iteration in a loop and proceed to the next iteration. Example:
for i in range(5):
    # range returns a list that starts with 0 and ends with arg -1 (i.e., range(5) -> [0,1,2,3,4])
    if i == 1:
        i -= 1
        continue  # the continue keyword will skip the iteration when i == 1
    print(i)  # this will print 0, 2, 3, 4

# continue with while loop (this works for similarly to for loop):
i = 5
while i >= 0:
    if i == 1:
        i -= 1
        continue
    print(i)

'''
The break keyword with loops:
'''
# the break keyword forces a loop to termiante before completeing the full iterations
for i in range(5):
    if i == 4:
        break  # this will termniate the loop immediately
    print(i)  # this will print 0,1,3

# break works the same way with while loop:
i = 5
while i >= 0:
    if i == 0:
        break
    print(i)  # this will print 5,4,3,2,1
    i -= 1

'''
The else keyword with loops:
'''
# you can also add an else block to a for/while loop. The code in the else block will execute after the loop terminates:
i = 5
while i >= 0:
    print(i)
    i -= 1
else:
    print('the loop terminated successfully!')

# else works the same with for loops
for i in range(5):
    print(i)
else:
    print('the loop terminated successfully')

# NOTE: the else code block does not run if the for/while loop was terminated using the break keyword
i = 5
while i >= 0:
    if i == 4:
        break
    print(i)
    i -= 1
else:
    print('This line will not print because the loop termianted abruptly with the break keywords')

# NOTE: the else code block will work as expected with the continue keyword. Else will execute once at the end of the loop
for i in range(5):
    if i == 4:
        i -= 1
        continue
    print(i)
    i -= 1
else:
    print('this line will run once after the loop terminates successfully')

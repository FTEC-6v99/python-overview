'''
Collections

A collection is a variable that can be assigned multiple values
There are four built in collections in Python:
1. List
2. Tuple
3. Set
4. Dictionary

'''

'''
List
'''
# construct a list using the square brackets
fruits = ['apple', 'banana', 'mango']
# a list is:
# 1. ordered:           the order of items in the list is guaranteed
# 2. mutable:           items can be added, removed, and updated from a list
# 3. allow duplicates:  a list can store two identical items

# each item in a list has an index: a numeric value that refer to the item's position in the list
# lists are 0-based (i.e., the first element has an index of 0)

# to retrieve an element from a list use the element's index between square brackets
apple = fruits[0] # this will return the first element in the list
banana = fruits[1] # second element in the list

# to add elements to a list use the append function
fruits.append('kiwi') # this will add the item to the end of the list

# to insert an element in a specific position use the insert funtion
fruits.insert(2, 'orange')

# to remove an item from a list:
# remove function
fruits.remove("kiwi")
# del keyword 
del fruits[0] # deletes the first item in the list
# pop function: returns and removes the item with the given index
fruits.pop(2)

# use the built-in len function to get the number of elements in a list
size = len(fruits)

# ways to loop over a list
for fruit in fruits:
  print(fruit)
# or
for i in range(len(fruits)):
  print(fruits[i])

'''
Tuple
'''
# to construct a tuple use the parantheses
ids = (154, 187, 192, 101)

# Like lists, tuples allow duplicates and are ordered.
# unlike lists, tuple are immutable (can not change!)

# Tuple items are accessed the same way as lists:
id1 = ids[0] # like lists (and all other Python collections), tuples are use 0-based index
id2 = ids[1]

# you can use the in keyword to check if an item exists in a tuple:
if 154 in ids:
  print('154 ID is found')

# loop over tuple:
for id in ids:
  print(id)
# or 
for i in range(len(ids)):
  print(ids[i])

'''
Set
'''
# to construct a set use the curly braces
departments = {'Sales', 'Engineering', 'Marketing', 'Finance'}

# Sets are:
# 1. unordered: the order of items is not guaranteed
# 2. immutable: items can not be changed
# 3. unique: duplicates are not allowed

# The distinguishing feature about sets is that they don't allow duplicates
departments_with_duplicates = {'Sales', 'Sales', 'Engineering', 'Marketing', 'Finance'}

# the above two sets are identical, because one of the two Sales items will be removed (no duplicated allowed)

# to add an item to a set use the add function
departments.add('Accounting')

# to remove an item from a set use the remove or pop functions
departments.remove('Sales')
departments.pop() # with sets pop doesn't not accept an argument because items in a set are not accessible

# looping over a set
for department in departments:
  print(department)

'''
Dictionaries
'''
# Dictionaries are a collection of key, value pairs:
employee_name_by_id = {
  1: 'John Doe',
  2: 'Jane Doe',
  3: 'James Doe'
}

# to access an item in a dictionary use the get function:
employee_name_by_id.get(1) # returns John Doe
employee_name_by_id.get(4) # returns None (i.e., key with value 4 is not found in the dictionary)

# to add an item to a dictionary:
employee_name_by_id[4] = 'Mohamad Doe'
# note keys in dictionary are unique, if you add a new value to an existing key it will overide the existing value

# to get all the keys
employee_name_by_id.keys()

# to get all values
employee_name_by_id.values()

# to get all items: a list of key, value tuples
employee_name_by_id.items()

# to loop over dictionary:
for id in employee_name_by_id.keys():
  print(f'Employee id: {id}, Employee name: {employee_name_by_id[id]}')
# or
for id, name in employee_name_by_id:
  print(f'Employee ID: {id}, Employee name: {name}')
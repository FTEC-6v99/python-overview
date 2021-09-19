# A class is a blueprint for creating objects in Python.
# Objects are made up of 1) attributed and 2) methods (i.e., functions that could be executed on the object)
class Animal():
    # the __ini__ method is called to create a new object from the Animal class
    # the first argument to the __init__ function is self: a reference to the object itself.
    # you can supply as many other args as you like in the __init__ constructor. These args are called class attributed when assigned to the self object.
    def __init__(self, name, weight, age):
        self.name = name  # declaring a class attribute called name
        self.weight = weight  # declaring a class attribute called weight
        self.age = age  # declaring a class attribute called age

    # a function inside of a class with first arg as self is called a class method.
    def make_sound(self):
        # when the interpreter reads pass, it will continue execution without impact (similar to reading comments)
        pass

# In order for a class to inherit from another class, we will need to add the name of the parent class in paranthesis after the name of the child class.
# the below means the Dog class extends from the Animal class (i.e., the dog class will have the same attributes/methods as the parent class: Animal)


class Dog(Animal):
    # constructor method __init__ for the dog class
    def __init__(self, name, weight, age, dog_breed):
        # since the dog class is a child of Animal (the parent class) we can user the super keyword to access parent level attributes/methods
        super.__init__(name, weight, age)
        self.breed = dog_breed

    def make_sound(self):  # this method overrides the similar method declared on the parent class
        print('Whoof!')


class Cat(Animal):
    def __init__(self, name, weight, age, cat_breed):
        super.__init__(name, weight, age)
        self.cat_breed = cat_breed

    def make_sound(self):
        print('Meow!')


# in order to create an object from a class use the class name followed by paranthesis and supply the class attributes
animal = Animal('Olive', 30.5, 1)
# this will have no impact since the make_sound method is not implemented on the parent class.
print(animal.make_sound())

dog = Dog('Rupert', 85, 7, 'Goldendoodle')
dog.make_sound()  # this should print: Whoof!

cat = Cat('Missy', 12, 3, 'Some cat breed')
cat.make_sound  # this should print: Meow!

# NOTE: when calling a class function you don't have to pass a self reference as the first argument, the interpreter automatically ingests the self
# variable when you call a class method.

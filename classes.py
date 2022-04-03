# Classes
# Class named Cat, which has two attributes: color and legs.
class Cat:
    # __init__ - called when an instance (object) of the class is created
    # The __init__ method is called the class constructor.
    # self - must have self as their first parameter
    # refers to the instance calling the method.
    # Attributes - Instances of a class have attributes
    # Cat instances have attributes color and legs
    def __init__(self, color, legs):
        # In an __init__ method, self.attribute can therefore be used to
        # set the initial value of an instance's attributes.
        self.color = color
        self.legs = legs

felix = Cat("ginger", 4)
rover = Cat("dog-colored", 4)
stumpy = Cat("brown", 3)

class Book:
    def __init__(self, title, pages, topics):
        self.title = title
        self.pages = pages
        self.topics = topics

# How classes get information
class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def intro(self):
        print(self.name + " (Level " + self.level + ")")

# 1st - get the information You need
name = input()
level = input()

# 2nd - pass it to the class
p1 = Player(name, level)
# 3rd - use the intro method to print the player name and 
p1.intro()

# Inheritance
# way to share functionality between classes. Sharing the same attributes
class Animal: # SUPERCLASS Animal
    def __init__(self, name, color):
        self.name = name
        self.color = color
# Class Cat with attribute SUPERCLASS Animal
class Cat(Animal):
    def purr(self):
        print("Purr...")
# Class Dog with attribute SUPERCLASS Animal  
class Dog(Animal):
    def bark(self):
        print("Woof!")

fido = Dog("Fido", "brown")
print(fido.color)
fido.bark()
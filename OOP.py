# -------------------------------------------------
# Object Oriented Programming System (OOPS) in Python
# -------------------------------------------------

# Class = blueprint of objects
# Object = instance of class

# ---------------------------
# Example: Class and Object
# ---------------------------
class Python:
    def new(self):   # Method inside class
        print("Hello World")

    def old(self):
        print("Hello Danish")


class JavaScript:
    def boss(self):
        print("Hello")

    def laptop(self):
        print("Danish")


# Object creation
ob = Python()
ob.new()
ob.old()

js = JavaScript()
js.boss()

# ---------------------------
# OOPS Main Concepts
# ---------------------------
# Polymorphism - many forms
# Encapsulation - data hiding
# Inheritance - veerasat (reusability)
# Abstraction - blueprint


# ---------------------------
# Inheritance Example
# ---------------------------
class PythonParent:   # Parent Class
    def code(self):
        print("We are here to code")

class Java(PythonParent):   # Child Class
    def new(self):
        print("Java is new for us")

js = Java()
js.code()
js.new()


# ---------------------------
# Types of Inheritance
# ---------------------------

# 1. Single Inheritance (done above)

# 2. Multiple Inheritance
class GrandParent:
    def legacy(self):
        print("Grandparent")

class Parent(GrandParent):
    pass

class Child(Parent):
    pass

# 3. Multilevel Inheritance
class Father:
    def skills(self):
        print("Father")

class Mother:
    def skills(self):
        print("Mother")

class ChildMulti(Father, Mother):
    pass

# 4. Hierarchical Inheritance
class ParentH:
    def skills(self):
        print("Parent")

class Child1(ParentH):
    pass

class Child2(ParentH):
    pass

# 5. Hybrid Inheritance
class Animal:
    def sound(self):
        print("Animals make sounds")

class Dog(Animal):     # Single Inheritance
    def bark(self):
        print("Dog barks")

class Puppy(Dog):      # Multilevel Inheritance
    def cute(self):
        print("Puppy is cute")

class Cat(Animal):     # Another branch
    def meow(self):
        print("Cat meows")

# Object creation
obj = Puppy()
obj.sound()
obj.bark()
obj.cute()

obj2 = Cat()
obj2.sound()
obj2.meow()


# ---------------------------
# Polymorphism - many forms
# ---------------------------
class PythonPoly:
    def new(self):
        print("Python is new")

class JavaPoly:
    def new(self):
        print("Java is good")

p = PythonPoly()
j = JavaPoly()
p.new()
j.new()


# ---------------------------
# Abstraction - Blueprint
# ---------------------------
from abc import ABC, abstractmethod

class Vehicle(ABC):   # Abstract Class
    @abstractmethod
    def start(self):
        pass

class Bike(Vehicle):   # Concrete class
    def start(self):
        print("Bike starts")

b = Bike()
b.start()


# ---------------------------
# Variables: Local, Public, Protected, Private
# ---------------------------

class Variables:
    def __init__(self, a, b, c, d):
        self.local = a        # Local (only inside method)
        self.public = b       # Public
        self._protected = c   # Protected (for subclass use)
        self.__private = d    # Private (name mangling)

    def show(self):
        print("Public:", self.public)
        print("Protected:", self._protected)
        print("Private:", self.__private)

obj = Variables(10, 20, 30, 40)
obj.show()
print("Accessing public:", obj.public)
# print(obj.__private)  # ❌ Error: private variable


# ---------------------------
# Encapsulation Example
# ---------------------------
class Encapsulation:
    def __init__(self, a, b, c):
        r = a              # Local
        self.b = b         # Public
        self.__c = c       # Private
        print("Local inside constructor:", r)

    def old(self):
        print("Public:", self.b)
        print("Private:", self.__c)

enc = Encapsulation(20, 30, 40)
enc.old()
print("Public outside:", enc.b)


# ---------------------------
# Constructor Example
# ---------------------------
class PythonConst:
    def __init__(self):
        print("Welcome - Constructor always runs without calling")

p = PythonConst()
# What are oops concepts? Is multiple inheritance supported in java
"""ans :python has been an object oriented language slice it existed. because of this creating and using classes and
       object are downrightway.
       thare are five oop concepts.
       
       Class: A blue print for an object
       Objects: An instance/part example of class
       Polymorphism:Ability to react in different way having the same name having many forms"
       types :1.overloadin
              2.overriding
       Encapsulation:Wrapping up od data into a single unit"
                    "here the unit is representes as our class"
       Inheritance:Inheritance: Ability to adapt the behaviour and propart of parent class to child class 
                  here two or more class are in parent-child relation.
                  inheritance will always follow parent-to-child
              
              ***** TYPE OF INHERITANCE*****
              1.single leval inheritance
              2.multi leval inheritance
              3.multipal inheritance
              4.hirirchical inheritance
              5.hybrib inheritance



      Inheritance is one of the core concepts of Object-Oriented Programming.
      Multiple Inheritance is the process in which a subclass inherits more than one superclass.
      Java does not support Multiple Inheritance; however,
      Java interfaces help us achieve Multiple Inheritance of type in Java."""

# How to Define a Class in Python? What Is Self? Give An Example Of A Python Class
"""ans :class  is a component of oops concept.class is defined by "class" keyword.by defining a class you can perform oops
      concept thats why it is important.\
      self: self is a by default paramater of any function . """

class A:
    def a(self):
        print("hello my name is bhumi")

a1=A()
a1.a()

print("-----------------------------------------------------------------------------------------")
# Write a Python class named Rectangle constructed by a length and  width and a method which will compute the area of a rectangle
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def compute_area(self):
        return self.length * self.width

rectangle1 = Rectangle(5, 10)

area = rectangle1.compute_area()
print("Area of the rectangle:", area)

print("---------------------------------------------------------------------------------------------")
# Write a Python class named Circle constructed by a radius and twomethods which will compute the area and the perimeter of a circle 
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def compute_area(self):
        return math.pi * self.radius ** 2

    def compute_perimeter(self):
        return 2 * math.pi * self.radius


circle1 = Circle(5)

area = circle1.compute_area()
perimeter = circle1.compute_perimeter()

print("Area of the circle:", area)
print("Perimeter of the circle:", perimeter)

print("----------------------------------------------------------------------------------------------------")

# Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle 
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def compute_area(self):
        return math.pi * self.radius ** 2

    def compute_perimeter(self):
        return 2 * math.pi * self.radius

circle1 = Circle(5)


area = circle1.compute_area()
perimeter = circle1.compute_perimeter()

print("Area of the circle:", area)
print("Perimeter of the circle:", perimeter)

print("-------------------------------------------------------------------------------------------------")

#Explain Inheritance in Python with an example? What is init? Or What Is A Constructor In Python?
"""ans: inheritance in python allows a class (Known as a subclass or derived class) to inherit attribtes and behaviors from
 another class (known as super class or base class)
 init : init method is a super method and it also know a constuctor method.by use  of init method you can take data or
 value from another methods"""

class A():
    def a(self):
        print("this is A class")
class B(A):
    def b(self):
        print("this is B class")
b1 = B()
b1.a()
b1.b()

print("-----------------------------------------------------------------------------------------------------")

# What is Instantiation in terms of OOP terminology?
""""""

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
my_car = Car("Toyota", "Camry")
print(my_car.make)
print(my_car.model)

# What is used to check whether an object o is an instance of class A?

"""In Python, you can use the isinstance() function to check whether an object is an instance of a specific class.
The isinstance() function returns True if the object is an instance of the specified class or any of its subclasses.
Otherwise, it returns False."""

class A:
    pass

class B(A):
    pass

o = B()

# Check if o is an instance of class A
if isinstance(o, A):
    print("o is an instance of class A.")
else:
    print("o is NOT an instance of class A.")

# What relationship is appropriate for Course and Faculty?
--> """single inheritance is used for cource and faculty."""

# What relationship is appropriate for Student and Person? 
"""multileval inheritance is used for student and person"""

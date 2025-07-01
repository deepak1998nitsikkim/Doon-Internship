# Object-Oriented Programming (OOP) in Python - Overview & Examples

## What is Object-Oriented Programming (OOP)?

Object-Oriented Programming (OOP) is a paradigm that organizes software design around data, or objects, rather than functions and logic. An object can be defined as a data field that has unique attributes and behavior.

### Key Concepts:
1. **Class**: Blueprint for creating objects.
2. **Object**: Instance of a class.
3. **Encapsulation**: Hiding internal state and requiring all interaction to be performed through an object's methods.
4. **Abstraction**: Hiding complex realities while exposing only the necessary parts.
5. **Inheritance**: Mechanism of basing an object or class upon another object or class.
6. **Polymorphism**: Ability to use a shared interface for multiple forms (data types).

### Why OOP?
- **Modular code**
- **Reusable components**
- **Easier maintenance**
- **Scalability**

## Procedural vs OOP Example

### Without OOP
def area(length, width):
    return length * width

print(area(5, 3))

### With OOP
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

r = Rectangle(5, 3)
print(r.area())

## 20 Python OOP Programs

# 1. Class with method
class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello", self.name)

s = Student("Alice")
s.greet()

# 2. Class with two methods
class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

c = Calculator()
print(c.add(3, 4))
print(c.multiply(5, 6))

# 3. Inheritance example
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()
d.bark()

# 4. Constructor demonstration
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def details(self):
        print(f"{self.brand} - {self.year}")

car = Car("Toyota", 2020)
car.details()

# 5. Encapsulation example
class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print("Balance:", self.__balance)

acc = BankAccount()
acc.deposit(1000)
acc.show_balance()

# 6. Polymorphism example
class Bird:
    def sound(self):
        print("Tweet")

class Duck(Bird):
    def sound(self):
        print("Quack")

b = Bird()
d = Duck()
b.sound()
d.sound()

# 7. Class with default arguments
class Employee:
    def __init__(self, name="Guest"):
        self.name = name

    def show(self):
        print("Name:", self.name)

e = Employee()
e.show()
e2 = Employee("John")
e2.show()

# 8. Class with class variable
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    def show(self):
        print("Objects created:", Counter.count)

c1 = Counter()
c2 = Counter()
c1.show()

# 9. Class with static method
class Math:
    @staticmethod
    def square(x):
        return x * x

print(Math.square(6))

# 10. Class with property
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

t = Temperature(25)
print(t.fahrenheit)

# 11. Method Overriding
class Parent:
    def show(self):
        print("Parent")

class Child(Parent):
    def show(self):
        print("Child")

c = Child()
c.show()

# 12. Using super()
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Bike(Vehicle):
    def __init__(self, brand, cc):
        super().__init__(brand)
        self.cc = cc

b = Bike("Yamaha", 150)
print(b.brand, b.cc)

# 13. Multiple inheritance
class A:
    def feature1(self):
        print("Feature 1")

class B:
    def feature2(self):
        print("Feature 2")

class C(A, B):
    pass

c = C()
c.feature1()
c.feature2()

# 14. Destructor example
class Test:
    def __del__(self):
        print("Destructor called")

t = Test()
del t

# 15. Operator overloading
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(1, 2)
p2 = Point(3, 4)
result = p1 + p2
print(result.x, result.y)

# 16. Abstract base class
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

s = Square(5)
print(s.area())

# 17. Composition
class Engine:
    def start(self):
        print("Engine starts")

class Car:
    def __init__(self):
        self.engine = Engine()

    def run(self):
        self.engine.start()
        print("Car is running")

c = Car()
c.run()

# 18. Object comparison
class Box:
    def __init__(self, volume):
        self.volume = volume

    def __eq__(self, other):
        return self.volume == other.volume

b1 = Box(10)
b2 = Box(10)
print(b1 == b2)

# 19. Private attributes
class Person:
    def __init__(self, name):
        self.__name = name

    def show(self):
        print("Name:", self.__name)

p = Person("Alice")
p.show()

# 20. Chaining methods
class Builder:
    def __init__(self):
        self.data = ""

    def add(self, text):
        self.data += text + " "
        return self

    def show(self):
        print(self.data)

b = Builder()
b.add("Hello").add("World").show()

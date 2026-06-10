# Classes and objects 
class Student:
    pass

s1 = Student()
s2 = Student()

print(type(s1))
# here s1 and s2 are the instance(Object) and Student is the class


# init constructor -> this is created when any object is created from the class
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Harsh", 22)

print(s1.name)
print(s1.age)

# this internally looks like 
# Student.__init__(s1, "Harsh", 22) so self refers here to the current object 
class Student:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("My name is", self.name)

s1 = Student("Harsh")
s1.introduce()

# pythin internally does Student.introduce(s1)


#Instance Variable Each object has its own copy.

class Student:
    def __init__(self, name):
        self.name = name
s1 = Student("Harsh")
s2 = Student("Aman")

# Each object stores a different name.
#Class Variable -> Shared by all objects.

class Student:
    school = "GLA University"

    def __init__(self, name):
        self.name = name

# Inheritance Child class inherits from parent class.

class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    pass

d = Dog()

d.eat()
# dog inherited the eat


#super class -> Used to call parent class methods.
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

# as if we dont call the super can't take the name from the parent 
d = Dog("Tommy", "Labrador")

# Method overriding -> Child replaces parent implementation.
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Bark")

d = Dog()
d.speak()


# getitem -> it allows us indexing  
class Numbers:
    def __init__(self):
        self.data = [10, 20, 30]

    def __getitem__(self, index):
        return self.data[index]

n = Numbers()

print(n[1])


#@staticmethod  Doesn't need self.
# does not need object 
class Math:
    @staticmethod
    def add(a, b):
        return a + b
print(Math.add(10, 20))



# @classmethod -> Works with the class itself.
class Student:
    school = "GLA"

    @classmethod
    def show_school(cls):
        print(cls.school)

Student.show_school()


#

class Student:

    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1

    @classmethod
    def total_students(cls):
        print("Total:", cls.count) 

s1 = Student("Harsh")
s2 = Student("Aman")
s3 = Student("Rohit")
Student.total_students()



# Abstarct classs An abstract class acts like a contract or blueprint. It defines what methods child classes must implement. If a child class forgets to implement any abstract method, Python will not allow an object of that class to be created.
from abc import ABC, abstractmethod

class LLM(ABC):

    @abstractmethod
    def generate(self, prompt):
        pass

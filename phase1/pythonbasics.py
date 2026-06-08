# Python fundaments
#Integers
x = 10
print(x)
a = 10
b = -5
print(a-b)

name = "Upgrading"
print(name)

# boolean
is_active = True
print(is_active)


# Type Conversion (Conversion of one data types into another)
print(int("10"))
print(type(str(100)))


#isinstance 
x = 10
print(isinstance(x, int))


#String Slicing
s = "HelloWorld"
print(s[0:5])
print(s[5:])  


# split used to convert string to list
s = "apple,banana,grape"
print(s.split(","))  # ['apple', 'banana', 'grape']

# join used to make list to string
words = ["AI", "is", "fun"]
print(" ".join(words))  # AI is fun

#replace 
s = "I love Java"
print(s.replace("Java", "Python"))


user = {"name": "Harsh", "age": 22}
print(user)
#create
user["city"] = "Delhi"
print(user)


users = [
    {"name": "A", "age": 20},
    {"name": "B", "age": 25}
]

print(users[0]["name"])


names = ["A", "B"]
ages = [20, 25]

for n, a in zip(names, ages):
    print(n, a)


#functions 
def greet():
    print("Hello AI Engineer")
greet()

#*args when we dont know that how many arguments are their in function args becomes a tuple:
def sum_all(*args):
    print(sum(args))

sum_all(1, 2, 3, 4)


def show_info(**kwargs):
    print(kwargs)

show_info(name="AI", model="GPT", version=4)


# function wth default values
def greet(name="Guest"):
    print("Hello", name)

greet()

# we can overwrite it
greet("Harsh")


def student(**kwargs):
    print(kwargs)

student(name="Harsh", age=22)

#Output:
#Store them as dictinory key value pairs
{'name': 'Harsh', 'age': 22}

#function with return 
def add(a, b):
    return a + b

result = add(10, 20)

print(result)



# return multiple values
def student():
    return "Harsh", 22

print(student())
# here python return the tuple so can be easy for us to unpack it
def student():
    return "Harsh", 22

name, age = student()

print(name)
print(age)

# Lambda function = A lambda is a small anonymous function.
students = [
    ("Harsh", 22),
    ("Aman", 20),
    ("Rohit", 25)
]

students.sort(key=lambda x: x[1])
# here key we write so that we can know about or what thing we are using to sort like name age 
print(students)


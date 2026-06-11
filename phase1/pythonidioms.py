### list Comprehension
squares = []
for i in range(5):
    squares.append(i * i)
print(squares)


squares = [i * i for i in range(5)]
print(squares)
evens = [i for i in range(5)]
print(evens)


# Set
nums = [1, 2, 2, 3, 3, 4]
unique = {x for x in nums}
print(unique) 

#Generator generator values one by one as in list it stores everthing in memory
gen =(i for i in range(100000))


#map
nums = [1, 2, 3]
result = list(map(lambda x: x * 2, nums))

print(result)

#filer 
nums = [1,2,3,4,5]
result = list(filter(lambda x:x%2==0,nums))
print(result)



#unpacking 
a,b , *rest = [1,2,3,4,5]
print(a)
print(b)
print(*rest)

 
#any()  Returns True if at least one value is True.
names = ["Harshit","Naman"]
print(any(name=="Harshit" for name in names))


#sorted() sorting using key
students = [
    ("Harsh", 22),
    ("Aman", 20),
    ("Rohit", 25)
]
print(sorted(students, key=lambda x: x[1]))


#counter()
from collections import Counter
words = ["apple", "banana", "apple"]
count = Counter(words)
print(count)


#default dictionary here not have to check the condition if key is empty it make a empty list assign to it 
from collections import defaultdict

students = [
    ("Harsh", "A"),
    ("Aman", "B"),
    ("Rohit", "A")
]

grades = defaultdict(list)

for name, grade in students:
    grades[grade].append(name)

print(grades)


#Deque for fast insertion and removal

q = deque()

q.append(1)
q.append(2)

print(q)
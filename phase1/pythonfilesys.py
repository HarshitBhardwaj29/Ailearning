# Writing to a file
file = open("notes.text","w")
file.write("Hello Harsh")
file.close

#reading from a file 
file = open("notes.text","r")
content = file.read()
print(content)
file.close()

#context
with open("notes.text", "r") as file:
    data = file.read()

print(data)


#writing csv
import csv 

rows = [
    ["name", "age"],
    ["Harsh", 22],
    ["Aman", 21]
]
with open("students.csv","w",newline="") as file:
    writer = csv.writer(file)
    writer.writerows(rows)
    
#'import csv
with open("students.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

#json 
# write by using dump and load to get using json.read
import json

data = {
    "name":"Harshit",
    "roll":23,
}

with open("user.json","w") as file:
    json.dump(data,file)

#pickle 
import pickle

data = [1, 2, 3]

with open("data.pkl", "wb") as file:
    pickle.dump(data, file)
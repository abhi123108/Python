info={
    "key" : "value",
    "name": "Abhinav",
    "age":34,
    "Is Adult":True,
    "marks": 78.8,
    "subjec": ["python" , "C", "java"],
    "topic": ("dict" , "set")
}

print(info["subjec"])
info["name"]="Sakshi"
info["sirname"]="Pandey"
print(info)


#nested Dictionary

student={
    "name": "Abhinav",
    "subject":{
        "phy":78,
        "chem":89,
        "maths":99
    }
}

print(student)

print(student["subject"]["chem"])

#Method

print(student.keys())
print(len(student))
print(student.values())

print(student.items())

print(student.get())


student.update({"name":"khushi"})


#Sets

collection ={1,2,3,4,5,6 , "hello" , "Abhi"}
print(collection)
print(type(collection))


#Methods
set= {2,3,4,5,3,8,9,}
newSet={0,8,1,5,6,5,4}
set.add(7)
set.add("Abhinav")

set.clear()

print(set)
print(set.pop())
print(set.union(newSet))

print(set.intersection(newSet))


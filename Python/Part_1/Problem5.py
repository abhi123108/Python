#Store following word meaning in a python Dictionary
#    table: "a piece of furniture", "list of facts & figures"
#   cat: "a small animal"

dictionary = {
    " cat": "a small animal",
    "table":["a piece of furniture", "list of facts & figures"]
    
}
print(dictionary)

# you are given a list pof subject for student. Assume one classroom is
#required for 1 subject . how many classroom are needed by all student?

Sub={"python" ,"java", "C++", "python", "javascript", "java" , "python", "java", "C++", "C"}
print(len(Sub))


# WAP to enter marks of 3 Subject from the user and store them in a dictionary. Start with 
#an empty dictionary & add one by one . Use subject name as key and marks a value.

marks={}

x=int(input("enter phy"))
marks.update({"phy":x})

x=int(input("enter maths"))
marks.update({"maths":x})

x=int(input("enter chem"))
marks.update({"chem":x})

print(marks)


#Figure outa way to store 9 & 9.0 as separate values in the set.

values={9 , "9.0"}
print (values)
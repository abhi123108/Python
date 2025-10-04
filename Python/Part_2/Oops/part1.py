# class Student:
#     name="Abhnav"


# s1=Student()
# print(s1.name)

# class Student:
#     college_name="ABC College"
#     def __init__(self , name , marks):
#         self.name=name
#         self.marks=marks
#         print("addindg new student in database")

# s1=Student("karan" ,98)
# print(s1.name , s1.marks)

# s2 =Student("Abhinav",99)
# print(s2.name , s2.marks)

# print(s2.college_name)



class Student:
    college_name="ABC College"
    def __init__(self , name , marks):
        self.name=name
        self.marks=marks
    
    
    def welcome(self):
        print("Welcome Students",self.name)
    
    def get_marks(self):
        return self.marks

s1=Student("karan" ,98)
s1.welcome()
print(s1.get_marks())


#Abstraction

class Car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False
    
    def start(self):
        self.clutch=True
        self.acc=True
        
        print("car started")

car1=Car()
car1.start()
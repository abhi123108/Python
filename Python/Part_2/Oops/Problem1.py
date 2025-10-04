#Create student class that takes name and marks of 3 subject as argument
# in constructor. then create a method to print the average.

class Student:
    def __init__(self , name,marks):
        self.name=name
        self.marks=marks
    
    def get_average(self):
        sum=0
        for val in self.marks:
            sum += val
        print("Hii", self.name,"Your avg. score is :" , sum/3)
        
s1=Student("Abhinav" ,[99,98,97])
s1.get_average()

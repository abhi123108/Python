#Define a Employee class with attribute role , department & sallary.
#this class also has a showDetail Methos.
# Create an engineer class that inherit properties from employee &
#has additional attribute : name & age

class Employee:
    def __init__(self , role , dept , salary):
        self.role=role
        self.dept=dept
        self.salary=salary
    
    def showDetails(self):
        print("role =",self.role)
        print("dept =", self.dept)
        print("salary =", self.salary)

class engineer(Employee):
    def __init__(self, name , age):
        self.name=name
        self.age=age
        super().__init__("Engineer", "IT", "75000")

engg1=engineer("Elin Musk",40)
engg1.showDetails()
class Account:
    def __init__(self , acc_no , acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass

    def reset_pass(self):
        print(self.__acc_pass)


acc1=Account("12345", "abcde")

print(acc1.acc_no)
print(acc1.reset_pass())



class Person():
    __name="anynomous"
    
    def __hello(self):
        print("hello person")
        
    
    def welcome(self):
        self.__hello()

p1=Person()

print(p1.welcome())



#INHERITANCE

# class Car:
#     @staticmethod
#     def start():
#         print ("car started")
    
#     @staticmethod
#     def stop():
#         print("car stopped")

# class ToyotaCar(Car):                             #SINGLE INHERITANCE
#     def __init__(self , name):
#         self.name= name

# car1=ToyotaCar("fortuner")
# car2=ToyotaCar("pyrus")

# print(car1.name)
# print(car1.start())


class Car:
    @staticmethod
    def start():
        print ("car started")
    
    @staticmethod
    def stop():
        print("car stopped")

class ToyotaCar(Car):                                    #MULTILEVEL INHERITANCE
    def __init__(self , brand):
        self.brand=brand

class Fortuner(ToyotaCar):
    def __init__(self , tyoe):
        self.type = type

car1=Fortuner("diesel")
Car.start()




class A:
    varA="Welcome to class A"

class B:
    varB="welcome to class B"                      #MULTIPLE INHERITANCE

class C(A , B):
    varC="welcome to class C"

c1=C()

print(c1.varC)
print(c1.varB)
print(c1.varA)





class car:
    def __init__(self, type):
        self.type=type
    
    @staticmethod
    def start():
        print("car started")
    
    @staticmethod
    def stop():
        print("car stopped")

class toyotaCar(car):
    def __init__(self, name ,type):
        super().__init__(type)
        self.name=name
        super().start()

car1=toyotaCar("prius", "electric")
print(car1.type)



class Porson():
    name = "anonymous"
    
    # def changeName(self , name):
    #     self.__class__.name="Rahul"
    
    @classmethod
    def changeName(cls , name):
        cls.name=name

p1=Person()
p1.changeName("Rahul")
print(p1.__name)
print(Person.name)




class student():
    def __init__(self, phy , chem, maths):
        self.phy=phy
        self.chem=chem
        self.maths=maths
    
    @property
    def percentage(self):
        return str((self.phy+self.chem+self.maths)/3)+"%"

stu1=student(93,98,99)
print(stu1.percentage)




#POLYMORPHISM

class Complex:
    def __init__(self , real , img):
        self.real=real
        self.img = img
    
    def showNumber(self):
        print(self.real, "i +" , self.img, "j")
    
    
    def __add__(self, num2):
        newReal=self.real + num2.real
        newImg =self.img + num2.img          #  __add__ = dunder function
        return Complex(newReal, newImg)
    
    
    def __sub__(self, num2):
        newReal=self.real + num2.real
        newImg =self.img + num2.img
        return Complex(newReal, newImg)

num1=Complex(1,3)
num1.showNumber()


num2=Complex(4,6)
num2.showNumber()

num3 =num1+num2
num3.showNumber()
#WAP to check if a number entered by the user is odd or even
num=int(input("enter your no."))

if(num%2==0):
    print("Number is Even")
else:
    print("number is Odd")
    

#WAP to find the greatest of 3 numbers enter bhy the user

a=int(input("First Number"))
b=int(input("Second Number"))
c=int(input("Third Number"))
if(a>b and a>c ):
    print(a)
elif(b>c and b>c ):
    print(b)
else:
    print(c)
# count = 5
# while count <= 5:
#     print("hello")
#     count += 1



#print number 1 to 5

# i=1
# while i<=5:
#     print(i)
#     i+=1




#print the multiplication of a number n.

# n=int(input("enter no."))
# i=1
# while i<=10:
#     print(n*i)
#     i+=1



#print the element of the following list using a loop
#[1,4,9,16,25,36,49,64,81,100]

# nums =[1,4,9,16,25,36,49,64,81,100]

# idx=0
# while idx<len(nums):
#     print(nums[idx])
#     idx+=1




#Search for a number x in this tuple using loops

tup=(1,4,9,16,25,36,49,64,81,100)
x=int(input("Enter no :"))
i=0
while i<len(tup):
    if (tup[i]==x):
        print("found at idx :", i)
        break                                         #BREAK
    else:
        print("not found")
        i+=1




i=0
while i<=5:
    if(i==3):
        i+=1
    continue              #SKIP
print (i)
i+=1



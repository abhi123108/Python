
#WAP to ask the user to enter names of there 3  favorite moveis & Store them in list

Movies=[]

m1=input("enter first movie")
m2=input("enter second movie")
m3=input("enter third movie")

Movies.append(m1)
Movies.append(m2)
Movies.append(m3)

print(Movies)

#Wap to check if a list contain a pelindrome of element

list1=[1,2,1]
list2=[1,2,3]

copy_list1=list1.copy()
copy_list1.reverse()

if(copy_list1==list1):
    print("pelindrome")
else:
    print("not pelindrome")
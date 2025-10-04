list=[1,2,3,4,5,6,7]

for num in list :
    print(num)



tup=(1,2,3,4,5,6)

for num in tup:
    print(num)



#print the element of the following list usin a loop
#[1,4,9,16,25,36,49,64,81,100]

# list=[1,4,9,16,25,36,49,64,81,100]

# for el in list:
#     print(el)



#Search for a number x in this tuple using loop
#[1,4,9,16,25,36,49,64,81,100]

tup=(1,4,9,16,25,36,49,64,81,100)

x=49
idx =0
for el in tup:
    if el==x:
        print("Found at idx :", idx)

        idx+=1



#RANGE

for i in range(5):
    print(i)


for i in range(1 , 10):  #range(Start , stop)
    print(i)


for i in range(1, 10 , 2):    #range(Start , stop, step)
    print(i)



#PASS

for i in range(5):
    pass

if i >5:
    pass

print("useful Work")


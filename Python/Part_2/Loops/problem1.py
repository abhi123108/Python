#WAP tomfind the sum of first n numbers. (Using While)

n=5
sum=0
i=1
while i<=n:
    sum+=i
    i+=1
print("Total Sum is :",sum)





#WAP  to find factorial of first n no. (Using for)

n=5
fact=1


for i in range(1 , n+1):
    fact *=i

print("factorial is : " , fact)
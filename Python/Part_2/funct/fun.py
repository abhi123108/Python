def cal_sum(a , b):
    sum =a+b 
    print(sum)
    return sum

cal_sum(2,3)


def cal_Avg(a,b,c):
    sum =a+b+c
    avg=sum/3
    print(avg)
    return avg

cal_Avg(4,5,8)


#WAF to print the length od a list

cities=["Buxar" , "gurgao", "noida" , "mumbai" , "chennai"]

def print_len(cities):
    print(len(cities))

print_len(cities)


#WAF to print the element of the list in a single line.


cities=["Buxar" , "gurgao", "noida" , "mumbai" , "chennai"]

def print_list(list):
    for item in list:
        print(item ,end=" ")

print_list(cities)



#WAF to print the factorial of n.

def fact(n):
    fact=1
    for i in range(1, n+1):
        fact*=i
    print(fact)

fact(5)

#WAF to convert USD to INR

def converter(usd_val):
    inr_val=usd_val*83
    print(usd_val, "USD =",inr_val,"INR")

converter(1)


def  odd_even(n):
    if n%2==0:
        print("Even")
    else:
        print("Odd")

odd_even(6)
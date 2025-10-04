# Reccurison Function

def show (n):
    if(n==0):                 #--BASE CASE
        return
    print(n)
    show(n-1)

show (5)


def fact(n):
    if(n==0 or n==1):
        return 1
    return fact(n-1)*n

print(fact(6))

#Write recursive function to calculate the sum of first n natural number


def calc_sum(n):
    if(n==0):
        return 0
    return calc_sum(n-1)+n

sum=calc_sum(5)
print(sum)



#Write recursive function to print all element in list

def print_list(list , idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)

cities=["Buxar" , "gurgao", "noida" , "mumbai" , "chennai"]

print_list(cities)
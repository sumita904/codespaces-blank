#if elif else concept

"""" 1st code
n=int(input("rupees"))
if n>=5:
    print("can buy biscuits")
elif n>=10:
    print("can buy chips")
elif n>=15:
    print("can buy chips and biscuits")
else:
    print("can't buy anything")
    """

""" voting
age=int(input("enter the age"))
if age>=18:
    print("person is eligible for voting")
else:
    print("person is not eligible for voting") 

"""
""" method 1

num1=int(input("enter no 1:"))
num2=int(input("enter no 2:"))
num3=int(input("enter no 3:"))

if num1<=num2:
    if num1<=num3:
        smallest=num1
        if num2<=num3:
            middle=num2
            largest=num3
        else:
            middle=num3
            largest=num2
    else:
        smallest=num3
        middle=num1
        largest=num2
else:
    if num2<=num3:
        smallest=num2
        if num1<=num3:
            middle=num1
            largest=num3
        else:
            middle=num3
            largest=num1
    else:
        smallest=num3
        middle=num2
        largest=num1
print(f"numbers are - {smallest},{middle},{largest}")

"""
#method2 - storing values like tupple

num1=int(input("enter no 1:"))
num2=int(input("enter no 2:"))
num3=int(input("enter no 3:"))

if num1<=num2<=num3:
    sort=(num1,num2,num3)
elif num1<=num3<=num2:
    sort=(num1,num3,num2)
elif num2<=num1<=num3:
    sort=(num2,num1,num3)
elif num2<=num3<=num1:
    sort=(num2,num3,num1)
elif num3<=num2<=num1:
    sort=(num3,num2,num1)
else:
    sort=(num3,num1,num2)
print(f"sorted values - {sort}")




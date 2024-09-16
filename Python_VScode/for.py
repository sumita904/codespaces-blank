"""print the no. is prime or not using for loop
num=int(input("enter num"))
x= True
for prime in range(2,num):
    if num%prime==0:
       x= False
       break  #here --we can/can't use break (without break also code will run)
if x:
    print(f"{num} is prime")
else:
    print(f"{num} is not prime")  
    """

"""factorial between the numbers
y=int(input("enter the num"))
z=int(input("enter the num"))
for i in range(y,z+1):
    x=1
    for a in range(i):
        x=x*(a+1)
    print(f"factorial of {i}= {x}")   
    """

y=int(input("enter the num"))
z=int(input("enter the num"))
x=1
for i in range(y,z+1):
    
    for a in range(i):
        print(f" {i}= {x}")  

#print the no. is prime or not using for loop
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
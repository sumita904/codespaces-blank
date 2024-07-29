"""print the no. is prime or not using for loop

num=int(input("enter no"))
x= True
for prime in range(2,num):
    if num%prime==0:
      x=False
      break   #break can be or can't be used here
if x:
   print(f"{num}no. is prime")
else:
   print(f"{num}no. is not prime")



num1=int(input("enter num1"))
num2=int(input("enter num2"))

for prime in range(num1,num2):
    x = True
    for y in range(2,prime):
      if prime%y==0:
         x=False
         break

    if x:
       print(f"{prime} is prime")

"""

"""print 5 table
for i in range(1,11):
     print(f" 5*{i} = {5*i}")
"""

#print factorial of any no

y=int(input("enter no"))
x=1
for i in range(1,y):
    x=x*(i+1)
print(x)





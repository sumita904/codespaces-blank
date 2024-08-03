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

"""print factorial of any no

y=int(input("enter no"))
x=1
for i in range(1,y):
    x=x*(i+1)
print(f"factorial of {y}= {x}")

"""
"""factorial between the nos
y=int(input("enter no"))
z=int(input("enter no"))
for i in range(y,z+1):
     x=1
     for a in range(1,i):
         x=x*(a+1)
     print(f"factorial of {i}= {x}")
     
     """
"""
i = 2
j = [1, 10, 100, 1000]
for x in j:
    print(f"{i * x:6}")
"""
""" Left to right pyramid
for x in range(1,6):
    for z in range(1,x+1):
       print(f"*",end=' ')
    print()
    """

"""Right to left pyramid
for x in range(1,6):
    for y in range(1,6-x):
        print(f" ",end=" ")
    for y in range(1,x+1):
        print(f"*",end=" ")
    print()
    """
#inverted  right to left pyramid
"""

for i in range(5):
    for j in range(i+1,6):
        print(f"*",end=" ")
    print() 
    
       """


"""right to left pyramid
for x in range(5):
    for y in range(x+1,5):
        print(f" ",end=" ")
    for y in range(x+1):
        print(f"*",end=" ")
    print()
    """
""" print full pyramid ------
for x in range(5):
    for y in range(x+1,5):
        print(f" ",end=" ")
    for y in range(x+1):
        print(f"*",end=" ")
    for y in range(x):
        print(f"*",end=" ")

    print()
    
"""

# print burfi ---------
for x in range(5):
    for y in range(x+1,5):
        print(f" ",end=" ")
    for y in range(x+1):
        print(f"*",end=" ")
    for y in range(x):
        print(f"*",end=" ")

    print()
for x in range(4):
    for y in range(x+1):
        print(f" ",end=" ")
    for y in range(x+1,5):
        print(f"*",end=" ")
    for y in range(x+1,4):
        print(f"*",end=" ")

    print()














"""
x=6
for i in range(1,x):

    space= ' '*(x-i)
    star= '*'*i
    space1=' '*(x-i-1)
    star1='*'*(i-1)
    print(space+star+star1+space1)

    """
"""
y=6
for i in range(1,y):
    space=''*(2*(y-i))
    star='* '*i
    print(space+star)
    """
"""
a= [b**2 for b in range(1,11)] #list comprehension
print (a)

y=[z for z in range(1,11) if z%2==0]
print(f"{y}")
  """

list1=[1,2,3]
list2=['a','b','c']
connect=[(x,y) for x in list1 for y in list2]
print(connect)
"""
list3=[1,2,3]
list4=['a','b','c']
connect1=[]   
for x in list3:
    for y in list4:
        connect1.append((x,y))
print(connect1) 
"""
"""
num1=int(input("num1"))
num2=int(input("num2"))
even_no=[y**2 for y in range(num1,num2) if y%2==0]
print(even_no)

"""
"""
number=[-1,-2,-3,1,2,3,4]
positive_no=[z for z in number if z>0]
print(positive_no)
"""

#dictionary - key,value
"""
key=['a','b','c']
value=[1,2,3]
dict={key[i]:value[i] for i in range(len(key))}
print(dict)
"""



































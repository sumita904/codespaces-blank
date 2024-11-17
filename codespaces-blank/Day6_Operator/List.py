"""A list is a collection of items in a particular order. You can make a list that includes the letters of alphabet,
the digits from 0 to 9, or the names of all the people in your family. You can put anything you want into a list, and
the items in your list don't have to be related in any particular way.A list usually contains more than one element,
it's a good idea to make the name of your list plural, such as letters, digits, or names. """
"""" example-----
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
"""
"""
matrix =[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for i in matrix:

    for element in i:
        print(element,end=" ")
    #print()
    """
"""
for i in range(1,11):
    for j in range(1,11):
        print(f"{i * j:4}",end=" ")
    print()
    """
#accessing elements in a list
"""
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[-1].title())
"""
"""
#Modifying elements in a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati') #add element to the last
print(motorcycles)

motorcycles[0]='bmw' #modifying element into a list
print(motorcycles)

motorcycles.insert(0,'tvs') #inserting elements into a list
print(motorcycles)

del motorcycles[-1] #Removing elements from a list
print(motorcycles)

popped_motorcycles= motorcycles.pop() #removes last item from the list but we can work with the poped item
print(popped_motorcycles)
print(f"The last  motorcycle I owned was a {popped_motorcycles.title()}.")

luxury_motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = luxury_motorcycles.pop(0)  #popping items from any position in a List.
print(f"The last  motorcycle I owned was a {first_owned.title()}.")

luxury_motorcycles.remove('yamaha')  #remove an item by value
print(luxury_motorcycles)
"""

matrix1=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
matrix2=[
    [3,2,1],
    [6,5,4],
    [9,8,7]
]

#matrix=[items*items2  for row in matrix1[3][] for items in row for row2 in matrix2 for items2 in row2 ]
"""
result= [[matrix1[i][j]*matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
for items in result:
    print(f"{items}")
    """
for j in  range(len(matrix1[0])):
    for i in range(len(matrix2[0])):
        result= [matrix1[i][j]*matrix2[i][j]]
        





#for row in matrix1:
    #for items in row:
        #print (f" {items}",end=" ")
        #print(*row)
#print(*[items for row in matrix1 for items in row])

































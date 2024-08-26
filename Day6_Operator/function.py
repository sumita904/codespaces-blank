"""
def mary(a,b):
    return a+b
result= mary(2,5)
print(result)
"""
def sub(x,y):
    return x-y
substract= sub(9,3)
print(substract)

def multi(x1,y1):
    return x1*y1
multiply= multi(5,2)
print(multiply)

def divide(x2,y2):
    return x2//y2
division= divide(6,2)
print(division)

def straut(name="england"):
    return f" hello {name}"
print(straut("broad"))
print(straut())

def allan(*i):
    return sum(i)
print(allan(5,4,9,13,-6))

#higher order functions
def calculation(a,b,c):
    return c(a,b) # c as a function
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
print(calculation(2,4,add))
print(calculation(6,4,sub))

def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))

# ----------------Lambda function-------------

square = lambda a: a**2
print(f"{square(4)}")

# prime no using lambda
prime = lambda b: all(b%i!=0 for i in range(2,b))
value=9
print(prime(value))

numbers=[3,6,9,21,10,17]
pnumbers=list(filter(prime,numbers))  #filtering prime nos as true false from "numbers" then accumulated as list to pnumbers
print(pnumbers)

#------decorator----
def deco(func):
    def wrapper():
        print("before calling the function")
        func()
        print("after calling the function")
    return wrapper
@deco
def hello():
    print("hello world")
hello()

"""add two numbers using decorator
def cal(add):
    def num1(*no):
        no(1,2,3)
        return num1()
        add()
@cal
def sum1():
    print(sum (num1))
 sum1()   
    """
"""
def deco(func):
    def wrapper(*args):
        print(f"calling function : {func.__name__} with arguments:{args} ")
        result=func(*args)
        print(f"function:{func.__name__} returned: {result}")
        return result
    return wrapper
@deco
def add(a,b):
    return a+b
add(2,5)
"""

def factorial(func):
    def number(arg):
        print(f"enter the no : {arg}")
        result=func(arg)
        print(f"factorial returned: {result}")
        return result
    return number
""" using recurssion
@factorial
def fact(f):
    if f ==0 or f==1:
        return 1
    else:
        return f*fact(f-1)  #-----using recurssion-----
fact(5)
"""
@factorial
def fact(f):
    cal=1
    for i in range(1,f):
        cal= cal*(i+1)
    return cal
fact(6)

# fibonacci series ---------

def fibbo(func1):
    def series(*arg1):
        print(f"enter the range : {arg1}")
        value=func1(*arg1)
        #print(f"fibonacci series returned: {value}")
        return value
    return series
@fibbo
def fibonacci(v,r):
    series_cal=0
    for i in range(0,2):

        series_cal=series_cal+ i
        print(f"{series_cal}",end=" ")

    return series_cal

fibonacci(0,25)


""" yield
def text():
    yield 1
    yield 2
    yield 3
for j in text():
    print (f"{j}")
    
"""



















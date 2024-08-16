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
    return c(a,b)
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
print(calculation(2,4,add))
print(calculation(6,4,sub))

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














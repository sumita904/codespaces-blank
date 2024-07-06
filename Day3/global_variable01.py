#use the "global" keyword if you want to change the global variable inside a function

#To change the value of a global variable inside function, refer to the variable by using the"global" keyword

x="awesome"
def myfunc():
  global x
  x="fantastic"

myfunc()
print("Python is " + x)
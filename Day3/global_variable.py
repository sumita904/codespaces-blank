#variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables
#Global variables can be used by everyone, both inside of functions and outside
#CREATE A VARIABLE OUTSIDE OF A FUNCTION, AND USE IT INSIDE THE FUNCTION
X="awesome"
def myfunc():
 print("Python is " + X)

myfunc()

"""If you create a variable with same name inside a function,this variable will be local, can only be used inside the function.
The global variable with the same name will remain as it was, global with the original value"""

#CREATE A VARIABLE INSIDE A FUNCTION, WITH THE SAME NAME AS THE GLOBAL VARIABLE
Y="awesome"
def myfunc():
  Y="fantastic"
  print("Python is " + Y)

myfunc()

print("Python is " + Y)

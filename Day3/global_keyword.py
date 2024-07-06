#______The Global Keyword ______
"""Normally, when you create a variable inside  a function, that variable is local, and can only be used inside that function.
To create global variable inside a function, you can use the global keyword """

#IF YOU USE THE GLOBAL KEYWORD, THE VARIABLE BELONGS TO THE GLOBAL SCOPE:

def myfunc():
 global x
 x="awesome"

myfunc()
print("Python is " + x)


#Length of a String

random_string = "I am a batman" # 11 characters
print(len(random_string))

#Indexing and Reverse Indexing
#A string in Python is indexed from 0 to n-1 where n is its length.

batman = "Bruce Wayne"
first = batman[0]  # Accessing the first character
print(first)
space = batman[5]  # Accessing the empty space in the string
print(space)
last = batman[len(batman) - 1]
print(last)

batman = "Bruce Wayne"
print(batman[-1])  # Corresponds to batman[10]
print(batman[-5])  # Corresponds to batman[6]



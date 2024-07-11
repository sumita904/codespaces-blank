message="hello world is the first thing"
print(message)

print("first -", message[0])
print("second -", message[1], message[-1])

print("slice from 7 to end -" , message[7:]) #slice from 7 to end
print("length of string is -",len(message)) #30(including space)

#uppercase the whole word
First_name="sumita"
Last_name="sinha"
Full_name=First_name +" " + Last_name
print("full name is :-", Full_name)

print("uppercase -",First_name.upper())
print("uppercase -",Last_name.upper())
print("length of string is -",len(Full_name)) #12(including space)

#Lowercase the whole word
First_name="SUMITA"
Last_name="SINHA"
Full_name=First_name +" " + Last_name
print("lowercase -", First_name.lower())
print("lowercase -", Last_name.lower())

#search word in the sentence using "f" function
search="norld"
if search in message:
    print(f'"{search}" is available') #or we can also use -print(search ,"is available")
else:
    print(f'"{search}"is not available') #or we can also use -print(search ,"is not available")

#splliting the sentence in word
message1="human is the powerful animal on the planet,beware of them"
words=message1.split()
print("words in the message:",words)


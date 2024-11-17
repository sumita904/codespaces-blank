#set are mutable i.e it's value can be changed later
my_set = {1, 2, 3}
new_set = my_set
new_set.add(4)

print(my_set)
print(new_set)
#---to remove---
new_set.remove(4)
print(new_set)
print(my_set)
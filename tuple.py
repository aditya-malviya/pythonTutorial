#Tuple Data Type/Data Structure

#Tuple is same as list, list is mutable tuple is immutable.
#immutable = unchangeable
#tuples allows duplicate values
#tuples allows heterogenious daa types 

mytyuple = ("one", "two", 1, True)
print(mytyuple)

mytuple1 = ("one", "two","three","one")
print (mytuple1)


#Diff of tuples from list
#syntax
my_list = [1,2,3,4]
my_tuple = (1,2,3,4)

print (my_list)
print (my_tuple)

#mutability
my_list[2] = 10
print (my_list)  # 1,2,10,4
#my_tuple[1] = 10
print(my_tuple)


print(my_list.__sizeof__())
print(my_tuple.__sizeof__())


#List and tuples are same, the only diff is list is mutable and tuple is immutable
# both are ordered, slicing, duplicate, heterogenious

my_tuple1 = (10,)
print (my_tuple1)
print (type(my_tuple1))

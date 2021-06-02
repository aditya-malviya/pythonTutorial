#List! -> heterogenious, mixed data types 
#Array -> homogenious data type, data of same type

#How to declare list empy
my_first_list = []

#List with values 
my_list_with_values = [2,6,3,6]
print (my_list_with_values)

#List with diff data types 
my_list_with_diff_data_types = [4,True,"Aditya",9.4]
print (my_list_with_diff_data_types)

#Indexing
second_list = ['r','t','a','z','w','p']
print ("The first character is:", second_list[0])
print (second_list[:-1])

#Nested list, list in list
nested_list = ["Aditya", [26,7], True]
print (nested_list[0][1])

#Negative Indices
negativeIndices = ['r','t','a']
print(negativeIndices[-2])

#Appending Lists
my_list = [2,4,6,7]
my_list.append(7)
print(my_list)
my_list.extend([8,3,9])
print(my_list)
my_list.sort()
print (my_list)
my_list.reverse()
print (my_list)

#delete/remove List

del_list = ['d','t','u','i','a','o']
del del_list[2]
print (del_list)
#remove multiple items
del del_list[1:3]
print (del_list)

length_list = [2,4,5,7,8,5]
print (len(length_list))


















#File Input and Output Operations
#---------------------------------

#mode
# "r" -> reading, "w" -> writing, "a" -> appending, "r+" -> reading and writing

#open -> gets the file to do some operations read or write

file = open('../2.txt', 'r')
for each in file:
    print (each)


file1 = open('../3.txt', 'r')
print(file1.read())


file2 = open('../3.txt', 'r')
print(file2.read(100))
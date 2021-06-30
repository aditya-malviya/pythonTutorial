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


writefile = open('sample.txt', 'w')
writefile.write("Hello Geekls")
writefile.close()


f = open("sample.txt", "a")
f.write("Hello this is using append")
f.close()


writefile1 = open('sample1.txt', 'w')
writefile1.write("Hello Geekls using writefile1")
writefile1.close()

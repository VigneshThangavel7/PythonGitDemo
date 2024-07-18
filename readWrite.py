# read and write the text file using the python

file = open("testData.txt")
# print(file.read())  # using read() we can read all the content of the respective file

# print(file.read(2))  # reads only the specific size

# print(file.readline())  # reads only single line
# print(file.readline())

# read the file line by line using while loop
#line = file.readline()
#while line != "":
#    print(line)
#    line = file.readline()

# another way
# git example
#    print(line)
#    line = file.readline()
listContent = file.readlines()  # this function stores all the contents inside the list
print(listContent)
print(listContent[0])

for i in listContent:  # using for loop we can print all the data inside the list
    print(i)

file.close()  # closing the file for preventing the memory leaks

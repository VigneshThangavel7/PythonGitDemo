# Writing inside the file
# another way to open and close the file
# "w" and "r" refers the read and write mode


# task --> open the file
# reverse all the content
# write back to the file

with open("testData.txt", "r") as reader:  # file is the object stores all the data to the file object
    content = reader.readlines()  # list of content of the file
    reversed(content)  # reversed using the reversed method
    with open("testData.txt", "w") as writer:  # open the file again for writing the file
        for line in reversed(content):  # iterates al the reverse list
            writer.write(line)  # Writes the reversed content in the file



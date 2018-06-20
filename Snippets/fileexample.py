#opening and reading files
my_file = open("test.txt", "r")
print (my_file.read())
my_file.close()
print ("")

my_file = open("test.txt", "r")
print (my_file.readline())
print (my_file.readline())
print (my_file.readline())
print (my_file.readline())
print (my_file.readline())
my_file.close()
print ("")

my_file = open("test.txt", "r")
print (my_file.readlines())
my_file.close()
print ("")

#writing in a file
my_file1 = open("test.txt", "a")
my_file1.write("\n" + "understood")
my_file1.close()
my_file1 = open("test.txt", "r")
print (my_file1.read())
my_file1.close()

#creating a new file and writing to it
#my_file2 = open("test1.txt", "x")
#my_file2.write("hi ok")
#my_file2.close()

#with as opening and editing files
with open("test.txt", "r") as r:
    print (r.read())
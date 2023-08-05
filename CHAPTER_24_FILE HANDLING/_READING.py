#READING EXAPMLE
#READING TEXT FROM EXIiSTING FILE (data_read.txt)
f1 = open ("E:\\data_read.txt", "r")
print("reading text from existing file (data_read.txt) .\n ".upper())
print(f1.read().upper())
f1.close()


#APPENDING TEXT ON THE ABOVE EXISTING FILE (data_read.txt)
f1 = open("E:\\data_read.txt", "a")
f1.write("\nmy university name is shanto mariam university of creative technology.")
f1.close()


#READING TEXT AGAIN AFTER APPENDING FROM THE ABOVE EXISTING FILE (data_read.txt)
f1 = open("E:\\data_read.txt", "r")
print("\n\n\nreading text after appending new line on the above file (data_read.txt) .".upper())
print(f1.read().upper())
f1.close()


#READING TEXT LINE BY LINE (data_read.txt)
f1 = open("E:\\data_read.txt", "r")
print("\n\n\nreading text line by line on the above file (data_read.txt) .\n".upper())
print(f1.readline().upper())
print(f1.readline().upper())
print(f1.readline().upper())
print(f1.readline().upper())
print(f1.readline().upper())
f1.close()


#READING TEXT FROM EXIiSTING FILE (data_read.txt)
f1 = open ("E:\\data_read.txt", "r")
print("\n\n\nreading text (100) from existing file (data_read.txt) .\n ".upper())
print(f1.read(100).upper())
f1.close()


#READING TEXT LINE BY LINE (data_read.txt)
f1 = open("E:\\data_read.txt", "r")
print("\n\n\nreading text ( 30, 19 ) line by line on the above file (data_read.txt) .\n".upper())
print(f1.readline(30).upper())
print(f1.readline(19).upper())
f1.close()


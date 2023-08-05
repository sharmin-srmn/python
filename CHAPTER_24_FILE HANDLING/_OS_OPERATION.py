import os

#RENAME
#AT FIRST WE CREATE A FILE
f1 = open ("E:\\data_file.txt", "a")
f1.write("this file will be renamed.")
f1.close()

#READ THE FILE
f1 = open ("E:\\data_file.txt", "r")
print(f1.read())
f1.close()

#CHECK IF THE ( RENAMED )FILE EXISTS, THEN DELETE IT
if os.path.exists("E:\\data_file_renamed.txt"):
    os.remove("E:\\data_file_renamed.txt")
    
else:
    print("file doesn't exist".upper())

#NOW RENAME THE FILE    
os.rename("E:\\data_file.txt", "E:\\data_file_renamed.txt" )






#REMOVE
#AT FIRST WE CREATE A FILE
f1 = open ("E:\\data_file_delete.txt", "a")
f1.write("\n\n\nthis file will be deleted.")
f1.close()

#READ THE FILE
f1 = open ("E:\\data_file_delete.txt", "r")
print(f1.read())
f1.close()

#NOW RENAME THE FILE

if os.path.exists("E:\\data_file_delete.txt"):
    os.remove("E:\\data_file_delete.txt")
else:
    print("file doesn't exist".upper())





#CREATING FOLDER

if os.path.exists("E:\\Files"):
    os.rmdir("E:\\Files")
    os.mkdir("E:\\Files")
else:
    os.mkdir("E:\\Files")



#DELETING FOLDER

if os.path.exists("E:\\File_"):
    os.rmdir("E:\\File_")
else:    
    os.mkdir("E:\\File_")


    

#APPENDING EXAMPLE
#APPENDING TEXT ON NON_EXISTING FILE (IT WILL CREATE NEW FILE )
f1 = open("E:\\data_append.txt", "a")
f1.write("\nhi! this is sharmin akhter.")
f1.write("\nmy id is 201071054.")
f1.write("\ni'm writing text through append mode.")
f1.close()



#READING TEXT FROM THE NEWLY CREATED FILE
f1 = open("E:\\data_append.txt", "r")
print("reading file after appending (data_append.txt) .\n".upper())
print(f1.read().upper())
f1.close()

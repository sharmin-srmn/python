#WRITING EXAMPLE
#WRITING TEXT ON NON_EXISTING FILE ( IT WILL CREATE NEW FILE)
f1 = open("E:\\data_write.txt", "w")
f1.write("hi! this is sharmin akhter.")
f1.write("\nmy id is 201071054.")
f1.write("\ni'm writing text through write mode.")
f1.close()



#READING TEXT FROM THE NEWLY CREATED FILE
f1 = open("E:\\data_write.txt", "r")
print("reading file after writing (data_write.txt) .\n".upper())
print(f1.read().upper())
f1.close()



#APPENDING TEXT ON THE ABOVE FILE
f1 = open("E:\\data_write.txt", "a")
f1.write("\ni'm now on 10th semester.")
f1.write("\ni'm from cse department.")
f1.write("\ni'm writing text through append mode.")
f1.close()


#READING TEXT FROM AGAIN AFTER APPENDING
f1 = open("E:\\data_write.txt", "r")
print("\n\n\nreading file after appending (data_write.txt) .\n".upper())
print(f1.read().upper())
f1.close()





#CREATING EXAMPLE
#CREATING A NEW BLANK FILE
f1 = open ("E:\\data_create.txt", "x")
f1.close()


#WRITE ON THE ABOVE FILE
f1 = open ("E:\\data_create.txt", "w")
f1.write("hi! this is sharmin akhter.")
f1.write("\nmy id is 201071054.")
f1.write("\ni'm writing text through write mode.")
f1.close()


#READING TEXT FROM THE NEWLY CREATED FILE
f1 = open("E:\\data_create.txt", "r")
print("reading file after writing (data_create.txt) .\n".upper())
print(f1.read().upper())
f1.close()



#APPENDING TEXT ON THE ABOVE FILE
f1 = open("E:\\data_create.txt", "a")
f1.write("\ni'm now on 10th semester.")
f1.write("\ni'm from cse department.")
f1.write("\ni'm writing text through append mode.")
f1.close()



#READING THE TEXT AGAIN FROM THE NEWLY CREATED FILE
f1 = open("E:\\data_create.txt", "r")
print("\n\n\nreading file after appending (data_create.txt) .\n".upper())
print(f1.read().upper())
f1.close()


#OVERWRITE TEXT ON THE ABOVE FILE
f1 = open ("E:\\data_create.txt", "w")
f1.write("hi! this is sharmin akhter.")
f1.write("\nmy id is 201071054.")
f1.write("\ni'm from shanto-mariam university of creative technology ")
f1.write("\ni'm over writing previous text through write mode.")
f1.close()


#READING THE OVERWRITING TEXT FROM THE ABOVE FILE
f1 = open("E:\\data_create.txt", "r")
print("\n\n\nreading file after overwritting (data_create.txt) .\n".upper())
print(f1.read().upper())
f1.close()






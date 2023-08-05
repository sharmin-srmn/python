#CREATING A FILE WITH VAlUE
f1 = open ("E:\\data_num1.txt", "w")
f1.write("25")
f1.close()


#CREATING ANOTHER FILE WITH VALUE
f2 = open ("E:\\data_num2.txt", "w")
f2.write("45")
f2.close()


#READING VALUES FROM BOTH FILE
f1 = open("E:\\data_num1.txt", "r")
value_1 = f1.read()


f2 = open("E:\\data_num2.txt", "r")
value_2 = f2.read()


#CONVERTING STRING VALUES INTO INTEGER
value_1 = int(value_1)
value_2 = int(value_2)



#PERSORMING TASK
addition = value_1 + value_2
substraction = value_1 - value_2
multiplication = value_1 * value_2
division = value_1 / value_2


#CONVERTING INTEGER RESULT INTO STRING

addition = str(addition)
substraction = str(substraction)
multiplication = str(multiplication)
division = str(division)



# CREATING NEW FILE TO STORE THE RESULTS
f3 = open ("E:\\data_result.txt", "a")
f3.write("\nthe summition is = ".upper())
f3.write(addition)
f3.write("\nthe substraction is = ".upper())
f3.write(substraction)
f3.write("\nthe product is = ".upper())
f3.write(multiplication)
f3.write("\nthe quotent is = ".upper())
f3.write(division)



#CLOSING ALL FILE
f1.close()
f2.close()
f3.close()

























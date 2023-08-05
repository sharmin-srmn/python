TEMP = input("ENTER THE TEMPERATURE (E.G- 45F, 102C) = ")
NUMBER = int(TEMP[:-1])
UNIT = TEMP[-1].upper()
if UNIT == 'C':
    result = int(round(( NUMBER * 1.8 ) + 32)) 
    converted_unit = 'Fahrenheit'
elif UNIT =='F':
    result = int(round((NUMBER - 32) * (5/9)))
    converted_unit = 'Celsius'
else:
    print("INVALID INPUT")
    quit()
    
print("The ",converted_unit, "resut of ", TEMP ," = ", result, converted_unit )    

print("LEFT RIGHTANGLE")
row = int(input("How many rows do you want ? = "))
for i in range(1,row+1):          #assume for 1-5
    for j in range(i):          #
        print("*", end =" ")
    print()
    
print("loop end")


print("LEFT RIGHT ANGLE - REVERSE")
row = int(input("How many rows do you want ? = "))
for i in range(row, 0,-1):
    for j in range(i):
        print("*", end= " ")
    print()
    
print("loop end.")    


print("RIGHT RIGHTANGLE")
row = int(input("How many rows do you want ? = "))
for i in range(1,row + 1):
    for k in range(0,row-i):
        print(" " , end= " ")
    for j in range(i):
        print("*", end =" ")
    print()
    
print("loop end")    

print("RIGHT RIGHTANGLE REVERSE")
row = int(input("How many rows do you want ? = "))
for i in range(row,0 ,-1):
    for k in range(1,row+1-i):
        print(" ", end = " ")
    for j in range (i):
        print("*", end = " ")
    print()
print("loop end.")


print("LEFT RIGHT-ANGLE UP DOWN")
row = int(input("how many rows do you want ? = "))
for i in range(1,row+1):
    for j in range(i):
        print("*", end =" ")
    print()

for i in range(row-1,0,-1):
    for j in range(i):
        print("*", end = " ")
    print()    
        

print("LOOP END.")    


print("RIGHT RIGHT-ANGLE UP DOWN")
row = int(input("how many rows do you want ? = "))
for i in range(1,row+1):
    for k in range(row-i,0,-1):
        print(" ", end= " ")
    for j in range(i):
        print("*", end = " ")
    print()
for i in range(1,row):
    for k in range(i):
        print(" ", end = " ")
    for j in range(row-i,0,-1):
        print("*", end= " ")
    print()    
    
print("LOOP END.")    


print("pyramid increase 2")
row = int(input("how many rows do you want ? = "))
for i in range(1,row+1):
    for k in range(row-i, 0,-1):
        print(" ", end = " ")
    for j in range(2*i-1):
        print("*", end= " ")
    print()

print("LOOP END")

print("pyramid 2 increase reverse")
row = int(input("how many rows do you want ? = "))
for i in range(row,0,-1):
    for k in range(1,row+1-i):
        print(" ", end = " ")
    for j in range(2*i -1):
        print("*", end= " ")
    print()

print("LOOP END")

print("diamond  2 increase reverse")
row = int(input("how many rows do you want ? = "))
for i in range(1,row+1):
    for k in range(row-i, 0,-1):
        print(" " ,end =" ")
    for j in range(2*i -1):
        print("*", end=" ")
    print()
    
for i in range(row, 1, -1):
    for k in range(1, row+2-i):
        print(" ", end= " ")
    for j in range(2*i-3): 
        print("*", end= " ")
    print()    
    
    
print("LOOP END")


print("pyramid 1 increase")
row = int(input("how many rows do you want ? = "))
for i in range(0, row):
    for k in range(0,row-i-1):
        print(" ", end=" ")
    for j in range(0,i+1):
        print(" * ", end=" ")
    print()    



print("pyramid 1 decrease")
row = int(input("how many rows do you want ? = "))
for i in range(1,row+1):
    for k in range(1,i):
        print(" ", end = " ")
    for j in range(row+1-i, 0, -1):
        print(" * ", end = " ")
    print()
    
print("LOOP END")           

  
    
    


        

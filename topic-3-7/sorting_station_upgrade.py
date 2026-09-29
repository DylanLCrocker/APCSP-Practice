user_input = input()
destinationisinspect = False

shape = str(user_input[0:4])
color = str(user_input[4:7])
size = int(user_input[7:10])
mass = int(user_input[10:14])
condition = str(user_input[14])

if (condition == "D" or size > 50 or mass > 2000) and not(shape == "CUBE" and size <= 60 and mass <= 2500):
    print("INSPECT")
    destinationisinspect = True
else:
    if shape == "BALL":
        if (color == "RED") and (size > 10) :
            print("B")
        else:
            print("A")
    else:
        if shape == "CUBE" :
            if ((color == "GRN") or (color == "BLU")) and (size <= 10) :
                 print("C")
            else :
                print("D")
        else :
            print("E")

if destinationisinspect == True :
    print("HOLD")
else :
    if (mass > 1000) or (shape == "CONE"): 
        print("CRATE")
    else:
        if shape == "BALL":
            print("PADDED")
        else:
            print("BOX")
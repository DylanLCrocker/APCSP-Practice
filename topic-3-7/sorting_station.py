user_input = input("Enter Label Here: ")

shape = str(user_input[0:4])
color = str(user_input[4:7])
size = int(user_input[7:10])
mass = int(user_input[10:14])
condition = str(user_input[14])

if (condition == "D") or (size > 50) or (mass > 2000):
    print("Inspect")
elif (shape == "BALL") and (color == "RED") and (size > 10):
    print("B")
elif (shape == "BALL"):
    print("A")
elif (color == ("BLU" or "GRN")) and (shape == "CUBE") and (size <= 10) :
    print("C")
elif (shape == "CUBE"):
    print("D")
else:
    print("E")
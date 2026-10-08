# Sum of squares program
import math

value = int(input())
num = value
list_squares = []
passes = 0
recreated_value = 0

if (value > 1000000) or (value < 1) :
    print("Domain Error")
    

while (num > 0) :

    root = math.floor(math.sqrt(num))
    list_squares.append(root)
    num -= root ** 2
    passes += 1

for i in range(0, len(list_squares), 1) :
    recreated_value += (list_squares[i]) ** 2

print("Original Value: " + str(value))
print("Sum of Squares: " + str(list_squares))
print("Passes: " + str(passes))
print("Recreated Value: " + str(recreated_value))
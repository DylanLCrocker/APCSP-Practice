# Sum of squares program

import math

original_value = int(input())
num = original_value
list_squares = []
passes = 0
recreated_value = 0

if (original_value > 10 ** 12) or (original_value < 1) :
    print("Domain Error")
    quit()
    
while (num > 0) :

    root = math.floor(math.sqrt(num))
    list_squares.append(root)
    num -= root ** 2
    passes += 1

for i in range(0, len(list_squares), 1) :
    recreated_value += (list_squares[i]) ** 2

frequencys = {}

for i in range(0, len(list_squares), 1) :
    value = list_squares[i]
    if value in frequencys :
        frequencys[value] += 1
    else:
        frequencys[value] = 1

max_freq = 0
max_value = 0

for value, freq in frequencys.items() :
    if freq > max_freq :
        max_freq = freq
        max_value = value

#### finding if there are any perfect squares withign the squares:

# for i in range(0, len(list_squares), 1) :
#    if math.sqrt(list_squares[i]) % 1 == 0 :
#       print("there is a perfect square amound the list of squares")
#   else :
#       print("there is no perfect square amound the list of squares")
#
        
print("Original Value: " + str(original_value))
print("Sum of Squares: " + str(list_squares))
print("Passes: " + str(passes))
print("Recreated Value: " + str(recreated_value))
print("Mode: " + str(max_value) + ", found " + str(max_freq) + " times")
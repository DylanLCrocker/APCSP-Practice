clock_values = [13, 42]
labels = ["hours", "minutes"]

clock_values.append(17)
labels.append("seconds")

selected_index = 2

clock_value = clock_values[selected_index]
label = labels[selected_index]

bit_list = []

remaining = clock_value

bit_1 = remaining % 2
remaining = remaining // 2
bit_2 = remaining % 2
remaining = remaining // 2
bit_4 = remaining % 2
remaining = remaining // 2
bit_8 = remaining % 2
remaining = remaining // 2
bit_16 = remaining % 2
remaining = remaining // 2
bit_32 = remaining % 2

bit_list = [bit_32, bit_16, bit_8, bit_4, bit_2, bit_1]

binary_string = str(bit_32) + str(bit_16) + str(bit_8) + str(bit_4) + str(bit_2) + str(bit_1)

print(str(labels[selected_index]) + ": " + str(clock_value) + "  ->  " + str(labels[selected_index]) + ": " + binary_string)

reconstruct_clock_value = 32 * bit_list[0] + 16 * bit_list[1] + 8 * bit_list[2] + 4 * bit_list[3] + 2 * bit_list[4] + 1 * bit_list[5]
print("String Reconstruction: " + str(reconstruct_clock_value))
if reconstruct_clock_value == clock_value:
    print("yay it works, good reconstruction")
else:
    print("FAIL")
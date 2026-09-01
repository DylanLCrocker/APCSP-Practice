clock_values = [13, 42]
labels = ["hours", "minutes"]

clock_values.append(17)
labels.append("seconds")

selected_index = 1

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
print(str(clock_value) + "->" + str(bit_list[0:6]))
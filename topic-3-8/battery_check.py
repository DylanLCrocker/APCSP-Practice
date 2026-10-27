charges = [62, 28, 85, 14, 47]
is_80_or_more = False
low = charges[0]
num_bellow_30 = 0

for i in charges :
    if i < low :
        low = i

    if i < 30 :
     num_bellow_30 += 1

    if i >= 80 :
        is_80_or_more = True

print("Low: " + str(low))
print("Data points bellow 30: " + str(num_bellow_30))
print("Is a number greater than or equal to 80: " + str(is_80_or_more))
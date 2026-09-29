num = 27
transformations = 0
peak = num

print("Start: " + str(num))

while num != 1 and num < 1000000 and transformations <1000 :
    if num % 2 == 0 :
        num = num / 2
        transformations += 1 
    else :
        num = num * 3 + 1
        transformations += 1
        if num > peak :
            peak = num

print("Total Transformations: " + str(transformations))
print("Peak: " + str(peak))

if num > 1000000 :
    print("Error number to large")
elif transformations > 1000 :
    print("Error, too many transofrmaions")
else :
    print("Value has returned to 1")
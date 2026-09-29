a = 48
b = 18
repetitions = 0
 
while a != b :
    if a > b :
        a = a - b
        repetitions += 1
    else :
        b = b - a
        repetitions += 1

print("GCF: " + str(a))

print("Repetitions: " + str(repetitions))
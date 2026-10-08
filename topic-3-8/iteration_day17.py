a = 1
b = 10**9

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
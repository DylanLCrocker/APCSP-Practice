num = 199
new_num = 11
repetitions = 0

if num < 0 or num > 1000000 :
    print("Number not within range")

while new_num >= 10 : 
    repetitions += 1
    new_num = 0

    while num > 0 :
        new_num += num % 10
        num = num // 10
    num = new_num


print(new_num)
print(repetitions)
n = 101
lower = 0
upper = 1001

if (n > 1000000) or (n < 0) :
    print("Domain Error")

while (upper - lower) > 1 :
    midpoint = (lower + upper) // 2
    if midpoint ** 2 <= n :
        lower = midpoint
    else :
        upper = midpoint

print("Input: " + str(n))
print("Largest Perfect Square: " + str(lower))
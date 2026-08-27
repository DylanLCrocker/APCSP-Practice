scores = [72, 85, 91, 68, 88]
title = "weekly score report"
#1
print(scores[0])
print(scores[2])
print(scores[0:])
#2
scores[1] = 86
print(scores[len(scores)-1])
#3
scores.append(93)
#4
print(title[0:6])
print(title[13:])
#5
print(": " + str(scores))
#6
print(title + ": " + str(scores[0:]))

# 7. because lists contaiin many vars so you can replaceone at a time, however a string is only on var and parts of it can't be replaced.
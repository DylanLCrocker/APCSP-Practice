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

#Part 2
# PROVIDED INPUT: replace your old value/label selection with this.
values[selected_index] = int(input("Enter a number: "))
clock_value = values[selected_index]
selected_label = labels[selected_index]
print("You entered:", clock_value)

# YOUR CODE START: range decision, existing report, parity decision.

# YOUR CODE END

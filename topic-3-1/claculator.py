minutes_available = int(input("minutes available: ")) #the var minutes available is set to the input of the number of minutes available, and has data type "integer"
breaks = int(input("Number of Breaks: ")) #the var breaks is set to the input of the number of breaks, and has data type "integer"
break_minutes =int(input("Minutes Per Break: ")) #the break minutes available is set to the input of the number of minutes per break, and has data type "integer"

work_minutes = minutes_available - breaks * break_minutes #the work minutes is set to the # availble minutes minus breaks times time per break

print("Focused work minutes: ", work_minutes) #prints a string and the value of work minutes and int is needed or the data type wont be defined imput is what the user enters in the terminal, assighment is giving the vars values, expresstion is what the var expresses and output is what is printed in the terminal.
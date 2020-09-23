# Adds two numbers together (a + b)
def Add(a, b):
	return str(round(a+b, 4))

def Subtract(a, b):
	#subtracts two numbers a - b
	result = str(round(a-b,4))
	return result

def Multiply(a, b):
	# evaluate function
	result = round(a * b,4)
	# return answer as string
	return str(result)

def Divide(a, b):
	try:
		return str(round(a/b, 2))
	except ZeroDivisionError:
		return '[Division By Zero]'

###
# start of execution
###

##

# Subtract(a,b) tests
assert Subtract(10,5) == "5"
assert Subtract(87.4,63.5) == "23.9"
assert Subtract(-15,-34) == "19"

# tests (3 per operation)
##

# Add() tests
assert Add(5.2, 57) == "62.2"
assert Add(3626.236, 74.745) == "3700.981"
assert Add(-3.5, -7.4) == "-10.9"

# Multiply() tests
assert Multiply(4, 13) == "52"
assert Multiply(7.534, 36.2) == "272.7308"
assert Multiply(-84.2, 2.6) == "-218.92"

# Divide() tests
assert Divide(10, 5) == '2.0'
assert Divide(50, 2) == '25.0'
assert Divide(7, 2) == '3.5'

##
# user input/output
##

alive = True

while alive:

	eq = input("Enter a single-operator equation (eg, 5*2.5): ")

	result = "Result: "

	if ("+" in eq):
		result += Add(float(eq.split("+")[0]), float(eq.split("+")[1]))
	elif ("-" in eq):
		result += Subtract(float(eq.split("-")[0]), float(eq.split("-")[1]))
	elif ("*" in eq):
		result += Multiply(float(eq.split("*")[0]), float(eq.split("*")[1]))
	elif ("/" in eq):
		result += Divide(float(eq.split("/")[0]), float(eq.split("/")[1]))
	else:
		result = "Invalid input"

	print(result)

	quit = input("Quit [Y/N]: ")
	print('')
	if quit.lower() == 'y':
		alive = False
		break
	elif quit.lower() == 'n':
		pass
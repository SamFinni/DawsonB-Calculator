def Add(a, b):
	#TODO
	return "TODO"

def Subtract(a, b):
	#TODO
	return "TODO"

def Multiply(a, b):
	#TODO
	return "TODO"

def Divide(a, b):
	#TODO
	try:
		return str(round(a/b, 2))
	except ZeroDivisionError:
		return '[Division By Zero!]'

###
# start of execution
###

##
# tests (3 per operation)
##
assert Divide(10, 5) == '2.0'
assert Divide(50, 2) == '25.0'
assert Divide(7, 2) == '3.5'

#TODO

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

	stayAlive = input("Quit [Y/N]")
	print('')
	if stayAlive.lower() == 'y':
		alive = False
		break
	elif stayAlive.lower() == 'n':
		pass
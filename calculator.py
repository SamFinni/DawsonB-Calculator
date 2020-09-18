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

#TODO

##
# user input/output
##

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
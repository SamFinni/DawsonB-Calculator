# Adds two numbers together (a + b)
def Add(a, b):
	return str(round(a+b, 4))

def Subtract(a, b):
	#TODO
	return "TODO"

def Multiply(a, b):
	#TODO
	return "TODO"

def Divide(a, b):
	#TODO
	return "TODO"

###
# start of execution
###

##
# tests (3 per operation)
##

# Add() tests
assert Add(5.2, 57) == "62.2"
assert Add(3626.236, 74.745) == "3700.981"
assert Add(-3.5, -7.4) == "-10.9"

##
# user input/output
##

eq = input("Enter a single-operator equation (eg, 5*2.5): ").strip()

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
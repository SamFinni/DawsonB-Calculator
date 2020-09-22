def Add(a, b):
	#TODO
	return "TODO"

def Subtract(a, b):
	#TODO
	return "TODO"

def Multiply(a, b):
	# evaluate function
	result = round(a * b,4)
	# return answer as string
	return str(result)

def Divide(a, b):
	#TODO
	return "TODO"

###
# start of execution
###

##
# tests (3 per operation)
##

assert Multiply(4, 13) == "52"
assert Multiply(7.534, 36.2) == "272.7308"
assert Multiply(-84.2, 2.6) == "-218.92"

##
# user input/output
##

eq = input("Enter a single-operator equation (eg, 5*2.5): ").replace(" ", "")

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
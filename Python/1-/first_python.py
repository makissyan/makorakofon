tempX = (input("First number: "))
tempY = (input("Second number: "))
operation = input("Operation: ")

result = None

print (type(tempX))
print (type(tempY))
if (isinstance(tempX, float) or (isinstance(tempX, int))) and (isinstance(tempY, float) or isinstance(tempY, int)):

	x = float(tempX)
	y = float(tempY)

	if (operation == '+'):
		result = x + y

	elif (operation == '-'):
		result = x - y

	elif (operation == '*'):
		result = x * y

	elif (operation == '/' ):
		result = x / y
	
	else : print("Whhhaaattt???")

else : print("Mathafucka!")

if (result != None):
	print ("Result:", result)  
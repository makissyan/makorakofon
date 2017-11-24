import sys

def ifInt(variableToCheck):
    try: 
        int(variableToCheck)
        return True
    except ValueError:
        return False

counter = 1
quantityParametr = 0
isPhotoParametr = False

print len (sys.argv)
while (counter <= 2) :

	if (ifInt(sys.argv[counter])) & (quantityParametr == 0) :		
		quantityParametr = abs(int(sys.argv[counter]))
		counter +=1	

	else :
		if (str(sys.argv[counter]).lower() == "true") :
			isPhotoParametr = True
			print "Photo parametr is " + str(isPhotoParametr).upper()
			counter +=1
		else :
			if (counter == int (len (sys.argv))) & (quantityParametr < 0) :
				print "Quantity parametr couldn't be read, default value will be used instead..."
				counter += 1
			else :
				if (counter == len (sys.argv)) & (isPhotoParametr == False) :
					print "Photo parametr couldn't be read, default value will be used instead..."
					counter += 1
				else :
					counter += 1

print "QUANTITY: " + str(quantityParametr)	
print "isPhotoParametr: " + str(isPhotoParametr)
'''	
while (counter < len (sys.argv)) & (counter < 3) :
				
	else:
		print "Incorrect format of " + str(counter) + " parametr... Default will be using instead."
		counter += 1
'''		
'''
if (len (sys.argv) == 2) :
	if ifInt(str(sys.argv[1])) :
		quantity = (str(sys.argv[1]))
		print quantity

	elif str(sys.argv[1]).lower() == "true" :
		isPhoto = True
		print isPhoto
	else:
 		print "Please use a correct format for arguments..."

if (len (sys.argv) == 3) :

	if (ifInt(str(sys.argv[1]))) & (str(sys.argv[2]).lower() == "true") :
		isPhoto = True
		quantity = int(sys.argv[1])
		print quantity
		print isPhoto

	elif (str(sys.argv[1]).lower() == "true") &  (ifInt(str(sys.argv[2]))) : 
		isPhoto = True;
		quantity = int(sys.argv[2])
		print quantity
		print isPhoto
	else:
   		print "Please use a correct format for arguments..."

if (len (sys.argv) > 3) :
	print "Please use a correct quantity of arguments..."
#BEFORE GENERATING - CHECK IF QUANTITY > 0 !!!
'''
file = open("generatedContacts.vcf", "w")
file.close() 

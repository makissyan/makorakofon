import sys

def ifInt(variableToCheck):
    try: 
        int(variableToCheck)
        return True
    except ValueError:
        return False

counter = 1
while (counter < len (sys.argv)) & (counter < 3) :
	if (ifInt(sys.argv[counter])) :
		quantity = sys.argv[counter]
		print "the quantity is" + str(quantity)
		counter += 1
			
	elif (str(sys.argv[counter]).lower() == "true") :
		isPhoto = True
		print "Photo parametr is" + str(isPhoto)
		counter += 1
			
	else:
		print "couldn't read " + str(counter) + " parametr."
		counter += 1
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

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


while (counter <= len (sys.argv) or (counter < 4)) :
	
	if (ifInt(sys.argv[counter])) & (quantityParametr == 0) :		
		quantityParametr = abs(int(sys.argv[counter]))
			
	else :
		if (str(sys.argv[counter]).lower() == "true") :
			isPhotoParametr = True
			
		else :
			break
	print "\n"+str(counter)
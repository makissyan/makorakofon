import sys
import random
import string

def ifInt(variableToCheck) :
    try: 
        int(variableToCheck)
        return True
    except ValueError:
        return False

def namesGenerator() :
	randomLetters = ""
	lettersQuantity = random.randint(3,9)
	for x in xrange(1,lettersQuantity):
		randomLetters += random.choice(string.ascii_letters)
	return str(randomLetters.capitalize())

#def photoGenerator() :

counter = 1
quantityParametr = 0
isPhotoParametr = False

while (counter < len (sys.argv) <= 3) :
#	print "\nloopstartedwith parametr " + str(sys.argv[counter])
	print "started main loop"
	if (ifInt(sys.argv[counter])) & (quantityParametr == 0) :		
		quantityParametr = abs(int(sys.argv[counter]))
		print "\nwe are in first if! counter now is" + str(counter) + ", but next step in should increase"
		counter +=1	
		print "\nint found? quantity is " + str(quantityParametr) + " and counter is " + str(counter)

	else :
		if (str(sys.argv[counter]).lower() == "true") :
			isPhotoParametr = True
			print "\nwe are in second if! isPhoto is" + str(isPhotoParametr) + " and now counter is " + str(counter) + ", but next step in should increase"
			counter +=1
			print "\ndid counter increased?" + str(counter)
		else :
			print "Please check format " + str(counter)
			counter +=1
			print "counter should +1!! it is: " + str(counter)
			
	
	print "\nendofloop"+str(counter)
		
if quantityParametr == 0:
	quantityParametr = 10
	print "\n\tCouldn't read quantity parametr... Default parametr {} will be used instead...".format(quantityParametr)
if isPhotoParametr == False:
	print "\n\tCouldn't read photo parametr... Default parametr ({}) will be used instead...".format(str(isPhotoParametr))

file = open("autoGenerated-{}-contacts.vcf".format(str(quantityParametr)), "w")


'''
for x in xrange(1,quantityParametr+1):
	file.write("BEGIN:VCARD\n")
	file.write("VERSION:3.0\n")
	file.write("N:" + "_SURNAME;" + "_NAME;;;\n")
	file.write("ORG:Harman\n")
	file.write("TEL;CELL:" + "_NUMBER\n")
	file.write("END:VCARD\n")
	print "Contact " + str(x) + " created..."
'''
r = random.randint(0,255)
print "\n" + str(r) + "\n"
print namesGenerator() + " " + namesGenerator()
#encoded = HEX_STRING.decode("hex").encode("base64")
file.close()
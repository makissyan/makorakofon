import subprocess
import string
import re

KNOWN_PHONES = ['CB5A27NUU4','10160ad8efee3403','0915f983de722d01','05445efb0a5cb40f','09a7ad48029a8b12','05535d970a5cab52','069a23bb344b6eaa',
'02b6f328d0236113','079ec7be00d355d8','32045110369281ad','ce0716079de52a1702','11160be17a933201','W3D7N15616010803','4790c0ccaeaa10fe']

#PATH = "D:\\TestApplicationPhone.properties"
PATH = "/home/maksym/project/TestController/resources/TestApplicationPhone.properties"
PHONES_SEARCH_EXPRESSION = re.compile("phone.\d")

actualPhones = []
errorPhones = []

print "\nRunning 'adb devices'...\n"
comResult = (subprocess.check_output(["adb devices"],shell=True)).decode("utf-8")
modifStr = comResult.replace("\r", ",").replace(" ", ",").replace("\n", ",").replace("\t", ",")
elements = modifStr.split(',')

for x in range (0, len(elements)) :
	if elements[x] in KNOWN_PHONES :
		if elements[x+1] == 'device' :
			actualPhones.insert(x, elements[x])
		else :
			errorPhones.insert(x, elements[x])			

#to write function for displaying list of phones
print "\tPhones found ({}): ".format(len(actualPhones))
for x in range (0, len(actualPhones)) :
	print "\t\t- " + str(actualPhones[x])

print "\n\tPhones with error ({}):".format(len(errorPhones))
for x in range (0, len(errorPhones)) :
	print "\t\t- " + str(errorPhones[x])

#to check if file exists

#to check if actual phones !=0

propertiesFile = open(PATH, "r")
wholeFile = propertiesFile.readlines()
propertiesFile.close()

for x in range (0, len(wholeFile)) :
	uncommentedPhones = PHONES_SEARCH_EXPRESSION.match(wholeFile[x])
	if str(uncommentedPhones).lower() != "none" :	
		wholeFile[x] = "#" + wholeFile[x]

print "\nSearching for phones in config file...\n" 
for x in range (0, len(actualPhones)) :
	for y in range(0,len(wholeFile)) :
		searchResult = re.search(actualPhones[x], wholeFile[y])
		if str(searchResult).lower() != "none" :	
			print "\tPhone " + str(actualPhones[x]) + "with number " + str(x+1) + " found on line " + str(y+1)
			for z in range (0,3) :
				wholeFile[y] = "phone." + str(x+1) + wholeFile[y][8:]
				y += 1

propertiesFile = open(PATH, "w")
propertiesFile.writelines(wholeFile)
propertiesFile.close()
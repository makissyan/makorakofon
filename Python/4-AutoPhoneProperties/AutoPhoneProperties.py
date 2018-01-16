import subprocess
import string
import re

KNOWN_PHONES = ['CB5A27NUU4','10160ad8efee3403','0915f983de722d01','05445efb0a5cb40f','09a7ad48029a8b12','05535d970a5cab52','069a23bb344b6eaa',
'02b6f328d0236113','079ec7be00d355d8','32045110369281ad','ce0716079de52a1702','11160be17a933201','W3D7N15616010803','4790c0ccaeaa10fe']

PATH = "D:\\TestApplicationPhone.properties"

STRINGS_RANGE = [13, 88]

actualPhones = []
errorPhones = []

print "\nRunning 'adb devices'...\n"
comResult = (subprocess.check_output(["testInput.py"],shell=True)).decode("utf-8")
modifStr = comResult.replace("\r", ",").replace(" ", ",").replace("\n", ",")
elements = modifStr.split(',')

for x in range (0, len(elements)) :
	if elements[x] in KNOWN_PHONES :
		if elements[x+1] == 'device' :
			actualPhones.insert(x, elements[x])
		else :
			errorPhones.insert(x, elements[x])

print "\tPhones found ({}): ".format(len(actualPhones))
for x in range (0, len(actualPhones)) :
	print "\t\t- " + str(actualPhones[x])

print "\n\tPhones with error ({}):".format(len(errorPhones))
for x in range (0, len(errorPhones)) :
	print "\t\t- " + str(errorPhones[x])

propertiesFile = open(PATH, "r")
wholeFile = propertiesFile.readlines()
#configLines = wholeFile [STRINGS_RANGE[0]:STRINGS_RANGE[1]]
print "\nSearching for phones in config file...\n" 

for x in range (0, len(actualPhones)) :
	for y in range(0,len(wholeFile)):
		searchResult = re.search(actualPhones[x], wholeFile[y])
		if str(searchResult).lower() != "none" :	
			print "\tPhone " + str(actualPhones[x]) + " found on line " + str(y+1) 

#	if actualPhones[x] in configLines : 



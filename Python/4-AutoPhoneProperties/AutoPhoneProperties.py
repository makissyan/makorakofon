import sys
import subprocess
import string
import re

def listDisplay(string, list) :
	print "\t" + string + "({}): ".format(len(list))
	for x in range (0, len(list)) :
		print "\t\t- " + str(list[x])
		if (x == len(list) -1) :
			print "\n"

def sortByPriority(fullReadyPhonesList, listToBeSortBy, string) :
	for x in range (0, len(fullReadyPhonesList)) :
		if fullReadyPhonesList[x] in listToBeSortBy :
			fullReadyPhonesList.insert(0, fullReadyPhonesList.pop(x))
			print "{} phone has been set on 1st place\n".format(string)
			break
		elif (x == len(fullReadyPhonesList) - 1) :
			print "{} phone couldn't be found in list of connected devices...\n".format(string)

KNOWN_PHONES = ['CB5A27NUU4','10160ad8efee3403','0915f983de722d01','05445efb0a5cb40f','09a7ad48029a8b12','05535d970a5cab52','069a23bb344b6eaa',
'02b6f328d0236113','079ec7be00d355d8','32045110369281ad','ce0716079de52a1702','11160be17a933201','W3D7N15616010803','4790c0ccaeaa10fe']
NEXUS_PHONES = ['05445efb0a5cb40f','09a7ad48029a8b12','05535d970a5cab52','069a23bb344b6eaa','02b6f328d0236113','079ec7be00d355d8']
SAMSUNG_PHONES = ['10160ad8efee3403','0915f983de722d01','32045110369281ad','11160be17a933201','4790c0ccaeaa10fe']

#Windows PATH:
PATH = "D:\\TestApplicationPhone.properties"
#Linux PATH:
#PATH = "/home/maksym/project/TestController/resources/TestApplicationPhone.properties"

PHONES_SEARCH_EXPRESSION = re.compile("phone.\d")

actualPhones = []
errorPhones = []
nexusPriority = False
samsungPriority = False

for x in range (0,len(sys.argv)) :
	if (str(sys.argv[x]).lower() == "samsung") :
		samsungPriority = True
		print "\nSamsung priority has been accepted..."
		break
	elif (str(sys.argv[x]).lower() == "nexus") :
		nexusPriority = True
		print "\nNexus priority has been accepted..."
		break	

print "\nRunning 'adb devices'...\n"
#comResult = (subprocess.check_output(["adb devices"],shell=True)).decode("utf-8")
comResult = (subprocess.check_output(["testInput.py"],shell=True)).decode("utf-8")
modifStr = comResult.replace("\r", ",").replace(" ", ",").replace("\n", ",").replace("\t", ",")
elements = modifStr.split(',')

for x in range (0, len(elements)) :
	if elements[x] in KNOWN_PHONES :
		if elements[x+1] == 'device' :
			actualPhones.insert(x, elements[x])
		else :
			errorPhones.insert(x, elements[x])

if (nexusPriority == True) :
	sortByPriority (actualPhones, NEXUS_PHONES, "Nexus")
if (samsungPriority == True) :
	sortByPriority (actualPhones, SAMSUNG_PHONES, "Samsung")

listDisplay("Ready phones: ", actualPhones)

if (errorPhones > []) :
	listDisplay("Phones with error: ", errorPhones)

try :
	propertiesFile = open(PATH, "r")
	wholeFile = propertiesFile.readlines()
	propertiesFile.close()

	for x in range (0, len(wholeFile)) :
		uncommentedPhones = PHONES_SEARCH_EXPRESSION.match(wholeFile[x])
		if str(uncommentedPhones).lower() != "none" :	
			wholeFile[x] = "#" + wholeFile[x]
	
	if (actualPhones > []) :
		for x in range (0, len(actualPhones)) :
			for y in range(0,len(wholeFile)) :
				searchResult = re.search(actualPhones[x], wholeFile[y])
				if str(searchResult).lower() != "none" :	
					for z in range (0,3) :
						wholeFile[y] = "phone." + str(x+1) + wholeFile[y][8:]
						y += 1
	else :
		print "\nCheck if phones connected properly."

	propertiesFile = open(PATH, "w")
	propertiesFile.writelines(wholeFile)
	propertiesFile.close()
	print "Config file has been succesfully updated."

except IOError :
	print "\nConfig file couldn't be opened. Check PATH variable."	
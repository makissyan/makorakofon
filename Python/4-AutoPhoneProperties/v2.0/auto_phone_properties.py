#!/usr/bin/env python2.7
import sys
import subprocess
import string
import re
import argparse

#listDisplay() - function for displaying lists. 
#Receives 2 parameters: string (text which should be displayed before list), list which should be displayed. 
def listDisplay(string, list) :
	print "\t" + string + "({}): ".format(len(list))
	for x in range (0, len(list)) :
		print "\t\t- " + str(list[x])
		if (x == len(list) -1) :
			print "\n"

#sortByPriority() - function for lists sorting by other list elements. Currently configured for shifting 1st found element to 1st place in list. 
#Receives 3 parameters: List which should be sorted, list with elements which will be taken as sorting criteria, string with a phone name.
def sortByPriority(fullReadyPhonesList, listToBeSortBy, phoneName) :
	print "{} priority has been accepted...".format(phoneName.upper())
	for x in range (0, len(fullReadyPhonesList)) :
		if fullReadyPhonesList[x] in listToBeSortBy :
			fullReadyPhonesList.insert(0, fullReadyPhonesList.pop(x))
			print "{} phone has been set on 1st place\n".format(phoneName.upper())
			break
		elif (x == len(fullReadyPhonesList) - 1) :
			print "{} phone couldn't be found in list of connected devices...\n".format(phoneName.upper())

#List of all known phones.
KNOWN_PHONES = ['CB5A27NUU4','10160ad8efee3403','0915f983de722d01','05445efb0a5cb40f','09a7ad48029a8b12','05535d970a5cab52','069a23bb344b6eaa',
'02b6f328d0236113','079ec7be00d355d8','32045110369281ad','ce0716079de52a1702','11160be17a933201','W3D7N15616010803','4790c0ccaeaa10fe']
#List of NEXUS phones.
NEXUS_PHONES = ['05445efb0a5cb40f','09a7ad48029a8b12','05535d970a5cab52','069a23bb344b6eaa','02b6f328d0236113','079ec7be00d355d8']
#List of SAMSUNG phones.
SAMSUNG_PHONES = ['10160ad8efee3403','0915f983de722d01','32045110369281ad','11160be17a933201','4790c0ccaeaa10fe']

#Regular expression for searching phone.* string.
PHONES_SEARCH_EXPRESSION = re.compile("phone.\d")

#Variable to store list of all connected and ready phones.
actualPhones = []
#Variable to store list of all connected, but not ready phones.
errorPhones = []


#Checking of given parameters for priority pointer and path.
parser = argparse.ArgumentParser(description = "Runs 'adb devices' and updates TestApplicationPhone.properties file with actual phone status.")
parser.add_argument ("-n", "--nexus", dest = "nexusPriority", action = 'store_true')
parser.add_argument ("-s", "--samsung", dest = "samsungPriority", action = 'store_true')
parser.add_argument("path", action='store')
args = parser.parse_args()

#Checking if path is valid and can be read
try :
	
		propertiesFile = open(args.path, "r")
		#Reading from TestApplicationPhone.properties by lines.
		wholeFile = propertiesFile.readlines()
		propertiesFile.close()

except IOError :
	print "\nConfig file couldn't be opened. Check the path..."
	sys.exit(0)


#Running external command 'adb devices' and converting output to utf-8 string.
print "\nRunning 'adb devices'...\n"
comResult = (subprocess.check_output(["adb devices"],shell=True)).decode("utf-8")

#Splitting string to a list by elements.
modifStr = comResult.replace("\r", ",").replace(" ", ",").replace("\n", ",").replace("\t", ",")
elements = modifStr.split(',')

#Checking if list contains known phones.
for x in range (0, len(elements)) :
	if elements[x] in KNOWN_PHONES :
		#If device is ready to use - adding phone to actualPhones list.
		if elements[x+1] == 'device' :
			actualPhones.insert(x, elements[x])
		#If device is not ready to use - adding phone and reason to errorPhones list.
		else :
			errorPhones.insert(x, elements[x] + " - " + elements[x+1])

#Sorting of phones according to setted priority.
if (args.nexusPriority == True) :
	sortByPriority (actualPhones, NEXUS_PHONES, "Nexus")
if (args.samsungPriority == True) :
	sortByPriority (actualPhones, SAMSUNG_PHONES, "Samsung")

#Displaying list of ready phones.
listDisplay("Ready phones: ", actualPhones)

#Displaying list of phones which connected, but not ready to be used.
if (errorPhones > []) :
	listDisplay("Phones with error: ", errorPhones)

#Commenting all phones.
for x in range (0, len(wholeFile)) :
	uncommentedPhones = PHONES_SEARCH_EXPRESSION.match(wholeFile[x])
	if str(uncommentedPhones).lower() != "none" :	
		wholeFile[x] = "#" + wholeFile[x]

#Checking if connected phones are ready.
if (actualPhones > []) :
	#Uncommenting connected and ready phones.
	for x in range (0, len(actualPhones)) :
		for y in range(0,len(wholeFile)) :
			searchResult = re.search(actualPhones[x], wholeFile[y])
			if str(searchResult).lower() != "none" :	
				for z in range (0,3) :
					wholeFile[y] = "phone." + str(x+1) + wholeFile[y][8:]
					y += 1
else :
	print "\nCheck if phones connected properly."

#Writing changes in TestApplicationPhone.properties.
propertiesFile = open(args.path, "w")
propertiesFile.writelines(wholeFile)
propertiesFile.close()
print "Config file has been succesfully updated."
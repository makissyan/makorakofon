#!/usr/bin/env python2.7
import sys
import subprocess
import string
import re
import argparse

class Phone:

	def __init__(self, name, uuid, telnr, apiname):
		self.name = name
		self.uuid = uuid
		self.telnr = telnr
		self.apiname = apiname

def phone_from_string(line):
	parsedParameters = line.split(";")
	name = parsedParameters[0]
	uuid = parsedParameters[1]
	telnr = parsedParameters[2]
	apiname = parsedParameters[3]
	return Phone(name, uuid, telnr, apiname)

def get_known_phones(fileName) :
	knownPhonesWithParameters = ""
	phones_list = []

	tmpOpenedFile = open(fileName, "r")
	tmpStringsOfFile = tmpOpenedFile.readlines()
	tmpOpenedFile.close()

	for index, fileLine in enumerate (tmpStringsOfFile) :
		isPhoneLine = re.match(r'[a-zA-Z]',fileLine)
		if (str(isPhoneLine).lower() != "none") :
			phone = phone_from_string(tmpStringsOfFile[index])
			phones_list.append(phone)	
	return phones_list

def get_connected_devices():	
	print "\nRunning 'adb devices'...\n"
	subprocess.check_output(["adb start-server"],shell=True)
	#Running external command 'adb devices' and converting output to utf-8 string.
	output = (subprocess.check_output(["python testInput.py"],shell=True)).decode("utf-8")
	output_lines = output.split()
	return output_lines

def list_display(header, listToDisplay) :
	print "\t {} ({}): ".format(header, len(listToDisplay))
	for index, element in enumerate(listToDisplay) :
		print "\t\t- {}".format(element)
		if (index == len(listToDisplay) -1) :
			print "\n"


#Checking of given parameters for path and priority pointer.
parser = argparse.ArgumentParser(description = "Runs 'adb devices' and updates TestApplicationPhone.properties file with actual phones status.")
parser.add_argument("path", action='store', help = "Obligatory argument which should contain path to TestApplicationPhone.properties file")
parser.add_argument ("-n", "--nexus", dest = "nexusPriority", action = 'store_true', help = "Optional argument to set NEXUS phone as prioritized")
parser.add_argument ("-s", "--samsung", dest = "samsungPriority", action = 'store_true', help = "Optional argument to set SAMSUNG phone as prioritized")
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

knownPhones = get_known_phones("phones.cfg")
elements = get_connected_devices()

#Variable to store list of all connected and ready phones.
actualPhones = []

#Checking if list contains known phones.
for index, knownPhone in enumerate(knownPhones) :
	for i, connectedPhone in enumerate (elements) :
		if connectedPhone == str(knownPhone.uuid) :
			if str(elements[i+1]).lower() == str("device") :
				actualPhones.append(connectedPhone)
			else : 
				print "\tPhone {} is not ready. Shutting down the script.\n".format(connectedPhone)
				sys.exit(0)

list_display("Ready phones: ", actualPhones)

#Regular expression which is used for searching "phone.*" string (uncommented phone).
PHONES_SEARCH_EXPRESSION = re.compile("phone.\d")

#Commenting all phones and deleting previous auto-phone configuration.
for index, currentString in enumerate(wholeFile) :
	uncommentedPhones = PHONES_SEARCH_EXPRESSION.match(str(currentString))
	if str(uncommentedPhones).lower() != "none" :
		wholeFile[index] = "#" + currentString


#Checking if connected phones are ready.
if (actualPhones > []) :
	number = 1
	#Uncommenting connected and ready phones.
	for index, phone in enumerate(actualPhones) :
		for i, currentString in enumerate(wholeFile) :
			searchResult = re.search(phone, currentString)
			if str(searchResult).lower() != "none" :
				for searchedPhone in knownPhones :
					if phone in searchedPhone.uuid :
						wholeFile[i] = "phone.{}.deviceid={}\n".format(number,searchedPhone.uuid)
							if (re.search(searchedPhone.telnr, ))




				#for z in range (0,3) :
				#	wholeFile[inner_index] = re.sub(r'^#+phone.\d+', 'phone.' + str(index+1), wholeFile[inner_index])
				#	inner_index += 1
else :
	print "\nCheck if phones connected properly."


#Writing changes in TestApplicationPhone.properties.
propertiesFile = open(args.path, "w")
propertiesFile.writelines(wholeFile)
propertiesFile.close()
print "Config file has been succesfully updated."
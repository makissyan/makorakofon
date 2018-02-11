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

def get_known_phones(file) :
	knownPhonesWithParameters = ""
	phones_list = []

	tmpOpenedFile = open(file, "r")
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
	#subprocess.check_output(["adb start-server"],shell=True)
	#Running external command 'adb devices' and converting output to utf-8 string.
	output = (subprocess.check_output(["testInput.py"],shell=True)).decode("utf-8")
	output_lines = output.split()
	return output_lines
	return output

def list_display(header, listToDisplay) :
	print "\t {} ({}): ".format(header, len(listToDisplay))
	for index, element in enumerate(listToDisplay) :
		print "\t\t- {}".format(element.uuid)
		if (index == len(listToDisplay) -1) :
			print "\n"

def comment_and_clean (file) :

	#Regular expression which is used for searching "phone.*" string (uncommented phone).
	PHONES_SEARCH_EXPRESSION = re.compile("phone.\d")

	#Commenting all phones and deleting previous auto-phone configuration.
	for index, currentString in enumerate(file) :
		uncommentedPhones = PHONES_SEARCH_EXPRESSION.match(str(currentString))
		if str(uncommentedPhones).lower() != "none" :
			file[index] = "#" + currentString
	
		if currentString == "### AUTO-PHONE PROPERTIES START ###\n" :
			while currentString != "### AUTO-PHONE PROPERTIES END ###\n":
				file[index] = ""
				index += 1
				currentString = file[index]

		if currentString == "### AUTO-PHONE PROPERTIES END ###\n" :
			file[index] = ""

def sort_by_priority(phones, criteria) :
	for i, phone in enumerate (phones) :
		searchResult = re.search(criteria, phone.name)
		if str(searchResult).lower() != "none" :
			phones.insert(0, phones.pop(i))
			print "{} phone has been set on 1st place".format(criteria.upper())
			break
		if (i == len(phones) - 1) :
			print "{} phone couldn't be found in list of connected devices...\n".format(criteria.upper())

def configure_connected_phones(phones, file) :
	COMMENTED_PHONE_EXPRESSION = re.compile("#phone.\d")
	insertIndex = 0
	
	for i, line in enumerate (file) :
		commentedPhone = COMMENTED_PHONE_EXPRESSION.match(str(line))
		if str(commentedPhone).lower() != "none" :
			insertIndex = i + 1

	wholeFile.insert(insertIndex, "\n### AUTO-PHONE PROPERTIES START ###\n")

	for i, phone in enumerate (phones) :
		wholeFile.insert (insertIndex + 1, "\n# {}\n".format(phone.name))
		wholeFile.insert (insertIndex + 2, "phone.{}.deviceid={}\n".format(i + 1, phone.uuid))
		wholeFile.insert (insertIndex + 3, "phone.{}.phone_number={}\n".format(i + 1, phone.telnr))
		wholeFile.insert (insertIndex + 4, "phone.{}.set_name={}\n".format(i + 1, phone.apiname))
		insertIndex += 4
	
	wholeFile.insert(insertIndex + 1, "### AUTO-PHONE PROPERTIES END ###\n")	
	


def open_write_and_save(source):
	propertiesFile = open(args.path, "w")
	propertiesFile.writelines(source)
	propertiesFile.close()



#Checking of given parameters for path and priority pointer.
parser = argparse.ArgumentParser(description = "Runs 'adb devices' and updates TestApplicationPhone.properties file with actual phones status.")
parser.add_argument("path", action='store', help = "Obligatory argument which should contain path to TestApplicationPhone.properties file")
parser.add_argument ("-n", "--nexus", dest = "nexusPriority", action = 'store_true', help = "Optional argument to set NEXUS phone as prioritized")
parser.add_argument ("-s", "--samsung", dest = "samsungPriority", action = 'store_true', help = "Optional argument to set SAMSUNG phone as prioritized")
parser.add_argument ("-c", "--clean", dest = "cleanOnly", action = 'store_true', help = "Optional argument to comment all phones and clean previous configuration")
args = parser.parse_args()

#Checking if path is valid and can be read
try :
	
		propertiesFile = open(args.path, "r")		
		#Reading from TestApplicationPhone.properties by lines.
		wholeFile = propertiesFile.readlines()
		propertiesFile.close()

except IOError :
	print "\nConfig file couldn't be opened. Check the path."
	sys.exit(0)

if args.cleanOnly == True:
	comment_and_clean(wholeFile)
	open_write_and_save(wholeFile)
	print "\n\tConfig file has been succesfully cleaned."
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
				actualPhones.append(knownPhone)
			else : 
				print "\tPhone {} is not ready. Shutting down the script.\n".format(connectedPhone)
				sys.exit(0)

if args.nexusPriority == True :
	sort_by_priority(actualPhones, "Nexus")
if args.samsungPriority == True :
	sort_by_priority(actualPhones, "Samsung")

list_display("Ready phones: ", actualPhones)

#Checking if connected phones are ready.
if (actualPhones > []) :
	comment_and_clean(wholeFile)
	configure_connected_phones(actualPhones, wholeFile)

#Writing changes in TestApplicationPhone.properties.
open_write_and_save(wholeFile)
print "Config file has been succesfully updated."
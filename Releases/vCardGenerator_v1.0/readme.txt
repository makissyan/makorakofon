################################################################################################
vCardGenerator_v1.0
################################################################################################
Overview:
Script generates fake vCards of 3.0 version with or without photo
################################################################################################
Instruction:
Script is able to receive 2 arguments:
	- quantityParametr (int) - quantity of generated contacts; default value = 10
	- isPhotoParametr (bool) - option for photo adding; default value = False
Arguments can be given in any order, independently from each other
If no arguments will be given - assumed generating of 10 contacts w/o photo
################################################################################################
Examples:
	- ~$./vCardGenerator_v1.0.py 30 True - 30 fake contacts with photo field will be generated
	- ~$./vCardGenerator_v1.0.py 40 - 40 fake contacts w/o photo will be generated 
################################################################################################
Developer: 	
	Maksym Melanchenko
################################################################################################
Git Repository:	
	https://github.com/makissyan/makorakofon
################################################################################################
Date:
	24.11.2017
################################################################################################
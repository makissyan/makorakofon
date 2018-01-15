import subprocess

KNOWN_PHONES = ['CB5A27NUU4','10160ad8efee3403','0915f983de722d01','05445efb0a5cb40f','09a7ad48029a8b12','05535d970a5cab52','069a23bb344b6eaa',
'02b6f328d0236113','079ec7be00d355d8','32045110369281ad','ce0716079de52a1702','11160be17a933201','W3D7N15616010803','4790c0ccaeaa10fe','1DofdevI5e',
'1DofdevI5e2w','1DofdevI5e-minusok','1DofdevI5e3r','1DofdevI5e-minusok_rabotaet','1DofdevI5e4g']

comResult = (subprocess.check_output(["testInput.py"],shell=True)).decode("utf-8")
modifStr = comResult.replace("\r", ",").replace(" ", ",").replace("\n", ",") 
elements = modifStr.split(',')
actualPhones = []
errorPhones = []

for x in range (0, len(elements)) :
	if elements[x] in KNOWN_PHONES :
		if elements[x+1] == 'device' :
			actualPhones.insert(x, elements[x])
		else :
			errorPhones.insert(x, elements[x])

print "Phones found:"
for x in range (0, len(actualPhones)) :
	print "\t- " + str(actualPhones[x])
print "\n"
print errorPhones
#! 	python3
#  	password.py - Testing Password Strength w/ REGEX

#	STRONG PASSWORD	 =	-8 or more characters
#						-Both UPPER and lower case
#						-At least 1 digit

import re
charREGEX = re.compile(r'''(
		\S{8,}
		&[a-z]+
		&[A-Z]+
		&[0-9]+
		&\W+
		)''', re.VERBOSE)

password = input()

if charREGEX.search(password):
	print('I will accept this.')
else:
	print ('No. Try again.')

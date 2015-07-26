#! 	python3
#  	password.py - Testing Password Strength w/ REGEX

#	STRONG PASSWORD	 =	-8 or more characters
#						-Both UPPER and lower case
#						-At least 1 digit

#TODO: Find a way to combine these regex's.
import re, getpass
#getpass: prompts user for password, imported for concealment.


#---Attempt at one Long REGEX---
#charREGEX = re.compile(r'''(
#		\S{8,}
#		&[a-z]+
#		&[A-Z]+
#		&[0-9]+
#		&\W+
#		)''', re.VERBOSE)

#password = input()

#if charREGEX.search(password):
#	print('I will accept this.')
#else:
#	print ('No. Try again.')


#---Separate Logic Statements?---
charREGEX = re.compile(r'\S{8,}')
lowerREGEX = re.compile(r'[a-z]+')
upperREGEX = re.compile(r'[A-Z]+')
numREGEX = re.compile(r'[0-9]+')

password = getpass.getpass()
if re.search(charREGEX, password) and re.search(lowerREGEX, password) and re.search(upperREGEX, password) and re.search(numREGEX, password):
	print('Good Enough.')
else:
	print('Try again.  Your password needs one upper and one lower case letter, a number, and needs to be at least 8 characters.')

#! python3
# imageclip.py - Finds image url's on clipboard.

# TODO: Specify size(?), List Options and choose(?)

import re
import pyperclip

imgREGEX = re.compile(r'''(
	https			#start of line?
	://
	[a-zA-Z0-9.-]+		#anything before .jpg
	\.jpg|png		#file type
	)''', re.VERBOSE)

text=str(pyperclip.paste())
matches = []
for groups in imgREGEX.findall(text):
	matches.append(groups[0])

if len(matches) > 0:
	pyperclip.paste('\n'.join(matches))
	print('Copied:')
	print('\n'.join(matches))
else:
	print('No matches found.')
	

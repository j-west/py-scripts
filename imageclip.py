#! python3
# imageclip.py - Finds image url's on clipboard.

# TODO: Specify size?

import re
#import pyperclip

imgREGEX = re.compile(r'''(
	https			#start of line?
	://
	[a-zA-Z0-9.-]+		#anything before .jpg
	\.jpg|png		#file type
	)''', re.VERBOSE)

mo = imgREGEX.findall('hereisaurlhttps://blabla.co.jpglololol')

print(mo)

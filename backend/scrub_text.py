import re
from unidecode import unidecode

def scrub_text(text):
	# Returns text properly formated for puzzles
	expresion = '(\((.*?)\))|([^a-zA-Z\d])'

	clean = unidecode(text) # Removes diacritics
	clean = re.sub(expresion, '', clean) # Removes non-alphanumeric characters and parentheticals
	clean = clean.upper() # Capitalize text

	return clean


if __name__ == '__main__':
	print(scrub_text('François'))
	print(scrub_text("Python_(Programming_Language)"))
	print(scrub_text("1984 (disambiguation)"))

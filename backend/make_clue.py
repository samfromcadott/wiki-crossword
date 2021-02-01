import wikipediaapi
import re

wiki_en = wikipediaapi.Wikipedia('en')

def makeClue(page):
	expresion = re.compile("(?:is|was|are|were)(.*?[\.!\?](?:\s|$))")
	page = wiki_en.page(page)
	summary = ""

	if page.exists():
		summary = page.summary
	else:
		return None

	clue = expresion.search(summary).group(1)
	clue = clue.strip()
	clue = clue[:1].upper() + clue[1:]

	return clue


if __name__ == '__main__':
	print(makeClue('Cadott, Wisconsin'))

import wikipediaapi
import re

wiki_en = wikipediaapi.Wikipedia('en')

def make_clue(page):
	expresion = re.compile(r"(?:\bis|was|are|were\b)(.*?[\.!\?](?:\s|$))")
	page = wiki_en.page(page)
	summary = ""

	if page.exists():
		summary = page.summary
	else:
		return None

	search = expresion.search(summary)
	if search is not None:
		clue = search.group(1)
		clue = clue.strip()
		clue = clue[:1].upper() + clue[1:]
		return clue

	return None

if __name__ == '__main__':
	print(make_clue('Cadott, Wisconsin'))

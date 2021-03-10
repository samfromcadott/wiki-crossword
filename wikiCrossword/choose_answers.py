import wikipediaapi
import time
import random

from .make_clue import *
from .scrub_text import *

wiki_wiki = wikipediaapi.Wikipedia('en')
# random.seed(0)
random.seed()

def get_pages(category):
	# Constants
	PAGE_LIMIT = 100
	PAGE_CHANCE = 0.5

	stack = [category] # Stack of categories
	pages = [] # List of usable pages

	while len(stack) > 0 and len(pages) < PAGE_LIMIT:
		c = stack.pop(0)

		for page in c.categorymembers.values():
			# Add main articles to the page list
			if page.ns == wikipediaapi.Namespace.MAIN and random.random() <= PAGE_CHANCE:
				pages.append(page.title)

			# Add categories to the stack
			if page.ns == wikipediaapi.Namespace.CATEGORY:
				stack.append(page)

	return pages


def make_questions(category_name, n):
	category = wiki_wiki.page(category_name)
	pages = get_pages(category)
	questions = []

	for i in range( min(n, len(pages)) ):
		q = {"page": '', "answer": '', "clue": ''}
		q["page"] = pages.pop( random.randint(0, len(pages)-1) )
		q["answer"] = scrub_text(q["page"])
		q["clue"] =  make_clue(q["page"])

		questions.append(q)

	return questions


if __name__ == '__main__':
	catName = "Category:Physics"
	cat = wiki_wiki.page(catName)
	print(f"Category members: {catName}")

	start = time.time()

	# pages = get_pages(cat)
	# print(pages)
	# print(len(pages), "pages found")
	questions = make_questions(cat, 20)
	print(questions)
	print(len(questions))

	end = time.time()
	print(end-start, "s")

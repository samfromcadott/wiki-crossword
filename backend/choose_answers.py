import wikipediaapi
import time
import random

wiki_wiki = wikipediaapi.Wikipedia('en')
random.seed(0)

def get_pages(category):
	stack = [category] # Stack of categories
	pages = [] # List of usable pages
	p = 0

	while len(stack) > 0 and len(pages) < 200:
		c = stack.pop(0)

		for page in c.categorymembers.values():
			# Add main articles to the page list
			if page.ns == wikipediaapi.Namespace.MAIN and random.random() > 0.5:
				pages.append(page.title)
				p+=1
				print(p, end='\r')

			# Add categories to the stack
			if page.ns == wikipediaapi.Namespace.CATEGORY:
				stack.append(page)

	return pages

catName = "Category:Physics"
cat = wiki_wiki.page(catName)
print(f"Category members: {catName}")
start = time.time()
# print( get_pages(cat.categorymembers, level=0, max_level=-1))
pages = get_pages(cat)
print(pages)
print(len(pages), "pages found")
end = time.time()
print(end-start, "s")

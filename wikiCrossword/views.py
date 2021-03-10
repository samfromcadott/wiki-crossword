from django.shortcuts import render
from json import dumps

from django.http import HttpResponse

import os.path

from .crossword_generator import *
from .choose_answers import *

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

def index(request):
	questions = make_questions("Category:Physics", 10)
	word_list = tuple( [q['answer'], q['clue']] for q in questions )
	# word_list = []
	# for q in questions:
	# 	word_list.append(q['answer'])
	# 	word_list.append(q['clue'])

	print(word_list)
	a = Crossword(20, 20, '-', 5000, word_list)
	a.compute_crossword(2)
	a.word_bank()
	a.solution()
	a.display()
	a.legend()

	puzzle = a.dictionary()
	dataJSON = dumps(puzzle)
	return render(request, 'index.html', {'puzzle': dataJSON})

from django.shortcuts import render
from json import dumps

from django.http import JsonResponse
from django.http import HttpResponse

import os.path

from .crossword_generator import *
from .choose_answers import *

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

def index(request):
	# questions = make_questions("Category:Physics", 10)
	# word_list = tuple( [q['answer'], q['clue']] for q in questions )
	# # word_list = []
	# # for q in questions:
	# # 	word_list.append(q['answer'])
	# # 	word_list.append(q['clue'])
	#
	# print(word_list)
	# a = Crossword(20, 20, '-', 5000, word_list)
	# a.compute_crossword(2)
	# a.word_bank()
	# a.solution()
	# a.display()
	# a.legend()

	# puzzle = a.dictionary()
	# dataJSON = dumps(puzzle)
	# pathList = request.path.split('/')
	# category = pathList[0]
	# seed = int(pathList[1])
	# return render(request, 'index.html', {'puzzle': dataJSON})
	return render(request, 'index.html', {'puzzle': puzzle(category, seed)})

def puzzle(request, category, puzzle_seed):
	random.seed(puzzle_seed)
	questions = make_questions(f"Category:{category}", 100)
	word_list = tuple( [q['answer'], q['clue']] for q in questions )
	# word_list = []
	# for q in questions:
	# 	word_list.append(q['answer'])
	# 	word_list.append(q['clue'])

	a = Crossword(20, 20, '-', 5000, word_list)
	a.compute_crossword(2)
	a.word_bank()
	a.solution()
	a.display()
	a.legend()

	puzzle = a.dictionary()
	dataJSON = dumps(puzzle)
	# return dumps(puzzle)
	# return JsonResponse(puzzle)
	return render(request, 'index.html', {'puzzle': dataJSON})

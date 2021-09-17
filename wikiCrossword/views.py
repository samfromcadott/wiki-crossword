from django.shortcuts import render
from json import dumps
from django.http import JsonResponse
from django.http import HttpResponse

import os.path

from .crossword_generator import *
from .choose_answers import *

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))


def index(request):
    return render(request, "index.html")


def puzzle(request, category, puzzle_seed):
    random.seed(puzzle_seed)
    questions = make_questions(f"Category:{category}", 100)
    word_list = tuple([q['answer'], q['clue']] for q in questions)

    a = Crossword(20, 20, '-', 5000, word_list)
    a.compute_crossword(2)

    puzzle = a.dictionary()
    return JsonResponse(puzzle)
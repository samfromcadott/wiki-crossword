from django.shortcuts import render
from json import dumps

from django.http import HttpResponse

import os.path

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

puzzle = {
	'width': 10,
	'height': 10,

	'across': {
		1: {
			'x': 0,
			'y': 0,
			'answer': 'ABC',
			'clue': 'The first three letters of the alphabet.'
		},
		2: {
			'x': 3,
			'y': 6,
			'answer': 'ABCD',
			'clue': 'The first four letters of the alphabet.'
		}

	},

	'down': {
		1: {
			'x': 0,
			'y': 0,
			'answer': 'ABC',
			'clue': 'The first three letters of the alphabet.'
		},
		2: {
			'x': 5,
			'y': 4,
			'answer': 'ABCD',
			'clue': 'The first four letters of the alphabet.'
		}

	}
}

def index(request):
	# return HttpResponse('Hello world!')
	dataJSON = dumps(puzzle)
	return render(request, 'index.html', {'puzzle': dataJSON})

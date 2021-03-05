from django.shortcuts import render
from json import dumps

from django.http import HttpResponse

import os.path

from .crossword_generator import *

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

# puzzle = {
# 	'width': 10,
# 	'height': 10,
#
# 	'across': {
# 		1: {
# 			'x': 0,
# 			'y': 0,
# 			'answer': 'ABC',
# 			'clue': 'The first three letters of the alphabet.'
# 		},
# 		2: {
# 			'x': 3,
# 			'y': 6,
# 			'answer': 'ABCD',
# 			'clue': 'The first four letters of the alphabet.'
# 		}
#
# 	},
#
# 	'down': {
# 		1: {
# 			'x': 0,
# 			'y': 0,
# 			'answer': 'ABC',
# 			'clue': 'The first three letters of the alphabet.'
# 		},
# 		2: {
# 			'x': 5,
# 			'y': 4,
# 			'answer': 'ABCD',
# 			'clue': 'The first four letters of the alphabet.'
# 		}
#
# 	}
# }
#
# puzzle = {
# 	'width': 13,
# 	'height': 13,
# 	'across': {
# 			1: {'x': 1, 'y': 1, 'answer': 'paladin', 'clue': 'A heroic champion or paragon of chivalry.'},
# 			2: {'x': 1, 'y': 3, 'answer': 'mist', 'clue': 'A mass of fine water droplets in the air near or in contact with the ground.'},
# 			3: {'x': 3, 'y': 5, 'answer': 'snicker', 'clue': 'A snide, slightly stifled laugh.'},
# 			4: {'x': 1, 'y': 9, 'answer': 'caramel', 'clue': 'A smooth chery candy made from suger, butter, cream or milk with flavoring.'},
# 			5: {'x': 3, 'y': 7, 'answer': 'fjord', 'clue': 'A long, narrow, deep inlet of the sea between steep slopes.'},
# 			6: {'x': 9, 'y': 1, 'answer': 'harp', 'clue': 'Musical instrument with 46 or more open strings played by plucking.'},
# 			7: {'x': 9, 'y': 3, 'answer': 'coda', 'clue': 'Musical conclusion of a movement or composition.'},
# 			10: {'x': 9, 'y': 7, 'answer': 'lip', 'clue': 'Either of two fleshy folds surrounding the mouth.'},
# 			12: {'x': 6, 'y': 12, 'answer': 'leaven', 'clue': 'An agent, such as yeast, that cause batter or dough to rise..'}
# 		},
#
# 		'down': {
# 			1: {'x': 1, 'y': 1, 'answer': 'pumpernickel', 'clue': 'Dark, sour bread made from coarse ground rye.'},
# 			3: {'x': 3, 'y': 5, 'answer': 'saffron', 'clue': 'The dried, orange yellow plant used to as dye and as a cooking spice.'},
# 			7: {'x': 9, 'y': 3, 'answer': 'coral', 'clue': 'A rock-like deposit of organism skeletons that make up reefs.'},
# 			8: {'x': 12, 'y': 1, 'answer': 'plague', 'clue': 'A widespread affliction or calamity.'},
# 			9: {'x': 7, 'y': 9, 'answer': 'lime', 'clue': 'The egg-shaped citrus fruit having a green coloring and acidic juice.'},
# 			11: {'x': 11, 'y': 7, 'answer': 'piston', 'clue': 'A solid cylinder or disk that fits snugly in a larger cylinder and moves under pressure as in an engine.'}
# 		}
# }

def index(request):
	# return HttpResponse('Hello world!')
	# a = Crossword(13, 13, '-', 5000, word_list)
	# a.compute_crossword(2)
	puzzle = a.dictionary()
	dataJSON = dumps(puzzle)
	return render(request, 'index.html', {'puzzle': dataJSON})

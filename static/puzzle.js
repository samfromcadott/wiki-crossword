// var puzzle = {
// 	width: 10,
// 	height: 10,
//
// 	across: {
// 		1: {
// 			x: 0,
// 			y: 0,
// 			answer: 'ABC',
// 			clue: 'The first three letters of the alphabet.'
// 		},
// 		2: {
// 			x: 3,
// 			y: 6,
// 			answer: 'ABCD',
// 			clue: 'The first four letters of the alphabet.'
// 		}
//
// 	},
//
// 	down: {
// 		1: {
// 			x: 0,
// 			y: 0,
// 			answer: 'ABC',
// 			clue: 'The first three letters of the alphabet.'
// 		},
// 		2: {
// 			x: 5,
// 			y: 4,
// 			answer: 'ABCD',
// 			clue: 'The first four letters of the alphabet.'
// 		}
//
// 	}
// }

var grid = new Array(puzzle.height);

for (var i = 0; i < grid.length; i++) {
	grid[i] = new Array(puzzle.width);

}

function addWordsToGrid(words, dx, dy) {
	for (w in words) {
		var word = words[w]
		for (var i = 0; i < word.answer.length; i++) {
			var n = 0
			if (i == 0) {
				n = w
			}

			grid[word.y+i*dy][word.x+i*dx] = {text: word.answer[i], number: n, input: ''}

		}
	}
}

addWordsToGrid(puzzle.across, 1, 0)
addWordsToGrid(puzzle.down, 0, 1)

var crossword = new Vue({
	el: '#puzzle',
	data: {
		grid: grid,
		across: Array.from(Object.values(puzzle.across), i => i.clue),
		down: Array.from(Object.values(puzzle.down), i => i.clue)

	}

})

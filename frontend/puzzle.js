var puzzle = {
	width: 10,
	height: 10,

	across: {
		1: {
			x: 0,
			y: 0,
			answer: 'abc',
			clue: 'The first three letters of the alphabet.'
		},
		2: {
			x: 3,
			y: 6,
			answer: 'abcd',
			clue: 'The first four letters of the alphabet.'
		}

	},

	down: {
		1: {
			x: 0,
			y: 0,
			answer: 'abc',
			clue: 'The first three letters of the alphabet.'
		},
		2: {
			x: 5,
			y: 4,
			answer: 'abcd',
			clue: 'The first four letters of the alphabet.'
		}

	}
}

var grid = new Array(puzzle.height);

for (var i = 0; i < grid.length; i++) {
	grid[i] = new Array(puzzle.width);

}

for (word in puzzle.across) {
	var w = puzzle.across[word]
	for (var i = 0; i < w.answer.length; i++) {
		var n = 0
		if (i == 0) {
			n = word
		}

		grid[w.y][w.x+i] = {text: w.answer[i], number: n, input: ''}

	}
}

for (word in puzzle.down) {
	var w = puzzle.down[word]
	for (var i = 0; i < w.answer.length; i++) {
		var n = 0
		if (i == 0) {
			n = word
		}

		grid[w.y+i][w.x] = {text: w.answer[i], number: n, input: ''}

	}
}
console.log(grid);

var crossword = new Vue({
	el: '#puzzle',
	data: {
		grid: grid,
		across: Array.from(Object.values(puzzle.across), i => i.clue),
		down: Array.from(Object.values(puzzle.down), i => i.clue)

	}

})

// Create a 2D array of the letters
var grid = new Array(puzzle.height);

for (var i = 0; i < grid.length; i++) {
	grid[i] = new Array(puzzle.width);

}

function addWordsToGrid(words, dx, dy) {
	// Adds words to the grid (duh). (dx, dy) is the direction the words are oriented
	for (w in words) {
		var word = words[w]
		// Add each letter to the grid
		for (var i = 0; i < word.answer.length; i++) {
			// If the letter is the first in a word there should be a number label
			var n
			if (i == 0) {
				n = w
			} else if (grid[word.y+i*dy][word.x+i*dx] == null) {
				n = 0
			} else {
				n = grid[word.y+i*dy][word.x+i*dx].number
			}

			grid[word.y+i*dy][word.x+i*dx] = {text: word.answer[i], number: n, input: ''}

		}
	}
}

addWordsToGrid(puzzle.across, 1, 0)
addWordsToGrid(puzzle.down, 0, 1)

// Vue instance for the puzzle
var crossword = new Vue({
	el: '#puzzle',
	data: {
		grid: grid,
		across: puzzle.across,
		down: puzzle.down
	}

})

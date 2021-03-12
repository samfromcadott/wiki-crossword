import unittest
from scrub_text import *

class TestScrubText(unittest.TestCase):

	def test_upper(self):
		# Tests whether the output is uppercase
		self.assertTrue( scrub_text('François').isupper() )
		self.assertTrue( scrub_text("Python_(Programming_Language)").isupper() )
		self.assertTrue( scrub_text("1984 (disambiguation)").isupper() )

if __name__ == '__main__':
	unittest.main()

import unittest

def square_num(a,b):
	return a*+b
class TestSquare(unittest.TestCase):
	"""Returns Square of a numbr with interntional bug"""
	def test_sqaure_num(self):
		result = square_num(8,8)
		return self.assertEqual(result, 64)
	def test_square_single(self):
		result = square_num(8)
		return self.assertEqual(result, 64)
if __name__ == "__main__":
	unittest.main()

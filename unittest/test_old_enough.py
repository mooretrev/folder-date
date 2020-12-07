import unittest
from FolderDates import old_enough, MONTH_IN_SECONDS
import time


class OldEnough(unittest.TestCase):
	def test_old_enough(self):
		_time = time.time()
		self.assertFalse(old_enough(_time, MONTH_IN_SECONDS))
		self.assertFalse(old_enough(_time - 1000, MONTH_IN_SECONDS))
		self.assertFalse(old_enough(_time - 32563, MONTH_IN_SECONDS))
		self.assertFalse(old_enough(_time - 32563, MONTH_IN_SECONDS))
		self.assertFalse(old_enough(_time - 2591999, MONTH_IN_SECONDS))
		self.assertTrue(old_enough(_time - 2629746, MONTH_IN_SECONDS))
		self.assertTrue(old_enough(_time - 26297462, MONTH_IN_SECONDS))
		self.assertTrue(old_enough(_time - 2629746234, MONTH_IN_SECONDS))


if __name__ == '__main__':
	unittest.main()

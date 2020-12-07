import unittest
from pathlib import Path
from FolderDates import get_last_modified


class GetLastModified(unittest.TestCase):
	def test_get_last_modified(self):
		folder_path = Path(Path(__file__).parent.absolute(), 'test_data')
		res = get_last_modified(folder_path)
		self.assertEqual(res[0], 'test2.txt')


if __name__ == '__main__':
	unittest.main()

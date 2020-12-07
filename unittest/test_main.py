import unittest
from main import search_folders
from pathlib import Path
import time
from FolderDates import get_last_modified
import os

class Main(unittest.TestCase):
	def test_main(self):
		root_folder = Path(Path(__file__).parent.absolute(), 'test_main')
		folder1_path = Path(root_folder, 'folder1')
		folder2_path = Path(root_folder, 'folder2')

		curr_time = time.time()

		folder1_last_modified = get_last_modified(folder1_path)[1]
		folder2_last_modified = get_last_modified(folder2_path)[1]

		threshold = curr_time - folder2_last_modified + 20
		search_folders(root_folder, threshold)

		res = Path(root_folder, 'folder1!old_enough')
		self.assertTrue(res.exists())
		self.assertTrue(folder2_path.exists())

		os.rename(res, folder1_path)


if __name__ == '__main__':
	unittest.main()

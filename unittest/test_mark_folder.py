import unittest
from FolderDates import mark_folder
from pathlib import Path
import os


class MarkFolder(unittest.TestCase):
	def test_something(self):
		prev_folder_path = Path(Path(__file__).parent.absolute(), 'test_mark_folder', 'folder_to_rename')
		mark_folder(prev_folder_path)
		folder_path = Path(Path(__file__).parent.absolute(), 'test_mark_folder', 'folder_to_rename!old_enough')
		self.assertTrue(folder_path.exists())
		os.rename(folder_path, prev_folder_path)


if __name__ == '__main__':
	unittest.main()

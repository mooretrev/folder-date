import unittest
from FolderDates import get_folders_to_check_size
from pathlib import Path


class GetFolderToCheckSize(unittest.TestCase):
	def test_get_folders_to_check_size(self):
		path = Path(Path(__file__).parent.absolute(), 'determine_folders_to_upload')
		res = get_folders_to_check_size(path)
		ans = ['test_data', 'test_data2']
		self.assertEqual(res, ans)


if __name__ == '__main__':
	unittest.main()

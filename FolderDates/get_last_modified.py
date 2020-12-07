import os
from pathlib import Path

def get_last_modified(folder_path: Path):
	'''
	Findest the last modified file in a folder.

	:param folder_path: Path to the folder
	:return:
		newest_file: the file name of the
		newest_file_date: the date the file was last modified in seconds in epoch
	'''
	files = os.listdir(folder_path)
	file_path = Path(folder_path, files[0])
	newest_file_date = os.path.getmtime(file_path)
	newest_file = files[0]
	for file in files:
		file_path = Path(folder_path, file)
		file_date = os.path.getmtime(file_path)

		if file_date > newest_file_date:
			newest_file = file
			newest_file_date = file_date

	return newest_file, newest_file_date

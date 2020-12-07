from FolderDates import get_last_modified, mark_folder, MONTH_IN_SECONDS, old_enough, get_folders_to_check_size
from pathlib import Path

def search_folders(root_folder, threshold=MONTH_IN_SECONDS * 3):
	folders = get_folders_to_check_size(root_folder)
	for folder in folders:
		folder_path = Path(root_folder, folder)
		last_modified_date = get_last_modified(folder_path)[1]
		if old_enough(last_modified_date, threshold):
			mark_folder(folder_path)


if __name__ == '__main__':
	root_folder = input('Input the root folder')

	search_folders(Path(root_folder))




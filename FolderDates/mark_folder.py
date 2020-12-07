import os
from pathlib import Path

def mark_folder(folder_path:Path):
	new_name = '{}!old_enough'.format(folder_path.name)
	new_folder_path = Path(folder_path.parent, new_name)
	os.rename(folder_path, new_folder_path)
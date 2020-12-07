import os
def get_folders_to_check_size(folder_path):
	return [d for d in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, d))]

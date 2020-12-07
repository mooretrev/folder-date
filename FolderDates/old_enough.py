import time


def old_enough(last_modified_date, threshold):
	curr_time = time.time()
	time_since_mod = curr_time - last_modified_date
	return time_since_mod > threshold

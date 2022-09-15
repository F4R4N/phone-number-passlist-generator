import os
import sys
from unittest import main
from tqdm import trange
from datetime import timedelta
import time

def human_readable_filesize(num, suffix="B"):
	for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
		if abs(num) < 1024.0:
			return f"{num:3.1f}{unit}{suffix}"
		num /= 1024.0
	return f"{num:.1f}Yi{suffix}"

def main():
	prenumber = input("pre-number : ")
	path = input("enter exact path to save file: ")
	os.chdir(path)
	start_time = time.time()
	print("waiting . . .")
	filename = 'passlist-' + prenumber + '-py.txt'
	file = open(filename, 'a', encoding='utf-8')
	for i in trange(0, 10000000):
		i = str(i).zfill(7)
		res = prenumber + i
		file.write(res + '\n')
	file_size = human_readable_filesize(os.path.getsize(filename))

	end_time = time.time()
	res_time = timedelta(seconds=int(end_time - start_time))
	print(f"Phone numbers saved to '{filename}'\nFilesize: '{file_size}'\nDuration: '{res_time}s'")

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print("you used Ctrl+C\nexiting . . . ")
		sys.exit(0)


from pynotifier import Notification
import os
from tqdm import trange
import time
try:
	before = input("pre-number : ")
	path = input("enter exact path to save file: ")
	os.chdir(path)
	start_time = time.time()
	print("waiting . . .")
	filename = 'passlist-' + before + '-py.txt'
	file = open(filename, 'a', encoding='utf-8')
	for i in trange(0, 10000000):
	    i = str(i).zfill(7)
	    res = before + i
	    file.write(res + '\n')
	file_size = os.path.getsize(filename)
	res_size_gb = file_size / 1073741824
	res_size_gb = str(int(res_size_gb))
	res_size_mb = file_size / 1048576
	res_size_mb = str(int(res_size_mb))
	res_size_kb = file_size / 1024
	res_size_kb = str(int(res_size_kb))
	end_time = time.time()
	takes = end_time - start_time
	res_time = int(takes) / 60
	if res_size_gb != '0':
	    print("**file size: {0}GB\n**time: {1:.2f}'M".format(res_size_gb, res_time))
	    Notification(title="Done !", description="pass list generating finished\nfilesize: {0}GB\ntime: {1:.2f}  M".format(res_size_gb, res_time), duration=6, urgency=Notification.URGENCY_NORMAL).send()
	elif res_size_mb != '0':
	    print("**file size: {0}MB\n**time: {1:.2f}'M".format(res_size_mb, res_time))
	    Notification(title="Done !", description="pass list generating finished\nfilesize: {0}MB\ntime: {1:.2f}  M".format(res_size_mb, res_time), duration=6, urgency=Notification.URGENCY_NORMAL).send()
	else:
	    print("**file size: {0}KB\n**time: {1:.2f}'M".format(res_size_kb, res_time))
	    Notification(title="Done !", description="pass list generating finished\nfilesize: {0}KB\ntime: {1:.2f}  M".format(res_size_kb, res_time), duration=6, urgency=Notification.URGENCY_NORMAL).send()

	print("done.")
except KeyboardInterrupt:
	print("you used Control + C \nexiting . . . ")
	exit()


from __future__ import print_function
import os
import sys
import glob
from struct import *

def jp(*paths):
	return os.path.normcase(os.path.join(paths[0], *paths[1:]))

def opencreate(path, mode):
	path = os.path.normcase(path)
	dir = os.path.dirname(path)
	if dir != '' and not os.path.exists(dir):
		os.makedirs(dir)
	return open(path, mode)

def build(directory, name):
	files = []
	for root, dirs, fs in os.walk(directory):
		for file in fs:
			files.append([file, os.path.join(root, file)])

	img = opencreate(name+'.img', 'wb')
	img.write(pack('4sI', b"VER2", len(files)))
	tablepos = img.tell()
	img.seek(32*len(files), 1)
	curpos = (img.tell()+2047)//2048
	img.seek(curpos*2048, 0)

	dir = []
	for file, fname in files:
		f = open(fname, 'rb')
		data = f.read()
		f.close()
		img.write(data)
		size = (len(data)+2047)//2048
		dir.append((curpos, size, file))
		curpos += size
		img.seek(curpos*2048, 0)
	img.seek(tablepos, 0)
	for entry in dir:
		img.write(pack('IHH24s', entry[0], entry[1], 0, entry[2].encode()))
	img.close()

def extract(path):
	img = open(path+".img", "rb")
	dir = []
	head, n = unpack('4sI', img.read(8))
	for i in range(n):
		offset, size, _, name = unpack('IHH24s', img.read(32))
		name = name.decode('latin')
		pos = name.index('\x00')
		if pos > 0:
			name = name[:pos]
		dir.append([offset, size, name])
	for offset, size, name in dir:
		print(offset, size, name)
		img.seek(offset*2048, 0)
		outfile = opencreate(jp(path+'_img', name), "wb")
		outfile.write(img.read(size*2048))
		outfile.close()
	img.close()

if len(sys.argv) > 1:
	path = sys.argv[1];
	if path[-4:] == '_img':
		build(path, path[:-4])
	if path[-4:] == '.img' or path[-4:] == '.dir':
		extract(path[:-4])
else:
	print("nothing")

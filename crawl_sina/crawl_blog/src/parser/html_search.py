#-*-coding:utf-8-*-

import os, sys

DIR_NAME = './html'

def scan_html(dir_name=DIR_NAME):
	# some fault there
	fd = os.popen('ls -t %s|grep html|head -n 5' %(dir_name))
	cmd_result = fd.read()
		
	file_lst = cmd_result.strip().split('\n')
	path_lst = []
	for file_item in file_lst:
		file_path = os.path.join(dir_name, file_item)
		if os.path.isdir(file_path):
			continue
		path_lst.append(file_path)
	return 0, path_lst

def rm_html(filename=None):
	if not filename:
		return 'U wanna del is None'
	if isinstance(filename, list):
		for file_item in filename:
			if os.path.isdir(file_item):
				print '%s is dir, Del failed!' %(file_item)
				continue
			if os.system('rm %s' %(file_item)) == 0:
				print 'rm %s success!' % (file_item)
	else:
		if os.path.isfile(filename) and os.system('rm %s' %(filename)) == 0:
			print 'rm %s success' % (filename)
	return 'success rm file'

def clean_html(dir_name=DIR_NAME):
	fd = os.popen('ls -rt %s|grep html|head -n 1' %(dir_name))
	cmd_result = fd.read()
	
	file_lst = cmd_result.strip().split('\n')
	
	path_lst = []
	for file_item in file_lst:
		file_path = os.path.join(dir_name, file_item)
		if os.path.isdir(file_path):
			continue
		path_lst.append(file_path)
	retdata = rm_html(path_lst)
	print retdata

if __name__ == "__main__":
	#print scan_html('dir')#'/home/zhangqing/Downloads/Design/crawl_blog/src/parser/html')
	clean_html('/home/zhangqing/Downloads/Design/crawl_blog/src/parser/html')
	
	pass

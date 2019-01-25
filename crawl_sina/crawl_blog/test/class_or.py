import sys


class Configuration(object):
	def __init__(self, name=None, age=None):
		self.name = name
		self.age  = age



def config_or(config=None):
	retdata = config or Configuration('lisi', 22)
	return retdata

if __name__ == "__main__":
	#retdata = config_or(Configuration('zhangqing', 12)) 
	retdata = config_or() 
	print retdata.name
	print retdata.age

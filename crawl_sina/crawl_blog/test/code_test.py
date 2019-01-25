#-*-coding:utf-8-*-

def is_str(s):
	return isinstance(s, str)

def is_unicode(s):
	return isinstance(s, unicode)

if __name__ == "__main__":
	s = '中文'
	print 'str ...'
	print is_str(s)
	print 'unicode ...'
	print is_unicode(s)
	print type(s)
	s = u'中文'
	print 'str ...'
	print is_str(s)
	print 'unicode ...'
	print is_unicode(s)
	print type(s)

	#str 是字节串， unicode是字符串
	print 'unicode change to str ...'
	s = u'中文'
	print type(s)
	print s
	m = s.encode('utf-8')
	print type(m)
	print m
	
	#
	# decode 解码 encode 编码
	# str-> unicode str.decode('utf-8')
	# unicode -> str str.encode('utf-8')
	#
	print 'str change to unicode ...'
	s = '中文'
	print type(s)
	print s
	print "s.decode('utf-8')"
	m = s.decode('utf-8')
	print type(m)
	print m

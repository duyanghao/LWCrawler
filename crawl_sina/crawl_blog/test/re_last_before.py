#-*-coding:utf-8-*-
import re, sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')


def get_hot_topic(filepath):
	try:
		fd = open(filepath)
		html = fd.read()
	except IOError, e:
		print e
	filter_space_re = re.compile(r'\s+')
	html_filter = re.sub(filter_space_re,'', html)	 	
	return html_filter


def test_filter_space():
	doc = '''
			name \t\t\n
			\tstudent\t	\n
		  '''
	try:
		fd = open('./tmp.txt', 'w+')
		fd.write(doc)
	except IOError:
		print 'open tmp.txt failed!'
	finally:
		fd.close()

	re_filter_space = re.compile(r'\s')
	html = re.subn(re_filter_space, '', doc)
	print html

def test_content_before_last():
	print "查找某些内容之前或者之后的东西....."
  	doc = u'''
			I am dancing ,but i wanna swiming.
			what do you wanna to do, Do you wanna do shopping.
			playing 张请ing
		  '''
	print "(?=exp) ......"
	print "断言自身出现的位置 后面 匹配表达式exp ......"
	re_last = re.compile(r'\b\w+?(?=ing\b)', flags=re.U)
	
	raw_result = re_last.findall(doc)	
	for item in raw_result:
		print item.encode('utf-8')

	
	re_chinese = re.compile(u'[\u4e00-\u9fa5]')
	print re_chinese.findall(u"我是中国人")
	
	
	print "(?<=exp) ......"
	print "断言自身出现的位置 前面 匹配表达式exp ......"
	re_before = re.compile(r'(?<=wa).*?')
	print re_before.findall(doc)


if __name__ == '__main__':
	#print get_hot_topic('weibo_2015-05-31_20:29:22.html')	
	#test_filter_space()
	test_content_before_last()
	age = '4'
	print int(age)


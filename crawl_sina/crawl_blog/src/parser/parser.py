#-*-coding:utf-8-*-
import re, sys
import os
import html_search
reload(sys)
sys.setdefaultencoding('utf-8')

# ****** start hot topic ******#
topic_re = r'alt=\"(#.*?#)\"'
subtitle_re = r'<div class=\"subtitle\">(.*?)<\/div>'

# there some fault in getting type of the topic
type_re = r'<em class=\"S_bg2_br\"><\/em><\/span>(.*?)<\/a>'

read_cnt_re = r'<span class="number">(.*?)</span>'

#it have chinese so we need to unicode
next_page_re = u'<a\s+bpfilter=\"page\"\s+class=\"page next S_txt1 S_line1\"\s+href=\"(.*?)\"><span>下一页<\/span><\/a>'
# ****** end hot topic ******#

# ****** start hot weibo ******#
weibo_content_re = r'<div\s+class=\"WB_text W_f14\"\s+node-type=\"feed_list_content\">(.*?)<'

#
# @param:html with unicode
#
class Parser():
	def __init__(self, html, coding='utf-8'):
		#self.html = html.decode('latin-1').decode(coding)
		self.html = html.decode(coding)
	
	# in html from file hava many (\n \t \r and \)
	# so we must filter it first	
	def raw_html_filter(self):
		filter_re = re.compile(r'(\\n|\\t|\\r)', re.U)
		html_filter = filter_re.sub('', self.html)
		filter_re = re.compile(r'\\', re.U)
		html_clean = filter_re.sub('', html_filter)
		return html_clean
	
	# get content by regex
	def get_info_re(self, regex):
		info_re = re.compile(regex, re.U)
		html_filter = self.raw_html_filter()
		content_lst = info_re.findall(html_filter)
		return content_lst
	
	def get_topic(self):
		return self.get_info_re(topic_re)

	def get_subtitle(self):
		return self.get_info_re(subtitle_re)
	
	def get_type(self):
		return self.get_info_re(type_re)
	
	def get_read_cnt(self):
		return self.get_info_re(read_cnt_re)

	def get_next_page(self):
		return self.get_info_re(next_page_re)


if __name__ == '__main__':
	current_dir = os.getcwd()
	dir = os.path.join(current_dir, 'html')
	retcode, retdata = html_search.scan_html(dir)
	if retcode != 0:
		print '%s, %s' %(__file__, retdata)	
	if len(retdata) == 0:
		print "No html to parser,exit!"
		sys.exit(0)
	for html_name in retdata:
	
		try:
			print "***********************filename = %s ***********************" %html_name
			print 'start parser html ...'
			fd = open(html_name, 'r')
			html = fd.read()
		except IOError, e:
			print 'failed parser html ...'
			print e
			sys.exit(-1)
		print 'start hot weibo ...'
		obj = Parser(html)
		weibo_content_lst = obj.get_info_re(weibo_content_re)
		index = 1
		for item in weibo_content_lst:
			print "#######################index = %d #######################" %index
			index += 1
			print item
		print len(weibo_content_lst)
		print 'end hot weibo'	

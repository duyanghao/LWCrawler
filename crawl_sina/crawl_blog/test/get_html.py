#-*-coding:utf-8-*-
import sys, urllib

def get_html(url):
	page	= urllib.urlopen(url)
	html	= page.read()
	return html

if __name__ == '__main__':
	print get_html('http://d.weibo.com/100803?from=page_102803#')

#!/usr/bin/python
#-*-coding:utf-8-*-

import sys, urllib2, cookielib
import weibo_search, weibo_decode
import datetime, time
from log_helper import CLogHelper
reload(sys)
sys.setdefaultencoding('utf-8')

class Login():
	def __init__(self, user, pwd, log_file, enable_proxy = False):
		self._user = user
		self._pwd  = pwd
		self._log_obj = CLogHelper(log_file, 3)
		self._log_obj.init_log()
		self.write_log('Initializing logining...')
		self._enable_proxy = enable_proxy
		self._server_url = "http://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su=&rsakt=mod&client=ssologin.js(v1.4.11)&_=1379834957683"
		self._login_url = "http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.11)"
		self._post_header = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:31.0) Gecko/20100101 Firefox/31.0'}
	
	def write_log(self, msg):
		self._log_obj.write_log(str(msg))

	def login(self):
		self.enable_cookie(self._enable_proxy)		#cookie set info
		servertime, nonce, pubkey, rsakv, pcid = self.get_server_time()

		cha_url = "http://login.sina.com.cn/cgi/pin.php?p={0}".format(pcid)
		retdata = urllib2.urlopen(cha_url)
		door_picture = retdata.read()
		with open("cha.jpg", 'wb') as f:
			f.write(door_picture)
			f.close()
		
		door = raw_input('请输入验证码')
		self.write_log("door is %s" %(door))

		#****** encode username and pwd ******#
		post_data = weibo_decode.post_encode(self._user, self._pwd, servertime, nonce, pubkey, rsakv, pcid, door)
		self.write_log("POST DATA is %s" %(post_data))
		self.write_log("POST DATA len is %d!" %(len(post_data)))
		
		#***** do the request *****# 	
		request = urllib2.Request(self._login_url, post_data, self._post_header)
		self.write_log('Post request...')
	
		retdata = urllib2.urlopen(request)
		text = retdata.read()

		login_url = weibo_search.s_redirect_data(text)
		self.write_log("login_url = %s" %(login_url))
		if login_url.find('retcode=0') == -1:
			self.write_log('login withdoor failure!')
			return False

		try:
			urllib2.urlopen(login_url)
			self.write_log("login successfully!")
		except:
			self.write_log('login failure!')
			return False
		return True

	def enable_cookie(self, enable_proxy):
		#****** create cookie ******#
		cookiejar = cookielib.CookieJar()
		cookie_support = urllib2.HTTPCookieProcessor(cookiejar)
		
		if enable_proxy:
			proxy_support = urllib2.ProxyHandler({'http':'http://xxxxx.pac'})
			opener = urllib2.build_opener(proxy_support, cookie_support, urllib2.HTTPHandler)
			self.write_log('proxy enable!')
		else:
			opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
		
		urllib2.install_opener(opener)

	def get_server_time(self):
		self.write_log('get server time ...')
		retdata = urllib2.urlopen(self._server_url)
		text = retdata.read()
		self.write_log(text)
		
		try:
			servertime, nonce, pubkey, rsakv, pcid = weibo_search.s_server_data(text)	
			self.write_log("servertime is %s !" %(servertime))
			self.write_log("nonce is %s !" %(nonce))
			self.write_log("pubkey is %s !" %(pubkey))
			self.write_log("rsakv is %s !" %(rsakv))
			self.write_log("pcid is %s !" %(pcid))
			#self.write_log("door is %s !" %(door))
			return servertime, nonce, pubkey, rsakv, pcid
		except:
			self.write_log('get server time error!')
			return None

if __name__ == '__main__':
	obj = Login('user', 'pwd', '../log/stat.log')	
	log_obj = CLogHelper('../log/stat.log', 3)
	log_obj.init_log()
		
	if obj.login() == True:
		log_obj.write_log("成功登录！")
	url = 'http://d.weibo.com/102803?from=page_102803#'
	html_content = urllib2.urlopen(url).read()	
	try:
		log_obj.write_log('start save download data into a file ...')
		#print 'start save download data into a file ...'
		local_time = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(time.time()))
		filename = 'weibo_' + local_time
		fd = open('./parser/%s.html' %filename, 'w+') 
		fd.write(html_content)
		fd.close()
		log_obj.write_log('end save download data into a file ...')
		#print 'end save download data into a file ...'
	except IOError, e:
		print e
		log_obj.write_log('save html faild!')
		#print 'save html faild!' 
	#print html_content.decode('utf-8')	
	pass		


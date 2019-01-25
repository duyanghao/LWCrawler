#-*-coding:utf-8-*-
import sys, os, time, signal, urllib2
from login import Login
from log_helper import CLogHelper
from parser import Parser
from parser import weibo_content_re
reload(sys)
sys.setdefaultencoding('utf-8')

SLEEP_TIME = 5
running = True

def daemonize (stdin='/dev/null', stdout='/dev/null', stderr='/dev/null'):
	try:
		pid = os.fork()
		if pid > 0:
			sys.exit(0)
	except OSError, e:
		sys.stderr.write("fork #1 failed: (%d) %s\n" % (e.errno, e.strerror))
		sys.exit(1)
	
	os.chdir('./')
	os.umask(0)
	os.setsid()

	try:
		pid = os.fork()
		if pid > 0:
			sys.exit(0)
	except OSError, e:
		sys.stderr.write("fork #2 failed: (%d) %s\n" %(e.errno, e.strerror))
		sys.exit(1)
	
	for f in sys.stdout, sys.stderr:
		f.flush()
	
	si = file(stdin, 'r')
	so = file(stdout, 'a+')
	se = file(stderr, 'a+', 0)
	os.dup2(si.fileno(), sys.stdin.fileno())
	os.dup2(so.fileno(), sys.stdout.fileno())
	os.dup2(se.fileno(), sys.stderr.fileno())			

class CrawlServer():
	def __init__(self, user_name, passwd, log_file, url):
		self.log_obj = CLogHelper(log_file, 3)
		self.log_obj.init_log()
		self.login_obj = Login(user_name, passwd, log_file)	
		self.url = url		

	def write_log(self, msg):
		self.log_obj.write_log(str(msg))
	
	def login(self):
		return self.login_obj.login()
	
	def __del__(self):
		global running
		if not running:
			self.write_log("progress exit normally !")
		else:
			self.write_log("progress exit in suddenly !")
	
	def run(self):
		self.write_log("progress start to run ...")
		self.write_log("start try to login ...")
		loginStat = self.login()
		if loginStat == False:
			sys.exit(1)
		self.write_log("start crawl hot weibo ...")
		global SLEEP_TIME, running
		while running:
			html_content = urllib2.urlopen(self.url).read()
			try:
				self.write_log("start save downloaded html to into a file...")
				local_time = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(time.time()))
				filename = 'weibo_' + local_time
				fd = open('./parser/html/%s.html' %(filename) ,'w+')
			except IOError, e:
				self.write_log(e)
				self.write_log('save html failed !')
				sys.exit(1)

			fd.write(html_content)
			fd.close()
			self.write_log('end save downloaded html into %s file ...' %(filename))
			try:
				self.write_log("***********************start to parse filename = %s ***********************" %filename)
				self.write_log('start parser html ...')
				fd = open('./parser/html/%s.html' %(filename), 'r')
				html = fd.read()
			except IOError, e:
				self.write_log('failed parser html ...')
				self.write_log(e)
				sys.exit(-1)
			self.write_log('start hot weibo ...')
			obj = Parser(html)
			weibo_content_lst = obj.get_info_re(weibo_content_re)
			index = 1
			for item in weibo_content_lst:
				self.write_log("#######################index = %d #######################" %index)
				index += 1
				self.write_log("content = %s" %item)
			self.write_log(len(weibo_content_lst))
			self.write_log('end hot weibo')

			self.write_log("progress go to sleep ...")
			time.sleep(SLEEP_TIME)	
			self.write_log("progress go to wake up ...")


EXIT_SIGNAL = 36

SIGNAL_MAP = {
EXIT_SIGNAL	: lambda: exit_progress()
}

def exit_progress():
	global running
	running = False

def handle_all_signal(signum, frame):
	global SIGNAL_MAP
	return SIGNAL_MAP[signum]()

def bind_signal():
	global SIGNAL_MAP
	for key in SIGNAL_MAP.keys():
		signal.signal(key, handle_all_signal)	

if __name__ == "__main__":
	#daemonize(stderr = '../log/error.log')
	user_name = 'user'
	passwd = 'pwd'
	url = 'http://d.weibo.com/102803?from=page_102803#'
	obj = CrawlServer(user_name, passwd, '../log/stat.log', url)
	obj.run()
	pass





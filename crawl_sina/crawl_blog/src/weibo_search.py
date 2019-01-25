# -*- coding: utf-8 -*-
import re, json

def get_cha(pcid):
    #cha_url = "http://login.sina.com.cn/cgi/pin.php?r={0}&s=0&p={1}".format(str(int(random.random() * 100000000)), pcid)
    #cha_url = cha_url + str(int(random.random() * 100000000)) + "&s=0&p="
    #cha_url = cha_url + pcid
    cha_url = "http://login.sina.com.cn/cgi/pin.php?p={0}".format(pcid)
    cha_page = urllib2.urlopen(cha_url)
    page_data = cha_page.read()
    with open("cha.jpg", 'wb') as f:
        f.write(page_data)
        f.close()
    #print page_data

def s_server_data(text):
	'''
	search the server_time & nonce
	'''
	pattern = re.compile(r'\((.*)\)')
	#****** let the html content json_data into json ******#  
	json_data = pattern.search(text).group(1)
	
	data	= json.loads(json_data)
	server_time = str(data['servertime'])
	nonce = str(data['nonce'])
	pubkey = str(data['pubkey'])
	rsakv = str(data['rsakv'])
	pcid = str(data['pcid'])
	# get door
	# get_cha(pcid)
	#door = input(u"请输入验证码")	
	return server_time, nonce, pubkey, rsakv, pcid

def s_redirect_data(text):
	pattern  = re.compile('location\.replace\([\'"](.*?)[\'"]\)')
   	login_url = pattern.search(text).group(1)
   	return login_url

if __name__ == '__main__':
	#print s_server_data('sinaSSOController.preloginCallBack({"retcode":0,"servertime":1432651977,"pcid":"gz-9d1198dae6b3f7006351310d20bf62561232","nonce":"5UBM07","pubkey":"EB2A38568661887FA180BDDB5CABD5F21C7BFD59C090CB2D245A87AC253062882729293E5506350508E7F9AA3BB77F4333231490F915F6D63C55FE2F08A49B353F444AD3993CACC02DB784ABBB8E42A9B1BBFFFB38BE18D78E87A0E41B9B8F73A928EE0CCEE1F6739884B9777E4FE9E88A1BBE495927AC4A799B3181D6442443","rsakv":"1330428213","exectime":3})')
	pass


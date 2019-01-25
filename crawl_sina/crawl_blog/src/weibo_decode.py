import urllib, binascii, rsa, base64

def post_encode(user, pwd, servertime, nonce, pubkey, rsakv, pcid, door):
	'''
	generate post data
	'''
	#******base 64******#
	encoded_user = encode_user(user)
	#******rsa ******#
	encoded_pwd  = encode_pwd(pwd, servertime, nonce, pubkey)
	post_para = {
		'entry': 'weibo',
		'gateway': '1',
		'from': '',
		'savestate': '7',
		'userticket': '1',
		'ssosimplelogin': '1',
       	'vsnf': '1',
	   	'vsnval': '',
        	'su': encoded_user,
        	'service': 'miniblog',
        	'servertime': servertime,
        	'nonce': nonce,
        	'pwencode': 'rsa2',
        	'sp': encoded_pwd,
        	'encoding': 'UTF-8',
        	'prelt': '115',
        	'rsakv': rsakv,    
        	'url': 'http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',
        	'returntype': 'META',
			'pcid': pcid,
			'door': door
	}
	post_data = urllib.urlencode(post_para)		#internet encode
	return post_data	

def encode_user(user):
	'''
	encode user name with base 64
	'''
	user_tmp = urllib.quote(user)
	encode_user = base64.encodestring(user_tmp)[:-1]
	return encode_user

def encode_pwd(pwd, servertime, nonce, pubkey):
	rsa_pubkey = int(pubkey, 16)
	#******create public key ******#
	key = rsa.PublicKey(rsa_pubkey, 65537)	
	message = str(servertime) + '\t' + str(nonce) + '\n' + str(pwd)
	passwd = rsa.encrypt(message, key)
	passwd = binascii.b2a_hex(passwd)
	return passwd	

	
if __name__ == '__main__':
	pass

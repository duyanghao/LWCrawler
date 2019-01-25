# LWCrawler
A lightweight crawler to collect hot spot content of [sina](https://weibo.com/).

## Process

![](https://raw.githubusercontent.com/duyanghao/LWCrawler/master/images/sina_crawler_process.png)

As is shown in the picture, the process of LWCrawler is commonly performed following these steps:

* login sina

1. 获取`servertime`, `nonce`, `pubkey`, `rsakv`, `pcid`字段

发送`HTTP GET`请求到如下地址：

```
http://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su=&rsakt=mod&client=ssologin.js(v1.4.11)&_=1379834957683
```

获取`servertime`, `nonce`, `pubkey`, `rsakv`, `pcid`如下：

```
sinaSSOController.preloginCallBack({"retcode":0,"servertime":1548388758,"pcid":"gz-0ebe667ff54e3d91ef45f17de848f65b11bd","nonce":"M1D973","pubkey":"EB2A38568661887FA180BDDB5CABD5F21C7BFD59C090CB2D245A87AC253062882729293E5506350508E7F9AA3BB77F4333231490F915F6D63C55FE2F08A49B353F444AD3993CACC02DB784ABBB8E42A9B1BBFFFB38BE18D78E87A0E41B9B8F73A928EE0CCEE1F6739884B9777E4FE9E88A1BBE495927AC4A799B3181D6442443","rsakv":"1330428213","exectime":4})
```

2. 获取验证码

根据`pcid`字段，发送`HTTP GET`请求到如下地址：

```
http://login.sina.com.cn/cgi/pin.php?p={gz-0ebe667ff54e3d91ef45f17de848f65b11bd}
```

获取验证码文件cha.jpg

3. 输入验证码

![](https://raw.githubusercontent.com/duyanghao/LWCrawler/master/images/cha.jpg)

4. 带信息登录

发送`HTTP POST`请求到如下地址：

```
http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.11)
```

将输入的验证码字段`door`与先前获取的`servertime`, `nonce`, `pubkey`, `rsakv`, `pcid`等字段作为`POST`请求内容发送

```
[2019-01-25 11:59:16 ]: servertime is 1548388758 !
[2019-01-25 11:59:16 ]: nonce is M1D973 !
[2019-01-25 11:59:16 ]: pubkey is EB2A38568661887FA180BDDB5CABD5F21C7BFD59C090CB2D245A87AC253062882729293E5506350508E7F9AA3BB77F4333231490F915F6D63C55FE2F08A49B353F444AD3993CACC02DB784ABBB8E42A9B1BBFFFB38BE18D78E87A0E41B9B8F73A928EE0CCEE1F6739884B9777E4FE9E88A1BBE495927AC4A799B3181D6442443 !
[2019-01-25 11:59:16 ]: rsakv is 1330428213 !
[2019-01-25 11:59:16 ]: pcid is gz-0ebe667ff54e3d91ef45f17de848f65b11bd !
[2019-01-25 11:59:45 ]: door is KE54e
[2019-01-25 11:59:45 ]: POST DATA is nonce=M1D973&pcid=gz-0ebe667ff54e3d91ef45f17de848f65b11bd&savestate=7&from=&service=miniblog&encoding=UTF-8&url=http%3A%2F%2Fweibo.com%2Fajaxlogin.php%3Fframelogin%3D1%26callback%3Dparent.sinaSSOController.feedBackUrlCallBack&servertime=1548388758&sp=5628e54604480ff22f9a92f9f199aa55b756a712c8d64cc15f11488dbf3f106993f964bb1660a88c1b2c8b56883f9e0ae600adec423dd3ff51cec04c2f00c6a9f08e7870edbe213a2dfb4cdb98a2bc875107356001929b267a99e6aa18f3ff604b7809132968294a1f324ca875ef0ea5c374af8404361211e133f8c38d2523c9&vsnval=&door=KE54e&su=Mzc0NjYwMjY3JTQwcXEuY29t&rsakv=1330428213&userticket=1&vsnf=1&returntype=META&entry=weibo&ssosimplelogin=1&gateway=1&prelt=115&pwencode=rsa2
```

5. 重定向登录

如果用户、密码、验证码都正确，会有一个重定向报文，这个时候解析出重定向地址，并进行最终登录请求，如下：

```
[2019-01-25 11:59:47 ]: login_url = http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack&ssosavestate=1579924789&display=0&ticket=ST-MjY4OTQ2MjQ2Mw==-1548388789-gz-B267E8C5D66ABFCA7A192313668506BF-1&retcode=0
```

最终登录过程日志如下：

```
[2019-01-25 11:59:16 ]: Initializing logining...
[2019-01-25 11:59:16 ]: progress start to run ...
[2019-01-25 11:59:16 ]: start try to login ...
[2019-01-25 11:59:16 ]: get server time ...
[2019-01-25 11:59:16 ]: sinaSSOController.preloginCallBack({"retcode":0,"servertime":1548388758,"pcid":"gz-0ebe667ff54e3d91ef45f17de848f65b11bd","nonce":"M1D973","pubkey":"EB2A38568661887FA180BDDB5CABD5F21C7BFD59C090CB2D245A87AC253062882729293E5506350508E7F9AA3BB77F4333231490F915F6D63C55FE2F08A49B353F444AD3993CACC02DB784ABBB8E42A9B1BBFFFB38BE18D78E87A0E41B9B8F73A928EE0CCEE1F6739884B9777E4FE9E88A1BBE495927AC4A799B3181D6442443","rsakv":"1330428213","exectime":4})
[2019-01-25 11:59:16 ]: servertime is 1548388758 !
[2019-01-25 11:59:16 ]: nonce is M1D973 !
[2019-01-25 11:59:16 ]: pubkey is EB2A38568661887FA180BDDB5CABD5F21C7BFD59C090CB2D245A87AC253062882729293E5506350508E7F9AA3BB77F4333231490F915F6D63C55FE2F08A49B353F444AD3993CACC02DB784ABBB8E42A9B1BBFFFB38BE18D78E87A0E41B9B8F73A928EE0CCEE1F6739884B9777E4FE9E88A1BBE495927AC4A799B3181D6442443 !
[2019-01-25 11:59:16 ]: rsakv is 1330428213 !
[2019-01-25 11:59:16 ]: pcid is gz-0ebe667ff54e3d91ef45f17de848f65b11bd !
[2019-01-25 11:59:45 ]: door is KE54e
[2019-01-25 11:59:45 ]: POST DATA is nonce=M1D973&pcid=gz-0ebe667ff54e3d91ef45f17de848f65b11bd&savestate=7&from=&service=miniblog&encoding=UTF-8&url=http%3A%2F%2Fweibo.com%2Fajaxlogin.php%3Fframelogin%3D1%26callback%3Dparent.sinaSSOController.feedBackUrlCallBack&servertime=1548388758&sp=5628e54604480ff22f9a92f9f199aa55b756a712c8d64cc15f11488dbf3f106993f964bb1660a88c1b2c8b56883f9e0ae600adec423dd3ff51cec04c2f00c6a9f08e7870edbe213a2dfb4cdb98a2bc875107356001929b267a99e6aa18f3ff604b7809132968294a1f324ca875ef0ea5c374af8404361211e133f8c38d2523c9&vsnval=&door=KE54e&su=Mzc0NjYwMjY3JTQwcXEuY29t&rsakv=1330428213&userticket=1&vsnf=1&returntype=META&entry=weibo&ssosimplelogin=1&gateway=1&prelt=115&pwencode=rsa2
[2019-01-25 11:59:45 ]: POST DATA len is 670!
[2019-01-25 11:59:45 ]: Post request...
[2019-01-25 11:59:47 ]: login_url = http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack&ssosavestate=1579924789&display=0&ticket=ST-MjY4OTQ2MjQ2Mw==-1548388789-gz-B267E8C5D66ABFCA7A192313668506BF-1&retcode=0
[2019-01-25 11:59:48 ]: login successfully!
```

* crawl content

* parse content

* cluster analysis

## TODO

* login sina

* crawl content

* parse content 

* cluster analysis


OA## Refs


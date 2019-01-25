# LWCrawler
A lightweight crawler to collect hot spot content of [sina](https://weibo.com/).

## Run

按照如下操作运行LWCrawler：

```bash
git cloen https://github.com/duyanghao/LWCrawler.git
cd LWCrawler/crawl_sina
tar -xzf rsa-3.1.1.tar.gz
export PYTHONPATH=./rsa-3.1.1/build/lib
cd crawl_blog/tools
bash start.sh
```

## Process

![](https://raw.githubusercontent.com/duyanghao/LWCrawler/master/images/sina_crawler_process.png)

As is shown in the picture, the process of LWCrawler is commonly performed following these steps:

### login sina

* 获取`servertime`, `nonce`, `pubkey`, `rsakv`, `pcid`字段

发送`HTTP GET`请求到如下地址：

```
http://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su=&rsakt=mod&client=ssologin.js(v1.4.11)&_=1379834957683
```

获取`servertime`, `nonce`, `pubkey`, `rsakv`, `pcid`如下：

```
sinaSSOController.preloginCallBack({"retcode":0,"servertime":1548388758,"pcid":"gz-0ebe667ff54e3d91ef45f17de848f65b11bd","nonce":"M1D973","pubkey":"EB2A38568661887FA180BDDB5CABD5F21C7BFD59C090CB2D245A87AC253062882729293E5506350508E7F9AA3BB77F4333231490F915F6D63C55FE2F08A49B353F444AD3993CACC02DB784ABBB8E42A9B1BBFFFB38BE18D78E87A0E41B9B8F73A928EE0CCEE1F6739884B9777E4FE9E88A1BBE495927AC4A799B3181D6442443","rsakv":"1330428213","exectime":4})
```

* 获取验证码

根据`pcid`字段，发送`HTTP GET`请求到如下地址：

```
http://login.sina.com.cn/cgi/pin.php?p={gz-0ebe667ff54e3d91ef45f17de848f65b11bd}
```

获取验证码文件`cha.jpg`

* 输入验证码

![](https://raw.githubusercontent.com/duyanghao/LWCrawler/master/images/cha.jpg)

* 带信息登录

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

* 重定向登录

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

### crawl content

这里采用简单的单进程爬取新浪微博内容，发送`HTTP GET`请求如下：

```
http://d.weibo.com/102803?from=page_102803#
```

抓取静态HTML文件并写到本地：

```
[2019-01-25 11:59:48 ]: start crawl hot weibo ...
[2019-01-25 11:59:49 ]: start save downloaded html to into a file...
[2019-01-25 11:59:49 ]: end save downloaded html into weibo_2019-01-25_11:59:49 file ...
```

### parse content

这里采用最简单的正则表达式对抓取的静态HTML文件进行解析，提取出每个用户发表的微博中第一行内容：

```
[2019-01-25 11:59:49 ]: ***********************start to parse filename = weibo_2019-01-25_11:59:49 ***********************
[2019-01-25 11:59:49 ]: start parser html ...
[2019-01-25 11:59:49 ]: start hot weibo ...
[2019-01-25 11:59:49 ]: #######################index = 1 #######################
[2019-01-25 11:59:49 ]: content =
[2019-01-25 11:59:49 ]: #######################index = 2 #######################
[2019-01-25 11:59:49 ]: content =                                                                     小花妹妹。求您放过我吧。 <200b><200b><200b><200b>                     
[2019-01-25 11:59:49 ]: #######################index = 3 #######################
[2019-01-25 11:59:49 ]: content =                                                                     大家别担心，这几天有了蓝胖子和面膜护体，晒伤全好了！新西兰的风景很美，
大家来玩一定注意防晒！出来工作好久了，我想吃山东各种美食，
[2019-01-25 11:59:49 ]: #######################index = 4 #######################
[2019-01-25 11:59:49 ]: content =
[2019-01-25 11:59:49 ]: #######################index = 5 #######################
[2019-01-25 11:59:49 ]: content =                                                                     2009年的我和2019年的我，你更喜歡哪個時期的我呢？
[2019-01-25 11:59:49 ]: #######################index = 6 #######################
[2019-01-25 11:59:49 ]: content =
[2019-01-25 11:59:49 ]: #######################index = 7 #######################
[2019-01-25 11:59:49 ]: content =                                                                     今年的
[2019-01-25 11:59:49 ]: #######################index = 8 #######################
[2019-01-25 11:59:49 ]: content =
[2019-01-25 11:59:49 ]: #######################index = 9 #######################
[2019-01-25 11:59:49 ]: content =
[2019-01-25 11:59:49 ]: #######################index = 10 #######################
[2019-01-25 11:59:49 ]: content =                                                                     左边09年刚出道 vs 右边19年现在的我 ，岁月慢慢带着我的骨胶原流失，却又>成就了今天站在大家面前的我，时间啊你真令人又爱又恨
[2019-01-25 11:59:49 ]: #######################index = 11 #######################
[2019-01-25 11:59:49 ]: content =                                                                     要100个赞可以吧？&nbsp;&nbsp;&nbsp;【搞笑】 <200b><200b><200b><200b>  
[2019-01-25 11:59:49 ]: #######################index = 12 #######################
[2019-01-25 11:59:49 ]: content =                                                                     【直播：国足赛后新闻发布会！】三个相同的失误，个个致命，中国队最终0-3>不敌伊朗，无缘半决赛。如何评价这场比赛？里皮有什么话要说？正直播赛后新闻发布会，一起来听听！
[2019-01-25 11:59:49 ]: #######################index = 13 #######################
[2019-01-25 11:59:49 ]: content =                                                                     纪念一下今天...
[2019-01-25 11:59:49 ]: #######################index = 14 #######################
[2019-01-25 11:59:49 ]: content =                                                                     感动，这也许是父亲送给女儿最好的礼物。
[2019-01-25 11:59:49 ]: #######################index = 15 #######################
[2019-01-25 11:59:49 ]: content =                                                                     每个人都拼到了现在，真的好想好想和大家一起创造奇迹！可是这么重要的比赛
，自己却出现了这么愚蠢低级的失误。太难接受了。不想去找任何借口！对不起大家！希望中国足球未来更好，希望大家还能继续支持中国队！ <200b><200b><200b><200b>                     
[2019-01-25 11:59:49 ]: 15
[2019-01-25 11:59:49 ]: end hot weibo
[2019-01-25 11:59:49 ]: progress go to sleep ...
```

原始新浪页面：

![](https://raw.githubusercontent.com/duyanghao/LWCrawler/master/images/sina_page.png)

### cluster analysis

这里解析部分还没有实现，有待完善（kmeans聚类？）……

## TODO

### login sina

登录过程，现在还需要手动输入验证码，后续可以自动识别……

### crawl content

爬取过程现在只是抓取静态网页，无法抓取动态网页且为单进程单线程抓取。可以采用多线程对动态网页并发进行爬取（涉及多线程同步）……

### parse content 

解析过程现在只是提取微博第一行内容，且有些微博会漏掉，后续可以进行优化，抓取整个微博内容且尽量不遗漏……

### cluster analysis

聚类算法目前没有实现，可以采用`kmeans`算法对解析的微博内容进行聚类，提取出热点话题……
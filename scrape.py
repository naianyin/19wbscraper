from bs4 import BeautifulSoup as bs
import requests as rq
import datetime
import urllib.parse as ups
import base64 as b64

def currentts(digits):
	return str(round(datetime.datetime.timestamp(datetime.datetime.now())*(10**(digits-10))))

def prelogin(uname):

	return "https://login.sina.com.cn/sso/prelogin.php?checkpin=1&entry=mweibo&su="+ b64.b64encode(bytes(ups.quote(uname),"utf-8")).decode("utf-8") +"&callback="+currentts(13)


uname="361369167@qq.com"
pwd="Jiubugaosuni2_"
headers={'Content-Type': 'application/x-www-form-urlencoded', 'Origin': 'https://passport.weibo.cn', 'Referer': 'https://passport.weibo.cn/signin/login', 'Sec-Fetch-Mode': 'cors', \
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
data=bytes("username="+ups.quote(uname)+"&password=" + ups.quote(pwd) + \
	"&savestate=1&r=&ec=0&pagerefer=&entry=mweibo&wentry=&loginfrom=&client_id=&code=&qq=&mainpageflag=1&hff=&hfp=","utf-8")
endpoint="https://passport.weibo.cn/sso/login"

ss=rq.session()
print(ss.get(prelogin(uname)).content)
print(ss.post(endpoint,data=data,headers=headers,verify=False).content)

print(ss.cookies)




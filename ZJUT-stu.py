import requests
import json
import time

userName = str()#输入学号
userPasswd = ""#输入密码

header = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Cookie": "PHPSESSID=bfmqcq63e0ht62iiotkn0ois24",
    "Referer": "http://192.168.8.1/a79.htm?wlanuserip=10.81.31.102&wlanacname=ME60&wlanacip=192.168.8.10&wlanuserfirsturl=http://172.16.22.83",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
    "Host": "192.168.8.1:801"
}

data = {
    "c": "Portal",
    "a": "login",
    "callback": "dr1003",
    "login_method": "1",
    "user_account": ",0," + userName,
    "user_password": userPasswd,
    "wlan_user_ip": "10.81.102.91",
    "wlan_user_mac": "0000000",
    "wlan_ac_ip": "192.168.8.10",
    "wlan_ac_name": "ME60",
    "jsVersion": "3.3.3",
    "v": "2675"

}
#192.168.8.1:801 不同设备不一样，具体的看登录网址
url = "http://192.168.8.1:801/eportal/?c=Portal&a=login&callback=dr1003&login_method=1&user_account=%2C0%2C"\
      +userName+"&user_password="+userPasswd+"&wlan_user_ip=10.81.31.91&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=192.168.8.10&wlan_ac_name=ME60&jsVersion=3.3.3&v=2675"


response = requests.post(url, data=data, headers=header)
if response.text[18:19] == '1':
    print('success')
else:
    print('error')
time.sleep(5)

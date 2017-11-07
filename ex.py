from urllib import request
import re
import random

def ua_ip(myurl,delaytime):
    uapools=[
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36 OPR/37.0.2178.32",
             ]
    def api():
        print('这一次调用了接口')
        thisall=request.urlopen("http://tvp.daxiangdaili.com/ip/?tid=558658506836506&num=10")
        print(thisall)
        ippools=[]
        for item in thisall:
            #print(item.decode('utf-8','ignore'))
            ippools.append(item.decode('utf-8','ignore'))
        return ippools
    def ip(ippools,time,uapools):
        thisua=random.choice(uapools)
        print(thisua)
        headers=("User-Agent",thisua)
        thisip=ippools[time]
        print(thisip)
        proxy=request.ProxyHandler({"http":thisip})
        opener=request.build_opener(proxy,request.HTTPHandler)
        opener.add_headers=[headers]
        request.install_opener(opener)
    x=0
    for i in range(0,35):
        try:
            if(x%10==0):
                time=x%10
                ippools=api()
                ip(ippools,time,uapools)
            else:
                time=x%10
                ip(ippools,time,uapools)
            url=myurl
            data=request.urlopen(url,timeout=delaytime).read().decode('utf-8','ignore')
            print(len(data))
            x+=1
            break
        except Exception as err:
            print(err)
            x+=1
    return data

from urllib import request
import re
import random

key='零食'
uapools=[
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36 OPR/37.0.2178.32",
         ]
def ua(uapools):
    thisua=random.choice(uapools)
    print(thisua)
    headers=("User-Agent",thisua)
    opener=request.build_opener()
    opener.add_headers=[headers]
    #安装为全局
    request.install_opener(opener)

for i in range(1,30,2):
    print('当前第'+str((i+1)/2)+'页')
    ua(uapools)
    keyword=request.quote(key)
    thisurl='https://search.jd.com/Search?keyword='+keyword+'&enc=utf-8&page='+str(i)
    data=request.urlopen(thisurl).read().decode('utf-8','ignore')
    goodspat='<strong class="J_.*?" data-done="1"><em>￥</em><i>(.*?)</i>.*?<a target="_blank" title="(.*?)"'
    #pricepat='<strong class=".*?" data-done="1"><em>￥</em><i>(.*?)</i>.*?<em><span class="p-tag" .*?</span>.*?<font class="skcolor_ljg">零食</font>.*?</em>'
    goodsrst=re.compile(goodspat,re.S).findall(data)
    #pricerst=re.compile(pricepat,re.S).findall(data)
    #print(goodsrst)
    goodsallrst=[]
    for item in goodsrst:
        text=item[1].replace('<font class="skcolor_ljg">零食</font>','')
        text=text.replace('<font class="skcolor_ljg">零食零食</font>','')
        print(text+'  '+item[0])

from urllib import request
import random
import re

keyword = '零食'
key = request.quote(keyword)
# https://search.jd.com/Search?keyword=%E9%9B%B6%E9%A3%9F&enc=utf-8&page=1

uapools = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36 OPR/37.0.2178.32",
]


def ua(uapools):
    thisua = random.choice(uapools)
    print(thisua)
    headers = ("User-Agent", thisua)
    opener = request.build_opener()
    opener.add_headers = [headers]
    # 安装为全局
    request.install_opener(opener)


for i in range(1, 10, 2):
    ua(uapools)
    pageurl = 'https://search.jd.com/Search?keyword=' + key + '&enc=utf-8&page=' + str(i)
    data = request.urlopen(pageurl).read().decode('utf-8', 'ignore')
    pat = '<strong class=".*?" data-done="1"><em>￥</em><i>(.*?)</i></strong>.*?<em>(.*?)<font class="skcolor_ljg">零食</font>(.*?)</em>'
    rst = re.compile(pat, re.S).findall(data)
    goodslist = []
    for item in rst:
        text = item[1] + item[2]
        addtext = re.compile('(￥.*?src=".*?" />)', re.S).findall(text)
        addtext1= re.compile('(<font class="skcolor_ljg">.*?</font>)', re.S).findall(text)
        # print(addtext)
        text = text.replace('<span class="p-tag" style="background-color:#c81623">京东超市</span>', '')
        text = text.replace('<font class="skcolor_ljg">零食</font>', '零食')
        text = text.replace('<font class="skcolor_ljg">礼包</font>', '礼包')
        text = text.replace('<font class="skcolor_ljg">零食零食</font>', '零食零食')
        text = text.replace('<font class="skcolor_ljg">包邮</font>', '包邮')
        '''
        if len(addtext) != 0:
            text = text.replace(addtext[0], '')
        
        if len(addtext1) != 0:
            for i in range(0,len(addtext1)):
                text=text.replace(addtext1[i], '零食')
        '''
        price = item[0]
        goodslist.append(text + '  ' + price)
    with open('.//' + str((i+1)/2) + '.txt', 'w') as file:
        for line in goodslist:
            if len(line)<100:
                file.write(line + '\n')
    commentpat = '<strong class="J_(.*?)"'
    commenturlall = re.compile(commentpat, re.S).findall(data)
    for thisID in commenturlall:
        for num in range(1,3):
            thiscommenturl='https://sclub.jd.com/comment/productPageComments.action?productId='+thisID+'&score=0&sortType=5&page='+str(num)+'&pageSize=10'
            commentdata=request.urlopen(thiscommenturl).read().decode('gbk','ignore')
            pagecommetpat='"content":"(.*?)","creationTime"'
            commentall=re.compile(pagecommetpat,re.S).findall(commentdata)
            with open('.//' + thisID + '.txt', 'a') as file:
                for linenum in range(0,len(commentall)):
                    if commentall[linenum]!=commentall[linenum-1] or linenum==0:
                        file.write(commentall[linenum]+'\n')
    print(len(goodslist))

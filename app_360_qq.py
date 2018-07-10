# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 09:55:54 2018

@author: jcao2014
"""

# '\u2022' '•'
#\u25aa' '▪'
#from unicodedata import name
from selenium import webdriver
# from pandas import read_table, DataFrame, ExcelWriter
from bs4 import BeautifulSoup
from time import sleep
from urllib.parse import urlencode
from random import choice
from urllib.request import Request, urlopen
from json import loads

def get360info(data):
    driver = webdriver.PhantomJS(executable_path='C:\\Users\\jcao2014\\Downloads\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')
    driver.get(data)
    sleep(3)
    data = BeautifulSoup(driver.page_source).find_all('dd')
    driver.close()
    title = []
    print(len(data))
    for i in data:
        title.append((i.a['title'].strip()))
    return title

for i in ['旅游','出境游','国内游','旅行','周边游']:
    with open(i + '360.txt', 'a') as f:
        for j in range(1, 35):
            url = 'http://zhushou.360.cn/search/index/?' + urlencode({'kw': i, 'page': str(j)})
            try:
                title = get360info(url)
                print(title)
                if len(title) == 0: break
                print('\n'.join(title), file = f)
            except Exception as e:
                print(str(e))
                continue


def genHeader():
    headerset = [
        {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
         "Accept": "text/html,application/xhtml+xml,application/xml; q=0.9,image/webp,*/*;q=0.8"},
        {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ' 'Chrome/45.0.2454.101 Safari/537.36'},
        {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)" "Chrome/52.0.2743.116 Safari/537.36"},
        {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)" "Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586"},
        {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"},
        {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0"},
        {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"}]
    return choice(headerset)

baseUrl = 'http://sj.qq.com/myapp/searchAjax.htm?'
app = {}
for i in ['旅游','出境游','国内游','周边游','旅行']:
    try:
        with open(i+'360.txt') as f:
            with open(i+'.txt', 'a') as g:
                for j in f:
                    j = j.strip()
                    if j in app:
                        print({'keyword':i, 'name':j, 'detail':app[j]}, file=g)
                    else:
                        try:
                            print(j)
                            data = {'kw': j}
                            data = baseUrl + urlencode(data)
                            data = Request(url=data, headers=genHeader())
                            data = urlopen(data).read()
                            sleep(3)
                            data = data.decode()
                            data = loads(data)
                            for k in data['obj']['items']:
                                if j in k['appDetail']['appName'] or k['appDetail']['appName'] in j:
                                    print(k['appDetail']['appName'])
                                    print({'keyword':i, 'name':j, 'detail':k['appDetail']}, file=g)
                                    app[j] = k['appDetail']
                                    break
                        except Exception as e:
                            print('inner', str(e))
                            continue
    except Exception as e:
        print('outer', str(e))
        continue

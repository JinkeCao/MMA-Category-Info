import requests
from bs4 import BeautifulSoup
import time
import timeout_decorator
import random
import timeit
##from lxml import etree
import urllib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def writeByLine(fileName, content):
    with open(fileName, "a") as f:
        print(content.strip(), file = f)

def pageNum(l):
##    try:
    driver = webdriver.PhantomJS(executable_path='/home/jinke/Documents/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')
##    driver = webdriver.firefox()
    driver.get(l)
    time.sleep(10)
    pageSource = driver.page_source
    bsObj = BeautifulSoup(pageSource)
    n = bsObj.find("em", class_="fui-paging-num").get_text()
    print(n)
    return int(n)
##    
##    except Exception as e:
##        print(e)
##        pass
##     
     
##for i in a:
##    n = pageNum(i)
##    print(n)
##    n = int(n)
##    for j in range(n):
##        writeByLine("hufu",i + "&beginPage=" + str(j+1))

with open("urlClean") as f:
    for i in f:
##        try:                
        info = i.strip()
        print(info)
        link = i.split(",")[3]
        n = pageNum(link)
        for j in range(n):
            write("page", info + "#beginPage="+str(j+1))
##        except Exception as e:
##            print(e)
##            continue

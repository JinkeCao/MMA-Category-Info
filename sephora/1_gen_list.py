import requests
from bs4 import BeautifulSoup
import random
import time

##{"护肤", "美容仪", "美容仪配件", "PHILIPS飞利浦", "飞利浦净颜焕采洁肤仪普通刷头"}

session = requests.Session()
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
           "Accept":"text/html,application/xhtml+xml,application/xml; q=0.9,image/webp,*/*;q=0.8"}
inputs = ["http://www.sephora.cn/category/60001/,护肤",
          "http://www.sephora.cn/category/60005/,男士护肤",
          "http://www.sephora.cn/category/60002/,彩妆",
          "http://www.sephora.cn/category/60007/,香水",
          "http://www.sephora.cn/category/60006/,美发护发",
          "http://www.sephora.cn/category/60003/,洗浴护体"]
            
def getlinks(info):
    links = []
    url = info.split(",")[0]
    category = info.split(",", maxsplit = 1)[1]
    req = session.get(url, headers=headers)
    bsObj = BeautifulSoup(req.text)
    subBs = bsObj.find("div",class_="categoryNav categoryNavMob").findAll("li")
    for i in subBs:
        links.append(i.find("a").attrs["href"] + "," + category + "," + i.find("a").attrs["title"])
    time.sleep(random.randrange(1, 3))
    return links

def getpages(inputs):
    for i in inputs:
        for j in getlinks(i):
            for k in getlinks(j):
                with open("pages", "a") as output:
                    print(k, file=output)
                    print(k)

if __name__ == "__main__":
    try:
        getpages(inputs)
    except Exception as e:
        print(str(e))




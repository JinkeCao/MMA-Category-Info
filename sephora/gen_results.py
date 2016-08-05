import requests
import random
import time
import json
from lxml import etree


session = requests.Session()
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
           "Accept":"text/html,application/xhtml+xml,application/xml; q=0.9,image/webp,*/*;q=0.8"}

def getPages(info):
    lists = [info]
    url, category = info.split(",", maxsplit = 1)[0], info.split(",", maxsplit = 1)[1]
    body = session.get(url, headers=headers).text
    pageNum = etree.HTML(body).xpath('//*[@id="searchResultListDiv"]/div[4]/label/b')[0].text
    n = int(pageNum)
    if n > 1:
        for i in range(2, n+1):
            lists.append(url + "page" + str(i) + "/," + category)
    time.sleep(random.randrange(2, 3))
    return lists


def genInputs(filenames):
    with open(filenames) as data:
        for i in data:
            i = i.strip()
            for j in getPages(i):
                with open("inputs", "a") as output:
                    print(j, file = output)
                    print(j)

if __name__ == "__main__":
    try:
        genInputs("pages")
    except Exception as e:
        print(str(e))

            
    
##print(getPages("http://www.sephora.cn/category/230198-230197-60001/,护肤,美容仪,美容仪"))

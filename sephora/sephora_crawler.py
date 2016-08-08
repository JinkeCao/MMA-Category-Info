import requests
import random
import time
import json
from bs4 import BeautifulSoup
## //*[@id="search_mini_450544"]/p[2]

session = requests.Session()
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
           "Accept":"text/html,application/xhtml+xml,application/xml; q=0.9,image/webp,*/*;q=0.8"}
n = 1

def fileOut(eachLine, n):
    url, c1, c2, c3 = eachLine.split(",")[0].strip(), eachLine.split(",")[1].strip(), eachLine.split(",")[2].strip(), eachLine.split(",")[3].strip()
    brandObj = BeautifulSoup(session.get(url, headers=headers).text).find("ul", class_ = "mb64 clearFix").findAll("p",class_="proBrand")
    for i in brandObj:
        brand, info = i.get_text().strip(), i.next_sibling.next_sibling.find("a").attrs["title"]
        with open("mma_sephora_20160807.json", "a") as output:
            print(json.dumps({"1st":c1, "2nd":c2, "3rd":c3, "brand":brand, "info":info}, ensure_ascii = False, sort_keys = True), file = output)
        print(str(n)+ " " + info)
        n = n + 1
    time.sleep(random.randrange(2, 5))
    return n

try:
    with open("inputs") as infile:
        for i in infile:
            n = fileOut(i, n)
except Exception as e:
    print(str(e))

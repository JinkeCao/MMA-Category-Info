import urllib
def writeByLine(fileName, content):
    with open(fileName, "a") as f:
        print(content.strip(), file = f)

with open("MMALinks.txt") as f:
    for i in f:
        if "1688" in i:
            url = i.strip()
            data = urllib.parse.urlparse(url)
            query = data.query.split("&")
            for j in query:
                if "keywords" in j:
                    keywords = j.split("=")[1]
                    cate = urllib.parse.unquote(keywords,encoding='gbk')
                    writeByLine("urlClean", cate + ",https://s.1688.com/selloffer/offer_search.htm?" + j)
                    

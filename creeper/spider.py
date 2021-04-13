import re
from urllib import request
class Spider():
    url = 'http://gg.q1.com/'
    root_pattern = '<ul class="nav">([\s\S]*?)</ul>'
    big_title = '<p>([\s\S]*?)</p>'
    small_title = '<span>([\s\S]*?)</span>'

    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        return r.read().decode('utf8')

    def __analysis(self,htmls):
        root_html = re.findall(Spider.root_pattern,htmls)
        titleArr = []
        for r in root_html:
            title1 = re.findall(Spider.big_title,r)
            title2 = re.findall(Spider.small_title,r)
            titles = list(map(lambda x,y:{'big_title':x,'small_title':y},title1,title2))
            length = len(titles)
            if length>0:
                titleArr = titles
        print(titleArr)
        print(len(titleArr))

    def runSpider(self):
        htmls = self.__fetch_content()
        self.__analysis(htmls)

spider = Spider()
spider.runSpider()
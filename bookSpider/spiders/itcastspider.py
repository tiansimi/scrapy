__author__ = '努力学习 不要让自己失望'

# 放置spider代码的目录。
import scrapy
from bookSpider.items import ItcastItems


class ItcastSpider(scrapy.Spider):
    # 爬虫名（执行的时候写这个名字）
    name = "itcast"
    # 允许爬虫作用的范围
    allowd_domains = ["http://www.itcast.cn/"]
    start_urls = ["http://www.itcast.cn/channel/teacher.shtml#"]
    print("1")

    def parse(self, response):
        # with open("teacher.html", "wb") as f:
        #   f.write(response.body)
        # 通过scrapy自带的xpath匹配出所有的老师的根节点
        teacher_list = response.xpath("//div[@class = 'li_txt']")
        teachersItem = []

        # 遍历跟节点集合
        for each in teacher_list:
            item = ItcastItems()
            # extract()将匹配出来的对象结果转换为unicode字符串
            name = each.xpath("./h3/text()").extract()
            # 不加extract()结果为xpath
            title = each.xpath("./h4/text()").extract()
            info = each.xpath("./p/text()").extract()

            item["name"] = name[0]
            item["title"] = title[0]
            item["info"] = info[0]
            # teachersItem.append(item)

            '''with open("itcast.txt", "a+", encoding="utf-8") as f:
                f.write(name[0])
                f.write(title[0])
                f.write(info[0])        '''

            yield item

from scrapy.crawler import CrawlerProcess

from kgc.python数据爬取.scrapy_demo.scrapy_demo.spiders.example import ExampleSpider

process = CrawlerProcess()
process.crawl(ExampleSpider)
process.start()
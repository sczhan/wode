from scrapy.cmdline import execute

execute("scrapy crawl qcwy_sp_spider -o jobs.csv".split())
# execute("scrapy crawl qcwy_sp_spider".split())
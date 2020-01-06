# Scrapy
# 爬虫框架
- 框架
- 爬虫框架
    - scrapy
    - pyspider
    - crawley
    
- scrapy框架介绍
    - https://doc.scrapy.org/en/latest
    - http://scrapy-chs.readthedocs.io/zh_CN/latest/index.html
    
- 安装
    - 利用pip
    
- scrapy概述
    - 包含各个部件
        - ScrapyEngine: 神经中枢, 大脑, 核心
        - Scheduler调度器: 引擎发来的request请求,调度器需要处理,然后交换引擎
        - Downloader下载器: 把引擎发来的requests发出请求,得到response
        - Spider爬虫: 负责把下载器得到的页面/结果进行分解, 分解成数据+链接
        - ItemPipeline: 详细处理Item
        - DownloaderMiddleware下载中间件: 自定义下载的功能扩展功能
        - SpiderMiddleware爬虫中间件: 对sipder进行功能扩展
        
- 爬虫项目流程:
    - 新建项目:scrapy startproject xxx
    - 明确需要目标/产出: 编写item.py
    - 制作爬虫: 地址 spider/xxspider.py
    - 存储内容: pipelines.py
        
- 案列e1-scrapy-baidu
    - 利用最简单的爬虫
    - 爬取百度页面
    - 关闭配置机器人协议
    - scrapy startproject baidu
    - scrapy crawl baidu
    
- 案列e2_scrapy_meiju
    - 创建新项目
    - 分析网页, 定义item
    - 编写pipeline, 确定如何处理item
    - 编写spider, 确定如何提取item
    - 可以通过增加一个单独命令文件的方式在pycharm中启动
    
- 案列e3_qq招聘
    - 创建项目
    - 编写item
    - 编写spider
    - 编写pipeline
    - 设置pipeline
    
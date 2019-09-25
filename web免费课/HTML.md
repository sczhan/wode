

HTML概述

一. 什么是HTML
- HTML 是用来描述网页的一种语言
    - 超文本标记语音(英语: Hyper Text  Markup Language 简称:HTML)是一种用于创建网页的标准标记语言
    -  HTML 不是一种编程语言, 而是一种标记语言
    - 标记语言是一套标记标签(markup tag)
    - HTML 文档包含了HTML标签及文本内容
    - HTML 文档也叫做web页面
    
二. HTML是干嘛的
    - 可以使用HTML来建立自己的WEB站点, HTML运行在浏览器上, 有浏览器来解析.
    
三. 建立HTML文件
    - .html
    - .htm
    
四. HTML注释
    - <!--注释内容--> 
    - pcharm：(ctrl + ?) 快速创建一个注释
    
五. HTML网页的基本结构
    - <!DOCTYPE html>   声明为HTML5 文档
    - <html>    元素是 HTML 页面的根元素
    - <head>    元素包含了文档的元(neta)数据
    - <body>    元素包含了可见的页面内容
    
    - 通用声明(了解)
    
        - HTML5
            - <!DOCTYPE html>   
            
        - HTML4.01
            - <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
              "http://www.w3.org/TR/html4/loose.dtd">         
        - HTML1.0
        
            - <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
              "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
              
六. HTML标签结构  1.html
HTML 标记标签通常被称为HTML标签(HTML tag)
    - HTML 标签是由尖括号包围的关键词
    - HTML 标签通常成对出现
    - 标签对中的第一个标签是开始标签, 第二个标签是结束标签
        - <开始标签>内容</结束标签>
        
七. HTML元素
"HTML 标签" 和 "HTML 元素" 通常都是描述同样的意思. 一个 HTML 元素包含了开始标签与结束标签

八. HTML属性
    - HTML 元素可以设置属性
    - 属性一般添加在开始标签
    - 属性一般以名称/值对的形式出现，比如：name="value"
    - 注意: 
        - 属性值必须用双引号引起来
        - 标签都用小写字母
        - 双标签必须要写闭合标签
        

HTML 常用标签 
一. HTML常用的块级标签(块级元素)  2.html
    - 独占一行
    - 有语义的HTML块级元素
        - 有默认样式
        - 标题（Heading） 
            - 通过H1～H6 标签来定义的.
        - 段落标签
            - 通过标签 p 来定义的.
        - 列表
            - 无序列表 ul,li
                - 是一个项目的列表,列项目使用粗体圆点（典型的小黑圆圈）进行标记
            - 有序列表 ol,li
                - 也是一个项目的列表，列表项目使用数字进行标记。
            - 自定义列表 dl,dt,dd（了解）
        - 表格 table,tr,td
            - table常用属性:
                - border        边框
                - cellpadding   内容距离表框的距离
                - cellspacing   单元格和单元格之间的距离
                - rowspan       垂直合并（跨行显示）
                - colspan       水平合并（跨列显示）
                - anglin        内容水平对其方式
                - valign        内容垂直对其方式
    - 无意义的块级元素 div
        - <div> 元素没有特定的含义。除此之外，由于它属于块级元素，浏览器会在其前后显示换行。
        - 一般与 CSS 一同使用
        - <div> 元素的另一个常见的用途是文档布局。它取代了使用表格定义布局的老式方法。

二. HTML 常用的行级标签(行内元素) 3.html
- 不独占一行

- 有语义的行内元素
    - HTML 链接 a标签
        - <a href="链接地址">链接文本</a>
        - target属性，定义被链接的文档在何处显示  _blank 新窗口打开
        
    - HTML图像
        - <img src="图片地址" alt="">
    - 文本标签
        - b标签 i标签 strong标签 em标签

- 无语义的行内元素
    - span标签 配合css使用
# CSS
- 为了让网页的样式更加丰富
- 也为了让网页的内容和样式能拆分开
- CSS由此思想而诞生，
- CSS是 Cascading Style Sheets 的首字母缩写，意思是层叠样式表。
- 有了CSS，html中大部分表现样式的标签就废弃不用了,
- html只负责文档的结构和内容，表现形式完全交给CSS，html文档变得更加简洁。

## Css基本语法及页面引用
- css的定义方法是:选择器(属性:值 属性:值 属性:值) 选择器是将样式和页面元素关联起来的名称,属性是希望设置的样式属性有一个或多个值.

- css页面引入方法
    - 1. 外联式: 通过link标签,连接到外部样式表页面中
        - <link rel="stylesheet" type="text/css" href="css/mian.css">
    - 2.嵌入式: 通过style标签, 在网页上创建嵌入的样式表
        - <style type="text/css">
            div{width:100px; height:100px; color:red}
            ....
          </style>
    - 3.内联式: 通过标签的style属性, 在标签上直接写样式
        - <div style=width:100px; height:100px; color:red;>
          ....
          </div>   
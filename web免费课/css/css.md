# CSS
- 为了让网页的样式更加丰富
- 也为了让网页的内容和样式能拆分开
- CSS由此思想而诞生，
- CSS是 Cascading Style Sheets 的首字母缩写，意思是层叠样式表。
- 有了CSS，html中大部分表现样式的标签就废弃不用了,
- html只负责文档的结构和内容，表现形式完全交给CSS，html文档变得更加简洁。

## CSS基本语法及页面引用
###css基本语法
- css的定义方法是:选择器(属性:值 属性:值 属性:值) 选择器是将样式和页面元素关联起来的名称,属性是希望设置的样式属性有一个或多个值.
    - div{width:100px; height:200px; color:red;}
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
          
## CSS选择器
常用的选择器有如下几种:
    - 1.标签选择器
        - 标签选择器, 此种选择器影响范围比较大,建议尽量应用在层级选择器中.
        - 举例: 
            *{margin:0;padding:0}
            div{color:red}   
            <div>....</div>   <!-- 对应以上两条样式 -->
            <div class="box">....</div>   <!-- 对应以上两条样式 -->
    - 2.id选择器
        - 通过id名来选择元素,元素的id名称不能重复,所以一个样式设置项只能对应于页面上一个元素, 不能复用,id名一般给程序使用,所以不推荐使用id作为选择器
        - 举例:
            #box{color:red;}
            <div id="box">.....</div>
    - 3.类选择器
        - 通过类名选择元素,一个类可应用于多个元素,一个元素上也可以使用多个类, 应用灵活,可复用,是css中应用最多的一种选择器
        - 举例:
            .red{color:red;}
            .big{font-size:20px;}
            .mt10{margin-top:10px;}
            <div class="red">...</div>
            <div class="red big mt10">...</div>
            <div class="red mt10">...</div> 
    - 4、层级选择器
        - 主要应用在选择父元素下的子元素，或者子元素下面的子元素，可与标签元素结合使用，减少命名，
        - 同时也可以通过层级，防止命名冲突。
            - 举例:
                .box span{color:red}
                .box .red{color:pink}
                .red{color:red}
                <div class="box">
                    <span>....</span>
                    <a href="#" class="red">....</a>
                </div>       
                <h3 class="red">....</h3>
    - 5、组选择器
        - 多个选择器，如果有同样的样式设置，可以使用组选择器。也成为并列选择
        - 举例:
            .box1,.box2,.box3{width:100px;height:100px}
            .box1{background:red}
            .box2{background:pink}
            .box2{background:gold}
            <div class="box1">....</div>
            <div class="box2">....</div>
            <div class="box3">....</div>  
    -6、伪类及伪元素选择器
        - 常用的伪类选择器有hover，表示鼠标悬浮在元素上时的状态，
        - 伪元素选择器有before和after,它们可以通过样式在元素中插入内容。
        - 举例:
            .box1:hover{color:red}
            <div class="box1">....</div>
            a:hover {color: #FF00FF; text-decoration: underline} /* 鼠标在该元素上时 */
            a:before{content:"Hello";}         /*在每个<a>元素之前插入内容*/
            a:after{content:"world";}        /*在每个<a>元素之后插入内容*/
      
        
        
# Css颜色,文本字体

## css颜色表示法
css颜色表达法:
    - 1.颜色名表示，比如：red 红色，gold 金色
    - 2.16进制数值表示，比如：#ff0000 表示红色，这种可以简写成 #f00
        - 取值范围: 16进制  0-9 a-f
    - 3.RGB颜色: 红(R)、绿(G)、蓝(B)三个颜色通道的变化 background-color: rgb(200,100,0);
        - 取值范围: rgb的值 0-255
    - 4.RGBA颜色: 红(R)、绿(G)、蓝(B)、透明度(A) background-color: rgba(0,0,0,0.5);
        - 透明度取值 0.0 - 1.0 的小数

## css文本设置
常用的应用文本的css样式：
    - color 设置文字的颜色，如： color:red;
    - font-size 设置文字的大小，如：font-size:12px;
    - font-family 设置文字的字体，如：font-family:'微软雅黑';
    - font-style 设置字体是否倾斜，如：font-style:'normal'; 设置不倾斜，font-style:'italic';设置文字倾斜
    - font-weight 设置文字是否加粗，如：font-weight:bold; 设置加粗 font-weight:normal 设置不加粗
    - line-height 设置文字的行高，如：line-height:24px;
    - text-decoration 设置文字的下划线，如：text-decoration:none; 将文字下划线去掉
    - text-indent 设置文字首行缩进，如：text-indent:24px; 设置文字首行缩进24px
    - text-align 设置文字水平对齐方式，如text-align:center 设置文字水平居中
    
    
## css边框属性
- CSS边框属性:
    - border:宽度 样式 颜色;
    - border-color;
    - border-style; 边框样式：solid实线，dotted点状线，dashed虚线
    - border-width:
    - border-left-color;
    - border-left-style;
    - border-left-width:
- CSS3的样式:
    border-radius：圆角处理
    box-shadow: x轴偏移 y轴偏移 模糊度 扩散程度 颜色 inset内阴影 设置或检索对象阴影
## 背景属性
- 背景属性:
    - background-color: 背景颜色
    - background-image: 背景图片
    - background-repeat：是否重复，如何重复?(平铺)
    - background-position：定位   
    - background-size: 背景大小，如 background-size:100px 140px;
    
## 元素溢出
当子元素的尺寸超过父元素的尺寸时，需要设置父元素显示溢出的子元素的方式，设置的方法是通过overflow属性来设置。
- overflow的设置项：
    - 1.visible 默认值。内容不会被修剪，会呈现在元素框之外。
    - 2.hidden 内容会被修剪，并且其余内容是不可见的，此属性还有清除浮动、清除margin-top塌陷的功能。
    - 3.scroll 内容会被修剪，但是浏览器会显示滚动条以便查看其余的内容。
    - 4.auto 如果内容被修剪，则浏览器会显示滚动条以便查看其余的内容。
 
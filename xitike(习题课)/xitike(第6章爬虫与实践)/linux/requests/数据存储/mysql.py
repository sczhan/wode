"""
数据存储之mysql
Ubuntu环境安装mysql
    sudo apt-get update
    sudo apt-get install mysql-server
    sudo apt-get install mysql-client
    sudo apt-get install libmysqlclient-dev

登录数据库:
    sudp mysql -u root -p



rhel7 环境安装mysql数据库
    https://www.cnblogs.com/guozhiping/p/7684134.html

mysql数据库远程连通:
    1. 修改/etc/mysql/my.conf
        找到bind-address = 127.0.0.1 这一行, 将这一行注释
        或者: 将这一行改为bing-address= 0.0.0.0

    2. 让root用户支持连接mysql数据库
        mysql -u root -p
        grant all privileges on *.* to root@'%' identified by "yourpassword" with grant option

    3. 让rhel7中防火墙允许mysql服务通过
        firewall-cmd --permanent --add -service=mysql
        firewall -cmd --reload


Python操作mysql(pymysql)
    pip install pymysql
"""
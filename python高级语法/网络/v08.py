from email.mime.text import MIMEText

mail_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Love You</title>
    </head>
    <body>
    <h1> 我最爱刘梦</h1>
    </body>
    <html>
    """

msg = MIMEText(mail_content, "html", "UTF-8")

# 构造发送者地址和登录信息
from_addr = "5481493@qq.com"
from_pwd = "xpcdvyxaporlbhgf"

# 构造邮件接受者信息
to_addr = "1019409214@qq.com"
srv = "smtp.qq.com"

try:
    import smtplib
    msg_srv = smtplib.SMTP_SSL(srv.encode(), 465)
    msg_srv.login(from_addr, from_pwd)
    msg_srv.sendmail(from_addr, [to_addr], msg.as_string())
    msg_srv.quit()

except Exception as e:
    print(e)

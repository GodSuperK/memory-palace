# Email 提醒

发送邮件的协议是STMP, Python内置对SMTP 的支持，可以发送纯文本邮件、HTML 邮件以及带附件的邮件。Python对SMTP支持有smtplib 和 email 两个模块、email负责构造邮件，smtplib 负责发送邮件。



## Getting Ready

1. 申请一个163邮箱，开启 SMTP 功能，采用的是网易的电子邮件服务器 smtp.163.com.

## Basic Use

**发送纯文本邮件**

```python
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr

import smtplib

# MIMEText(邮件正文，subtype, 编码格式) plain 表示纯文本，最终的MIME 就是 text/plain
# What is MIME type
# https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Basics_of_HTTP/MIME_types
content = ("赠汪伦\n唐代 李白\n李白乘舟将欲行，忽闻岸上踏歌声。"
           "\n桃花潭水深千尺，不及汪伦送我情。")
msg = MIMEText(content, 'plain', 'utf-8')


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode('utf-8'), addr))


# 发件人地址
from_addr = 'iamliuche@163.com'
# 授权码
password = "xxxxxx"
# 收件人地址
to_addr = "1796017500@qq.com"
# 163 网易邮箱服务器地址
smtp_server = "smtp.163.com"

# 设置发件人
msg['From'] = _format_addr('孔德成 <no-reply{}>'.format(from_addr))
# 设置收件人
msg['To'] = _format_addr('{}'.format(to_addr))
# 设置主题
msg['Subject'] = Header('千里送行', 'utf-8').encode()

# 发送邮件
server = smtplib.SMTP(smtp_server, 25)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

```

**发送html邮件**

在构造 MIMEText对象时， 把HTML字符串传进去， 再把subtype 变成 html就行了。

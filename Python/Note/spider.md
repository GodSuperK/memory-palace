#  网络爬虫开发



## 爬虫分类

1. 通用网络爬虫：搜索引擎（baidu, Yahoo and Google）通用搜索引擎的目标时尽可能大的网络覆盖率。
2. 聚焦网络爬虫： 一个自动下载网页的程序，将目标定为抓取与某一特定主题内容相关的网页。
3. 增量式网络爬虫：只获取更新的数据，以前爬取过的数据不重复爬取，例如爬取招聘信息。
4. 深层网络爬虫：爬取用户登陆或者注册才能访问的网页。

## 网络爬虫实际运用场景

1. 常见的BT网站，通过爬取互联网的DHT网络中分享的BT种子信息，提供对外搜索服务。
2. 一些云盘搜索网站，通过爬取用户共享出来的云盘文件数据，对文件数据进行分类划分，从而提供对外搜索服务。

## 网络爬虫的基本工作流程：

1. 首先选取一部分精心挑选的种子URL
2. 将这些URL放入待抓取URL队列
3. 从待抓取URL队列中读取待抓取队列的URL，解析DNS，并且得到主机的IP，并将URL对应的网页下载下来，存储进已下载网页库中。此外，将这些URL放进已抓取URL队列。
4. 分析已抓取URL队列中的URL，从已下载的网页数据中分析出其他URL，并和已抓取的URL进行比较去重，最后将去重过的URL放入待抓取URL队列，从而进入下一个循环。



### 完整的请求与响应模型

```python
import urllib.request
import ssl

# 取消全局证书验证
ssl._create_default_https_context = ssl._create_unverified_context
URL_1 = 'https://www.baidu.com'
URL_2 = 'https://httpbin.org/post'
def req_resp_get_1(url):
    # 请求 -> 响应 （一步完成）
    resp = urllib.request.urlopen(url=url)
    # show bytes content
    html = resp.read()
    return html


def req_resp_get_2(url):
    # 请求 -> 响应 （两步完成）
    req = urllib.request.Request(url=url)
    resp = urllib.request.urlopen(req)
    html = resp.read()
    return html

def req_resp_post_1(url):
    post_data = {
        'username': 'ABU',
        'password': 'kaduoxi'
    }
    # 对数据进行编码
    data = urllib.parse.urlencode(post_data)
    # 请求, 数据实体为bytes类型
    req = urllib.request.Request(url=url, data=data.encode())
    # 响应
    resp = urllib.request.urlopen(req)
    html = resp.read()
    return html
```

### 请求头headers 处理

```python
"""即使POST请求的数据是对的，但是服务器拒绝你的访问。

问题出在请求中的头信息，服务器会检验请求头，来判断是否是来自浏览器的访问
这也是反爬虫的常用手段。
"""

import urllib.request
import urllib.parse
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

URL = 'https://httpbin.org/post'

user_agent = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 "
              "(KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36")

# referer 的作用：https://www.sojson.com/blog/58.html
referer = "https://httpbin.org/"

post_data = {
    'username': 'ABU',
    'password': 'kaduoxi'
}


def post_1(url):
    # 构造请求头
    headers = {
        'User_Agent': user_agent,
        'Referer': referer
    }
    data = urllib.parse.urlencode(post_data).encode()
    req = urllib.request.Request(url=url, data=data, headers=headers)
    resp = urllib.request.urlopen(req)
    html = resp.read().decode()
    return html


def post_2(url):
    data = urllib.parse.urlencode(post_data).encode()
    req = urllib.request.Request(url=url, data=data)
    # 写入头信息
    req.add_header('User-Agent', user_agent)
    req.add_header('Referer', referer)
    resp = urllib.request.urlopen(req)
    html = resp.read().decode()
    return html


if __name__ == "__main__":
    print(post_2(url=URL))

```

对有些header要特别留意，服务器会针对这些header 做检查，例如：

1. User-Agent: 有些服务器或Proxy 会通过该值来判断是否是浏览器发出的请求。
2. Content-Type: 在使用REST接口时，服务器会检查该值，用来确定HTTP Body中的内容该怎样解析。在使用服务器提供的RESTful或SOAP服务时， Content-Type 设置错误会导致服务器拒绝服务。常见的取值有：application/xml(在 XML RPC， 如 RESTful/SOAP 调用时使用)、application/json (在 JSON RPC调用时使用)、application/x-www-from-urlencoded(浏览器提交web表单时使用)
3. Referer: 服务器有时候会检查防盗链

### Cookie 处理

```python
import urllib.request
from http import cookiejar

from spider.utils import Utils


def main():
    # 取消ssl全局验证
    Utils.unverified_ssl()
    # 使用CookieJar 对象管理cookie
    cookie = cookiejar.CookieJar()
    # 创建一个请求打开器，将一个HTTPCookieProcessor cookie处理器对象作为参数传入
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
    # 使用opener 的open 方法发起请求
    response = opener.open('https://www.zhihu.com')
	# 迭代cookie
    Utils.show_cookie(cookie)


if __name__ == "__main__":
    main()
```

### 设置响应超时时间

```python
import urllib.request
from urllib.error import URLError
from spider.utils import Utils

Utils.unverified_ssl()
try:
    # 如果请求超时，则会抛出 urllib.error.URLError 异常
    resp = urllib.request.urlopen('https://www.google.com', timeout=2)
except URLError as e:
    print(e)
```

### 获取响应状态码

对于 200 OK 来说， 只要使用 urlopen 返回的 response 对象的 getcode() 方法就可以得到 HTTP 的返回码。 但对其他返回码来说， urlopen 会抛出异常。这时候，就要检查异常对象的 code 属性了。

```python
import urllib.request

from spider.utils import Utils

Utils.unverified_ssl()
try:
    resp = urllib.request.urlopen('http://39.105.73.108/hello')
    print(resp.read())
except urllib.request.HTTPError as e:
    if hasattr(e, 'code'):
        print('Error code:', e.code)
```

### 重定向

urllib 默认情况下会针对 HTTP 3XX 返回码自动进行重定向动作。要检测是否发生了重定向动作，只要检查一下Response的URL和Request的URL是否一致就可以了。

```python
import urllib.request

URL = 'http://www.zhihu.cn'
resp = urllib.request.urlopen(URL)
isReDirected = resp.geturl() == URL
```



### Proxy的设置

使用ProxyHandler在程序中动态设置代理

```python
from urllib.request import ProxyHandler
import urllib.request

from spider.utils import Utils

Utils.unverified_ssl()

opener = urllib.request.build_opener(ProxyHandler({'http:': '127.0.0.1:8787'}))
# 设置urllib 全局opener, 之后所有的访问都使用这个代理
urllib.request.install_opener(opener)
resp = urllib.request.urlopen("https://www.baidu.com")
print(resp.read())
```

```python

opener = urllib.request.build_opener(ProxyHandler({'http:': '127.0.0.1:8787'}))
# 不设置全局代理
resp = opener.open("https://www.baidu.com")
print(resp.read())
```

### http.client实现

```python
import http.client
import urllib.parse


def req_get():
    conn = None
    try:
        conn = http.client.HTTPConnection("www.baidu.com")
        conn.request("GET", '/')
        resp = conn.getresponse()
        # 获得返回状态码， 和返回说明
        print(resp.status, resp.reason)
        # 获得响应的头部信息(列表格式)
        print(resp.getheaders())
        # 获得响应的头部信息（字符串格式）
        print(resp.msg)
    except Exception as e:
        print(e)
    finally:
        if conn:
            conn.close()


def req_post():
    conn = None
    post_data = {'name': 'ABU', 'password': 'kaduoxi'}
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
    data = urllib.parse.urlencode(post_data).encode()
    try:
        conn = http.client.HTTPConnection("httpbin.org", timeout=3)
        conn.request("POST", '/post', data, headers=headers)
        resp = conn.getresponse()
        # 获得返回状态码， 和返回说明
        print(resp.status, resp.reason)
        # 获得响应的头部信息(列表格式)
        print(resp.getheaders())
        # 获得响应的头部信息（字符串格式）
        print(resp.msg)
        print(resp.read().decode())
    except Exception as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    req_post()

```

## 更人性化的 Requests

### 一、请求

```python
import requests

# 不带参数的 get 请求
resp_get = requests.get("https://www.baidu.com")
# 带参数的 get 请求
params = {'name': 'abu', 'password': 'kaduoxi'}
resp_get_param = requests.get(url="https://httpbin.org/get", params=params)
# 查看完整的url
print(resp_get_param.url)

# post 请求
post_data = {'name': 'ABU', 'password': 'kaduoxi'}
resp_post = requests.post(url='https://httpbin.org/post', data=post_data)
```

### 二、响应与编码

```python
import requests

resp = requests.get(url="https://www.baidu.com")
# resp.content -> bytes
print("Content:", resp.content)
# resp.text -> str
print("Text:", resp.text)
# resp.encoding -> 根据HTTP头猜测的网页编码格式
print("Encoding:", resp.encoding)
```

#### 文本出现乱码

**方法1**

```python
# 将页面的编码形式修改正确
resp.encoding = "utf8"
print(resp.text)
```

**方法2**

```python
import chardet
# -> {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}
# confidence 是检测精确度， encoding 是编码形式
right_encoding = chardet.detect(resp.content)['encoding']
resp.encoding = right_encoding
print(resp.text)
```

### 三、请求头headers 处理

```python
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
resp_get = requests.post(url='https://httpbin.org/', headers=headers)
resp_post = requests.post(url='https://httpbin.org/post', headers=headers)
```

### 四、响应码 code 和响应头 headers 处理

```python
import requests

resp = requests.get(url='https://httpbin.org')
if resp.status_code == requests.codes.ok:
    # 获取 response 的状态码
    print(resp.status_code)
    # 获取response 的 headers 信息 -> dict
    print(resp.headers)
    # 字典的操作，通过key取value， 如果key不存在，返回None
    print(resp.headers.get('content-type'))
else:
    # 主动的产生一个异常
    # 当响应码是4XX和5XX时，会抛出异常
    # 当响应码是200时，返回None
    resp.raise_for_status()
```

### 五、Cookie 处理

```python
# 如果响应中包含Cookie的值， 可以如下方式获取 Cookie 的值
import requests
from spider.utils import Utils


# 获取response 中返回的cookie值
def get_cookie_1():
    resp = requests.get(url='https://github.com/')
    # <class 'requests.cookies.RequestsCookieJar'>
    # 兼容性类; 是一个cookielib.CookieJar，但暴露了一个字典接口。
    print(type(resp.cookies))

    # 使用字典接口迭代cookies
    for i in resp.cookies.keys():
        print(i, resp.cookies[i])

    # 使用类字段迭代
    Utils.show_cookie(resp.cookies)


# 在发送的请求中携带自己定义的cookie值
def get_cookie_2():
    cookies = {'name': 'abu', 'password': 'kaduoxi'}
    resp = requests.get(url='https://httpbin.org', cookies=cookies)
    print(resp.text)


"""
有时候我们不需要关系 Cookie 值是多少，只是希望每次访问的时候，
程序自动的把cookie的值带上，像浏览器一样。
Requests提供了一个session的概念，在连续访问网页，处理登陆跳转时特别方便，
不需要关注具体细节。

"""
def get_cookie_4():
    loginURL = 'http://www.xxxx.com/login'
    s = requests.Session()
    # 首先访问登陆界面，作为游客，服务器会先分配一个cookie
    r = s.get(loginURL, allow_redirects=True)
    datas = {'name': 'abu', 'password': 'kaduoxi'}
    # 向登陆链接发送post请求，验证成功，游客权限转为会员权限
    r = s.post(loginURL, data=datas, allow_redirects=True)
    print(r.text)


if __name__ == "__main__":
    pass
```

### 六、重定向与历史信息

```python
"""
处理重定向只是需要设置一下 allow_redirects 字段即可，例如:
requests.get(url, allow_redirects=True)
设置为False表示禁止重定向
可以通过r.history字段查看历史信息，即访问成功之前的所有请求跳转信息
"""
import requests

resp = requests.get('http://www.sun.com')
# 获取实际请求的url
print(resp.url)
print(resp.status_code)
# 迭代所有跳转历史
for i in resp.history:
    print(i.url)
```

### 七、超时设置

```python
requests.get('https://github.com', timeout=2)
```

### 八、代理设置

使用代理 Proxy, 你可以为任意请求方法通过设置 proxies 参数来配置单个请求：

```python
import requests
proxies = {
    'http': "http://0.10.1.10:3128",
    'https': "http://10.10.1.10:1080"
}
requests.get("http://example.org", proxies=proxies)
```

代理需要使用HTTP Basic Auth， 可以使用 `http://user:password@host/`语法

```python
proxies = {
    'http': 'http://user:pass@10.10.1.10:3128',
}
```


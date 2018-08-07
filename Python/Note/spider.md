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
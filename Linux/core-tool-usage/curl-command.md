# cURL Usage
根据[http://www.codebelief.com/article/2017/05/linux-command-line-curl-usage/](http://www.codebelief.com/article/2017/05/linux-command-line-curl-usage/)整理

## 1. 获取页面内容
当不加任何选项使用curl时，默认会发送GET请求来获取链接内容到标准输出。
```shell
curl http://www.baidu.com
```

## 2. 显示 HTTP 头
`-I` 选项，只显示Response headers，而不显示文件内容
```shell
curl -I http://www.baidu.com
```
`-i` 选项， 同时显示响应头和文件内容
```shell
curl -i http://www.baidu.com
```

## 3. 响应内容保存到文件
可以使用 `>` 将输出重定向到本地文件中
```shell
curl http://www.baidu.com > index.html
```

也可以通过curl自带的`-o/-O` 选项将内容保存到文件中
- `-o`: 需提供文件名
- `-O`: 使用url中末尾的文件名,如果没有文件名，应该使用-o选项
```shell
curl -o index.html http://www.baidu.com
# 爱的童话-任然
curl -O http://m10.music.126.net/20180930071858/3d6a497a0b9feb57556f3f2bd92b73c2/ymusic/2629/ef28/8fab/342ffe5e297dd941293d04ee6c54058c.mp3
```

## 4. 同时下载多个文件
```shell
curl -O url1 -O url2
curl -o name1 url1 -o name2 url2
```

## 5. 自动重定向
如果直接使用curl 打开某些被重定向后的链接，这种情况下就无法获取我们想要的网页内容,而当我们通过浏览器打开链接时，会自动跳转到重定向后的网址。
我们可以使用`-L`选项来自动实现重定向跳转
```shell
curl -I http://codebelief.com

HTTP/1.1 301 Moved Permanently
Date: Sat, 29 Sep 2018 23:14:40 GMT
Server: Apache/2.4.10 (Debian)
Location: http://www.codebelief.com/
Content-Type: text/html; charset=UTF-8
```
```shell
curl -L http://codebelief.com
```

## 6. 自定义User-Agent
```shell
curl -A "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36" https://www.baidu.com
```

## 7. 自定义 header
```shell
curl -H "Referer: www.example.com" -H "User-Agent: Custom-User-Agent" http://www.baidu.com
# 携带cookie
curl -H "Cookie: JSESSIONID=D0112A5063D938586B659EF8F939BE24" http://www.example.com
```

## 8. 保存Cookie
当我们使用curl访问页面的时候，默认时不会保存Cookie的。可以使用`-c`选项将cookie保存到指定的文件中。
```shell
curl -c "cookie-example" http://www.example.com
```

## 9. 读取Cookie

```shell
# 自定义cookie发送
curl -b "JSESSIONID=D0112A5063D938586B659EF8F939BE24" http://www.example.com
# 从文件中读取Cookie
curl -b "cookie-example" http://www.example.com
```

## 发送 POST 请求
```shell
curl -d "username=tom&password=123456"  http://www.httpbin.org/post
# 保存第一次登陆时服务器设置的cookie
curl -c "cookie-login" -d "username=tom&password=123456"  http://www.httpbin.org/post
# 下次访问携带cookie,可以保持登陆状态
curl -b "cookie-login" http://www.httpbin.org/post

```

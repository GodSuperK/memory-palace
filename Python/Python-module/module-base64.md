# base64

> Base64是一种用64个字符来表示任意的二进制数据的方法, 适用于小段内容的编码，比如URL

## How to use?

```python
import base64

url = "https://www.python.org/"

# 加密 返回 bytes 对象
url_encode = base64.urlsafe_b64encode(url.encode())

# 解密 返回 bytes 对象
url_decode = base64.urlsafe_b64decode(url_encode)
```


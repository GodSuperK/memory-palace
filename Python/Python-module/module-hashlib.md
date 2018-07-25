# hashlib

> hashlib模块提供了许多的hash算法,包括 md5, sha1, sha224, sha256, sha384, sha512

## Hash

1. hash也叫做散列函数
2. 可以把任意长度的数据转换为，一个长度固定的数据串
3. 特点：不可逆，唯一

## How to use?

```python
import hashlib
"""
hashlib.update() - 更新 hash 对象
hash.digest() - 返回Hash算法计算得到的值(bytes类型) 
hash.hexdigest() - 返回Hash算法计算得到的值(16进制 str类型)
hashlib.pbkdf2_hmac() - 用于对密码加密. 返回加密后的密钥 key(bytes类型)
pbkdf2_hmac（hash_name，password，salt，iterations，dklen = None）
"""

s = "中国"
md5_s = hashlib.md5(s.encode())
print(md5_s.hexdigest())

# 加密密码
passwd = "xffdsfdse213.".encode()
salt = "fsdf;'./".encode()
key = hashlib.pbkdf2_hmac("md5", passwd, salt, 10000)
print(key)
```


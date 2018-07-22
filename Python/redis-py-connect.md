# How to connect Redis Server in Python

> use redis module

`pip install redis`



## Basic demo1

```python
import redis
# 创建 redis 客户端实例
# decode_responses=True 表示存入的value是str类型, 反之为 byte 类型
r = redis.Redis(host='localhost', port=6379, decode_responses=True)
# redis set命令
r.set('name', 'ABU')
# 通过字典索引方式 get value
print(r['name'])
# 通过字典的 get 方法 to get value
print(r.get('name')) 
```



## 连接池

> 使用connection pool来管理对一个redis server的所有连接，避免每次建立、释放连接的开销。默认，每个Redis实例都会维护一个自己的连接池。 可以直接建立一个连接池，然后作为参数传给Redis，这样就可以实现多个Redis实例共享一个连接池

```python
import redis

# 创建一个连接池实例
pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
# 创建客户端实例时 指定连接池
r = redis.Redis(connection_pool=pool)
r.set('gender', 'male')
print(r.get('gender'))
```

## Redis 基本命令

### String

### 1. redis.Redis.set()

```python
"""Set the value at key ``name`` to ``value``

set(self, name, value, ex=None, px=None, nx=False, xx=False)

:param ex: sets an expire flag on key ``name`` for ``ex`` seconds(秒).  
:param px: sets an expire flag on key ``name`` for ``px`` milliseconds(毫秒).
:param nx: 如果设置为True，则只有name不存在时，当前set操作才执行
:param xx: 如果设置为True，则只有name存在时，当前set操作才执行

"""
```

### 2. redis.Redis.setnx()

```python
"""设置值，只有name不存在时，执行设置操作（添加）

setnx(self, name, vlaue)
"""
```

### 3. redis.Redis.mset()

```python
"""批量设置值
mset(self, *args, **kwargs)

根据映射设置键/值。 可以直接传入一个字典或 传递多个关键字参数
Sets key/values based on a mapping. Mapping can be supplied as a 
single dictionary argument or as kwargs.

"""
```

### 4. redis.Redis.mget()

```python
"""批量取出1个或多个key的值
mget(self, keys, *args)

Returns a list of values ordered identically to ``keys``
"""
```

### 5. redis.Redis.getset()

```python
"""设置新值并获取原来的值
getset(self, name, value)

Sets the value at key ``name`` to ``value`` and returns the old value at key ``name`` atomically.
"""
```

### 6. redis.Redis.getrange()

```python
"""获取子序列（根据字节获取，非字符）
getrange(self, key, start, end)

Returns the substring of the string value stored at ``key``, 
determined by the offsets ``start`` and ``end`` (both are inclusive)

参数：
name，Redis 的 name
start，起始位置（字节）
end，结束位置（字节）
如： "君惜大大" ，0-3表示 "君"
"""
```

### 7. redis.Redis.setrange()

```python
"""修改字符串内容，从指定字符串索引开始向后替换（新值太长时，则向后添加）

setrange(self, name, offset, value)

Overwrite bytes in the value of ``name`` starting at ``offset`` with ``value``. 
If ``offset`` plus the length of ``value`` exceeds the length of the original value, 
the new value will be larger than before. If ``offset`` exceeds the length of the 
original value, null bytes will be used to pad between the end of the previous value 
and the start of what's being injected.
    
Returns the length of the new string.

参数：
offset，字符串的索引，字节（一个汉字三个字节）
value，要设置的值
"""
```

### 8. redis.Redis.strlen()

```python
"""返回name对应值的字节长度（一个汉字3个字节, 一个字母一个字节）

strlen(self, name)

Return the number of bytes stored in the value of ``name``

"""
```

### 9. redis.Redis.incr()

```python
"""自增 name对应的值，当name不存在时，则创建name＝amount，否则，则自增

incr(self, name, amount=1)

Increments the value of ``key`` by ``amount``.  If no key exists, 
the value will be initialized as ``amount``

参数：
name,Redis的name
amount,自增数（必须是整数）
"""
```

#### 应用场景: 页面点击计数器

```python
import redis
 
# 导入连接配置信息
from test1 import redis_config

# 页面点击逻辑
def add_time():
    # 使用incr命令自增
    r.incr('page:index', amount=1)
 
if __name__ == "__main__":
    pool = redis.ConnectionPool(**redis_config)
 	r = redis.Redis(connection_pool=pool)
	# 设置页面初始点击次数
    r.set('page:index', 1000)
	while True:
        # 模拟页面点击
    	if input('>') == "y":
			add_time()
		else:
	 		break
    # 查看点击总数        
	print(r.get('page:index'))
```

### 10. redis.Redis.incrbyfloat()

```python
"""
同incr()
amount,自增数（浮点型）
"""
```

### 11. redis.Redis.decr()

```python
"""自减 name对应的值，当name不存在时，则创建name＝amount，否则，则自减。
decr(self, name, amount=1)

Decrements the value of ``key`` by ``amount``.  If no key exists, 
the value will be initialized as 0 - ``amount``

参数：
name,Redis的name
amount,自减数（整数)
"""
```

### 12. redis.Redis.append()

```python
"""在redis name对应的值后面追加内容

append(self, key, value)

Appends the string ``value`` to the value at ``key``. 
If ``key`` doesn't already exist, create it with a value of ``value``. 
Returns the new length of the value at ``key``.

将字符串``value``追加到``key``的值。 如果``key``不存在，则使用值``value``创建它。 返回``key``的值的新长度。
"""
```

### Hash

### 1. redis.Redis.hset()

```python
"""单个增加--修改(单个取出)--key不存在就添加，key 存在就修改 key 对应的 value
hset(self, name, key, value)

Set ``key`` to ``value`` within hash ``name``
Returns 1 if HSET created a new field, otherwise 0

hsetnx(name, key, value),当name对应的hash中不存在当前key时则创建（相当于只能添加）
"""
```

### 2. redis.Redis.hmset()

```python
"""批量增加（取出）
hmset(self, name, mapping)

Set key to value within hash ``name`` for each corresponding 
key and value from the ``mapping`` dict.

"""
r.hmset("hash", {"k2": "v2", "k3": "v3"})
```





### 3. redis.Redis.hget()

```python
"""在name对应的hash中获取根据key获取value
hget(self, name, key)
"""
r.hget("hash", "k1")
```

### 4. redis.Redis.hmget()

```python
"""在name对应的hash中获取多个key的值
hmget(self, name, keys, *args)

keys: 可以接收一个 list of keys, 也可以接收一个 key
"""

r.hmget("hash", "k1")
r.hmget("hash", "k1", "k2", "k3")
r.hmget("hash", ["k1", "k2", "k3"])
```

### 5. redis.Redis.hgetall()

```python
"""取出所有的键值对
hgetall(self, name)

获取name对应hash的所有键值
"""
r.hgetall("hash")
```

### 6. redis.Redis.hlen()

```python
"""返回 key 的个数, 相当于计算 hash 的长度
hlen(self, name)
"""
r.hlen("hash")
```

### 7. redis.Redis.hkeys()

```python
"""得到所有的keys（类似字典的取所有keys）
hkeys(self, name)
"""
r.hkeys("hash")
```

### 8. redis.Redis.hvals()

```python
"""得到所有的value（类似字典的取所有value）

hvals(self, name)
"""
r.hvals("hash")
```

### 9. redis.Redis.hexists()

```python
"""判断成员是否存在（类似字典的in）

hexists(self, name, key)
return True if exists else False
"""

r.hexists("hash", "k1")
```

### 10. redis.Redis.hdel()

```python
"""删除键值对
hdel(self, name, *keys)

Delete ``keys`` from hash ``name``
"""
r.hdel("hash", "k1", "k2", "k3")
r.hdel("hash", *["k1", "k2", "k3"])
```

### 11. redis.Redis.hincrby()

```python
"""自增自减整数
hincrby(self, name, key, amount=1)

自增(减, amount=-1)name对应的hash中的指定key的值，不存在则创建key=amount

参数：
name，redis中的name
key， hash对应的key
amount，自增数（整数）
"""

r.hincrby('hash', "k1", amount=1)
r.hincrby('hash', "k2", amount=-1)
```

### 12. redis.Redis.hincrbyfloat()

```python
"""自增自减浮点数
hincrbyfloat(name, key, amount=1.0)

同 hincrby, 只是 amount 是浮点类型
"""
```

### 13. redis.Redis.hscan()

```python
"""在哈希中递增返回键/值切片。 还返回指示扫描位置的光标。

hscan(self, name, cursor=0, match=None, count=None)
增量式迭代获取，对于数据大的数据非常有用，hscan可以实现分片的获取数据，并非一次性将数据全部获取完，从而防止内存被撑爆
参数：
name，redis的name
cursor，游标（基于游标分批取获取数据）
match，匹配指定key，默认None 表示所有的key
count，每次分片最少获取个数，默认None表示采用Redis的默认分片个数
如：
第一次：cursor1, data1 = r.hscan('xx', cursor=0, match=None, count=None)
第二次：cursor2, data1 = r.hscan('xx', cursor=cursor1, match=None, count=None)
...
直到返回值cursor的值为0时，表示数据已经通过分片获取完毕

Incrementally return key/value slices in a hash. Also return a cursor indicating the scan position. 

``match`` allows for filtering the keys by pattern 
``count`` allows for hint the minimum number of returns
"""

# 分片获取所有数据
datas = []
cursor = 0
while True:
	cursor, data = r.hscan("hash", cursor=cursor)
    datas.append(data)
    if not cursor:
        break
```

### 14. redis.Redis.hscan_iter()

```python
"""使用HSCAN命令创建一个迭代器，以便客户端不需要记住光标位置

hscan_iter(self, name, match=None, count=None)
利用yield封装hscan创建生成器，实现分批去redis中获取数据

参数：
match，匹配指定key，默认None 表示所有的key
count，每次分片最少获取个数，默认None表示采用Redis的默认分片个数
"""
datas = []
for data in r.hscan_iter("hash1"): 
    datas.append(data)
```


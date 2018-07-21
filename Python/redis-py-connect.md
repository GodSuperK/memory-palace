# How to connect Redis Server in Python

> use redis module

`pip install redis`



## Basic demo1

```python
import redis
# 创建 redis 客户端实例
# decode_reponses=True 表示存入的value是str类型, 反之为 byte 类型
r = redis.Redis(host='localhost', port=6379, decode_responses=True)
# redis set命令
r.set('name', 'ABU')
# 通过字典索引方式 get value
print(r['name'])
# 通过字典的 get 方法 to get value
print(r.get('name')) 
```



## 连接池

> 使用connection pool来管理对一个redis server的所有连接，避免每次建立、释放连接的开销。默认，每个Redis实例都会维护一个自己的连接池。 可以直接建立一个连接池，然后作为参数Redis，这样就可以实现多个Redis实例共享一个连接池

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

Returns the substring of the string value stored at ``key``, determined by the offsets ``start`` and ``end`` (both are inclusive)

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


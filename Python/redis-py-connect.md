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


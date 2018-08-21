# Redis

> Redis 是速度非常快的非关系型（NoSQL）内存键值数据库，可以存储键和五种不同类型的值之间的映射。
>
> 键的类型只能为字符串，值支持的五种类型数据类型为：字符串、列表、集合、有序集合、散列表。
>
> 值的类型决定了值本身支持的操作。Redis支持不同无序、有序的列表，无序、有序的集合间的交集、并集等高级服务器端原子操作。

## How to install?
```shell
sudo apt install redis-server
```

## Redis 基本命令

```shell
# 启动 redis 服务器端
redis-server
# 启动 redis 客户端
redis-cli
```



## Redis 数据结构

### String

```redis
> set hello world
OK
> get hello
"world"
> del hello
(integer) 1
> get hello
(nil)
```

### List

```
> rpush list-key item
(integer) 1
> rpush list-key item2
(integer) 2
> rpush list-key item
(integer) 3

# 迭代元素 lrange key start stop 
> lrange list-key 0 -1
1) "item"
2) "item2"
3) "item"

# 索引 lindex key index
> lindex list-key 1
"item2"

# 移除一个 value from left to right 
# lpop key
> lpop list-key
"item"

> lrange list-key 0 -1
1) "item2"
2) "item"

```

### Set

```
# 集合是元素不重复 无序的
> sadd set-key item
(integer) 1
> sadd set-key item2
(integer) 1
> sadd set-key item3
(integer) 1
> sadd set-key item
(integer) 0

# 迭代集合成员
> smembers set-key
1) "item"
2) "item2"
3) "item3"

# 判断是否是集合成员
> sismember set-key item4
(integer) 0
> sismember set-key item
(integer) 1

# 移除元素
> srem set-key item2
(integer) 1
# 返回 0 表示命令执行失败, 返回 1 表示命令执行成功
> srem set-key item2
(integer) 0

> smembers set-key
1) "item"
2) "item3"
```



### Zset

```
# key 的顺序 由 value的顺序决定
# zadd zset-key value(float) key
> zadd zset-key 728 member1
(integer) 1
> zadd zset-key 982 member0
(integer) 1
> zadd zset-key 982 member0
(integer) 0

# 迭代成员 withscores 表示 同时迭代 value
> zrange zset-key 0 -1 withscores
1) "member1"
2) "728"
3) "member0"
4) "982"

# 查找在 value 范围内的 key
# zrangebyscore key min max [withscores] [limit offset count]
> zrangebyscore zset-key 0 800 withscores
1) "member1"
2) "728"

# 删除 key
> zrem zset-key member1
(integer) 1
> zrem zset-key member1
(integer) 0

> zrange zset-key 0 -1 withscores
1) "member0"
2) "982"
```

### Hash

```
# key 不重复 无序
> hset hash-key sub-key1 value1
(integer) 1
> hset hash-key sub-key2 value2
(integer) 1
> hset hash-key sub-key1 value1
(integer) 0

# 获取 key 和 value
> hgetall hash-key
1) "sub-key1"
2) "value1"
3) "sub-key2"
4) "value2"

# 删除 key 对应的 value 也会同时被删除 
> hdel hash-key sub-key2
(integer) 1
> hdel hash-key sub-key2
(integer) 0

# 通过 key 获取对应的 value 值
> hget hash-key sub-key1
"value1"

> hgetall hash-key
1) "sub-key1"
2) "value1"

```

### Key 的过期时间

Redis 可以为每个键设置过期时间，当键过期时，会自动删除该键。

对于散列表这种容器，只能为整个键设置过期时间（整个散列表），而不能为键里面的单个元素设置过期时间。 

```
> SET cache_page "www.google.com"
OK

> EXPIRE cache_page 30  # 设置过期时间为 30 秒
(integer) 1

> TTL cache_page    # 查看剩余生存时间
(integer) 23

> EXPIRE cache_page 30000   # 更新过期时间
(integer) 1

> TTL cache_page
(integer) 29996
```



## FQA

1. key不要太长，尽量不要超过1024字节，这不仅消耗内存，而且会降低查找的效率

2. key也不要太短，太短的话，key的可读性会降低

3. 在一个项目中，key最好使用统一的命名模式，例如user:10000:passwd。

    

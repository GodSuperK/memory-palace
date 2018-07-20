# Redis

## Redis 基本命令

```shell
# 启动 redis 服务器端
redis-server
# 启动 redis 客户端
redis-cli
```



## Redis 数据结构

### 字符串 (strings)

```redis
// 设置字符串类型
set mystr "Hello world!"
// 读取字符串类型
get mystr
// 因为是二进制安全的，所以你完全可以把一个图片文件的内容作为字符串来存储。
```



### 字符串列表 (lists)



### 字符串集合 (sets)



### 有序字符串集合 (sorted sets)



### 哈希 (hashes)





## FQA

1. key不要太长，尽量不要超过1024字节，这不仅消耗内存，而且会降低查找的效率

2. key也不要太短，太短的话，key的可读性会降低

3. 在一个项目中，key最好使用统一的命名模式，例如user:10000:passwd。

    
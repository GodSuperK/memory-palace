# Mysql

1. 关系型数据库(SQL)将数据存储到磁盘之中， 数据存储在特定结构的表中, DBMS: Oracle, MySQL, SQL Server
2. 非关系型数据库(NoSQL)将数据存储到内存中， 存储方式比较灵活， DBMS: MongoDB, Redis

## 基本命令

```shell
# 连接 Mysql 服务器
mysql -uroot -pqwe123
# Ubuntu 关闭 Mysql 服务
sudo service mysql stop
# Ubuntu 启动 Mysql 服务
sudo service mysql start
```

## 库级操作语句

```mysql
# 退出 Mysql 客户端 
exit; 
# 显示所有库
show databases;
# 创建库
create database [if not exists] db_name;
# 删除库
drop database [if exists] db_name;
# 切换数据库
use db_name;
# 查看当前位于哪个数据库
select database();
```

## 表级操作语句

```mysql
# 显示所有的表
show tables;
# 创建表
create table tbl_name(create_definition, ...);
# 显示创建表的信息
show create table tbl_name;
# 删除表
drop table tbl_name;
# 显示表的结构
desc tbl_name;
```

## 用户管理

```shell
# 创建用户
create user 'user_name'@'%' identified by 'user_password';
# 赋予所有权限
grant all on *.* to 'user_name'@'%';
# 使权限生效
flush privileges;
# 查看当前用户
select user();
```



## C

```mysql
# 指定列插入, 
insert [into] tbl_name(col_name,...) values(col_value,...);
# 全列插入，需要给所有列赋值
insert [into] tbl_name values(value1, ...);
# 多行插入
insert [into] tbl_name values(all_values), (all_values), ...;
```

## R

```mysql
# 指定列查询
select col_name, ... from tbl_name;
# 全列查询
select * from tbl_name;
# where 子句
select col_names from tbl_name where conditions;
```

## U

```mysql
# 修改表中所有的记录
update tbl_name set field_1=value_1, ...;
# 修改表中指定的数据
update tbl_name set field_1=value_1, ... where conditions;
```

## D

```mysql
# 删除表中所有数据
delete from tbl_name;
# 删除表中满足条件的数据
delete from tbl_name where conditons;
```

## 数据类型

### 数值类型

| 类型         | 大小(byte) | 范围                     |
| ------------ | ---------- | ------------------------ |
| TINYINT      | 1          | 0~255                    |
| SMALLINT     | 2          | 0~65535                  |
| MEDIUMINT    | 3          | 0~16777215               |
| INT          | 4          | 0~4294967295             |
| BIGINT       | 8          |                          |
| FLOAT(M, N)  | 4          | M是总位数，N是小数的位数 |
| DOUBLE(M, N) | 8          |                          |



### 字符类型

| 类型                | 功能                                                         | 最大字符数量 |
| ------------------- | ------------------------------------------------------------ | ------------ |
| CHAR(size)          | 保存固定长度的字符串，在括号中指定字符串的长度               | 255          |
| VARCHAR(size)       | 保存可变长度的字符串，在括号中指定字符串的最大长度。如果值的长度大于255，则被转换为TEXT类型 | 255          |
| TINYTEXT / TINYBLOB | 用来存放较短文本数据/二进制数据                              | 255          |
| TEXT / BLOB         | 用来存放长文本数据/二进制数据                                | 65535        |
| LONGTEXT / LONGBLOB | 同上                                                         | 4294967295   |
| ENUM                | ENUM 类型的数据实际上是一个包含多个固定值的列表， 只能选择这些值（包括NULL值）。例如，如果希望某个字段包含"A", "B", 和 "C", 必须这样定义：ENUM('A', 'B', 'C'), 只有这些值（或NULL值）能够填充到该字段中。 |              |

### 时间日期类型

| 类型      | 用法                                 |
| --------- | ------------------------------------ |
| DATE      | 日期,  格式： 2014-09-18             |
| TIME      | 时间,  格式： 08:42:30               |
| DATETIME  | 日期时间， 格式：2014-09-18 08:42:30 |
| TIMESTAMP | 自动存储记录修改的时间               |
| YEAR      | 存放年                               |

### 常用数据类型

| 数据类型                | 代表内容                                              | 示例                                     |
| ----------------------- | ----------------------------------------------------- | ---------------------------------------- |
| int                     | 整型                                                  | id int                                   |
| varchar(20)             | 指定长度，最多65535个字符。**变长**（超出会自动截掉） | name varchar(20)（插入20个字符）         |
| char(4)                 | 指定长度，最多255个字符。**定长**                     | sex char(4)（不管插入几个字符都会占4个） |
| double(4,2)             | 双精度浮点型，m总个数，d小数位                        | price double(4,2)                        |
| text                    | 可变长度，最多65535个字符                             | detail text                              |
| datetime                | 日期时间类型YYYY-MM-DD HH:MM:SS                       | dates datetime                           |
| enum('good','not good') | 枚举，在给出的value中选择                             | ping enum('good','not good')             |



## 注意事项

1. 语句结束符： 每个语句都以；或\G结束
2. 大小写： 不严格区分大小写， 默认大写为程序代码， 小写为程序员写的代码
3. 类型： 强制数据类型，任何数据都有自己的类型
4. 逗号， 创建表最后一列不需要逗号
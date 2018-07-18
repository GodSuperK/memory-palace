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

### 约束条件

> 约束是一种限制， 通过对表中的数据做出限制，来确保表中数据的完整性，唯一性。

|                |                                                              |
| -------------- | ------------------------------------------------------------ |
| default        | 初始值设置，插入记录时，如果没有明确为字段指定值，则自动赋予默认值 |
| not null       | 限制一个字段的值不能为空，插入记录时必须添加该字段           |
| unique key     | 确保字段中的值唯一                                           |
| auto_increment | 自动编号，一般与主键组合使用。一个表里面只有一个自增，默认情况下，起始值为1， 每次的增量为1 |
| primary key    | 唯一标识一条记录， 每张表里只能有一个主键                    |
| foreign key    | 保持数据一致性，完整性实现一对多关系                         |

#### 如何定义外键？

```mysql
# 在创建表的时候，添加外键
constraint [foreign_key_name] foreign key(self_field_name) references other_tbl_name(field_name)

# 修改表结构的时候添加外键关系
alter table tbl_name add constraint [foreign_key_name] foreign key(self_field_name) references other_tbl_name(field_name);

# 删除外键关系
alter table tbl_name drop foreign key foreign_key_name;
# 再去删除用来保存外键关系的字段
alter table tbl_name drop field_name;
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

### 子查询

```mysql
# 将一个表的查询结果当做另一个表的条件
select columns from tbl1 where field = (select field from tbl2)
```

### 连接查询

```mysql
# 交叉连接， 又名笛卡尔连接，它列出了所有情况，其中一定有你需要的组合
# 排列组合 tbl1 和 tbl2 然后将结果 再与 tbl3 排列组合， 最后输出查询结果
select columns from tbl1 join tbl2 join tbl3;

# 内连接 就是添加条件过滤交叉连接的所有情况
select columns from tbl1 join tbl2 on conditions join tbl3 on conditions;
```



### 事务

```mysql
# 开启事务
begin;
# 回滚
rollback;
# 提交事务
commit;
```



### 其他配置管理

`mysql`配置文件的位置：

1. 全局配置文件：`/etc/mysql/mysql.conf.d/mysqld.cnf` `/etc/mysql/my.cnf`
2. 用户配置文件：`~/.my.cnf`

```mysql
# 用户管理
#查看编码
show variables like '%char%';	

#查看用户
select user,host from mysql.user;
#查看用户权限
show grants for 'abu';
#刷新授权
flush privileges;					

#创建用户
create user 'abu'@'%' identified by '123456';
#赋予所有权限
grant all on *.* to 'abu'@'%';
#移除权限
revoke all on *.* from 'abu'@'%';							

# 修改登陆权限
# localhost 表示只能本地连接， % 表示可以远程连接
update user set host ='localhost' where user='abu';

# 修改密码
set password for '用户名'@'登录地址'=password('密码')
#修改当前账号密码
set password = password("newpassword");		
                                           
# 删除用户
drop user 'test'@'localhost';
```



#### 常用权限

| 权限   | 作用             |
| ------ | ---------------- |
| all    | 允许做任何事情   |
| usage  | 只允许登陆       |
| alter  | 修改已经存在的表 |
| create | 创建表或库       |
| select | 查找数据         |
| update | 修改数据         |
| insert | 增加表的记录     |
| delete | 删除表的记录     |
| drop   | 删除库或表       |




## 注意事项

1. 语句结束符： 每个语句都以；或\G结束
2. 大小写： 不严格区分大小写， 默认大写为程序代码， 小写为程序员写的代码
3. 类型： 强制数据类型，任何数据都有自己的类型
4. 逗号， 创建表最后一列不需要逗号

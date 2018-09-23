# How to install mysql 5.7 on Ubuntu 18.04?

[See Also](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-18-04)

## 1. 安装 Mysql
```shell
sudo apt update
suo apt install mysql-server
```

## 2. 配置 Mysql
**1. 设置密码策略，root 密码等等, 这一步完成后还是不能用密码登陆。**
```shell
sudo mysql-secure-installation
```
**2. 调整用户身份验证和权限**

```shell
sudo mysql #进入mysql 数据库
```

输入mysql命令：

```mysql
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';
FLUSH PRIVILEGES;
```

完成以上步骤后，就可以使用密码登陆了 

## 3. 管理 Mysql服务
```shell
systemctl status mysql.service
sudo systemctl start mysql.service
sudo systemctl stop mysql.service
sudo systemctl restart mysql.service
```

## 4. 卸载 Mysql
```shell
# 查看mysql的所有依赖
dpkg --list|grep mysql
sudo apt purge mysql-common
sudo apt purge mysql-client-core-5.7
sudo apt purge mysql-server-core-5.7

```

## Mysql 配置文件 
`/etc/mysql/mysql.conf.d/mysqld.cnf`


### 在运行时修改字符集和字符序
如果不指定字符序，则使用字符集默认的字符序

```mysql
show variables like "%char%";
set character_set_database="utf8";
set character_set_server="utf8";
```

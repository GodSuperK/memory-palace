# How to install mysql 5.7 on Ubuntu 18.04?

[See Also](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-18-04)

## 安装 Mysql
```shell
sudo apt update
suo apt install mysql-server
```

## 配置 Mysql
**1. 设置密码策略，root 密码等等, 这一步完成后还是不能用密码登陆。**
```shell
sudo mysql-secure-installation
```
**2. 调整用户身份验证和权限**
    1. `sudo mysql #进入mysql 数据库`
    2. 输入mysql命令：
	- `ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';`
	- `FLUSH PRIVILEGES;`
    3. 现在就可以使用密码登陆了 

## 管理 Mysql服务
```shell
systemctl status mysql.service
sudo systemctl start mysql.service
sudo systemctl stop mysql.service
sudo systemctl restart mysql.service
```

## 卸载 Mysql
```shell
# 查看mysql的所有依赖
dpkg --list|grep mysql
sudo apt purge mysql-common
sudo apt purge mysql-client-core-5.7
sudo apt purge mysql-server-core-5.7

```

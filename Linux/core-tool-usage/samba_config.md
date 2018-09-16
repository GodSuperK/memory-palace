# Linux 系统配置Samba服务
Samba服务类似于windows上的共享功能，可以实现在Linux上共享文件，Windows也可以访问。
是一种在局域网上共享文件和打印机的一种通信协议，它为局域网内的不同计算机之间提供文件及打印机等资源的共享服务。

## Install 
`sudo apt install samba`

## Config
**配置文件：** /etc/samba/smb.conf
**服务器名称:** smbd.service

### samba 实践
> 要求共享一个目录，任何人都可以访问，即不用输入密码即可访问，要求只读。

```shell
# 1. 建立共享目录 
mkdir ~/myshare
# 2. 添加字用户 (假设我的ubuntu用户名为:test)
sudo pdbedit -a -u test 
# 3. 修改配置文件,在末尾添加以下内容
sudo vim /etc/samba/smb.conf
```

```
[myshare]
path=/home/myshare  
public=yes
writable=no
browseable=yes
```




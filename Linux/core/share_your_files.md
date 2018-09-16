# How to share your files(to othre computer user)?

## 从 Linux 访问 Windows 上的共享文件夹 
1. 安装SMB协议 `sudo apt install cifs-utils`
2. 创建一个新的空的文件夹作为共享文件夹的挂载点
3. 挂载共享文件夹到我们的Linux File Tree 上
    ```shell
    //sudo mount.cifs //目标主机的IP/共享文件夹的名称 挂载点 -o user=访问身份 
    // 提示输入密码的时候，直接回车即可。一般目标主机提供的Guest用户都是免密登陆
    sudo mount.cifs //192.168.1.108/shichao ~/mnt/share -o user=Guest
    ```

4. 不需要访问时 直接卸载掉挂载点即可 `sudo umount ~/mnt/share`

## 从 Windows 访问 Linux 上的共享文件夹
> [参见samba的搭建](../core-tool-usage/samba_config.md) 




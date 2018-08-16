# Ubuntu Grub Rescue 问题(ubuntu 18.04)

1. 先使用ls 命令， 找到 Ubuntu 安装在哪个分区：`grub rescue> ls`, 会罗列所有的磁盘分区信息
2. 然后依次查看每个分区 `grub rescue> ls (hd0, X)/grub`， 如果显示了文件夹中文件，表示Linux 安装在这个分区
3. 调用如下命令, 系统会自动重启

```shell
grub rescue> set root=(hd0,X)
grub rescue> set prefix=(hd0,X)/grub
grub rescue> insmod normal
grub rescue> normal
```

4. 如果重启，问题依旧存在，则在linux中对grub进行修复

```shell
sudo update-grub
sudo grub-install /dev/sdb # 不能指定分区号码，指定系统安装的分区
```

5. Finish!
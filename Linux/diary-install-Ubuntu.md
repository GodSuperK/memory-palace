# Ubuntu(18.04) 安装日记

> 将 Ubuntu 打造成一个超级银河战舰



## 1. 系统安装篇

**硬件清单**

```
1. Processor i5-3320M CPU @ 2.60GHZ x 4
2. Memory 7.5 GiB
3. Disk 128GB SSD + 500GB SATA
```

**分区表**

```scheme
sda1 /swap swap 7.6G
sda2 /home ext4 458.1G
sdb1 /boot ext4 476M
sdb2 /     ext4 47.7G
sdb3 /usr  ext4 71.1G
```



## 2. 系统美化篇

首先，安装Gnome主题管理工具 Tweaks，`sudo apt install gnome-tweak-tool`

[GNOME-LOOK.ORG](https://www.gnome-look.org) - gnome 主题整合网站

**Applications**

在用户家目录下，新建`.themes`目录管理图标主题，将网络上下载的图标压缩包解压后，将里面的目录移动到 `.themes`目录下，即可用 tweaks 进行管理。

推荐主题：

- Vimix



**Icons**

在用户家目录下，新建`.icons`目录管理图标主题，将网络上下载的图标压缩包解压后，将里面的目录移动到 `.icons`目录下，即可用 tweaks 进行管理。

推荐主题：

- Papirus



**壁纸网站**

- http://simpledesktops.com/browse/



## 3. 软件安装篇

1. 使用TUNA的软件源镜像

> Ubuntu 的软件源配置文件是 `/etc/apt/sources.list`。将系统自带的该文件做个备份，将该文件替换为下面内容，即可使用 TUNA 的软件源镜像。

```
# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-security main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-security main restricted universe multiverse

# 预发布软件源，不建议启用
# deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-proposed main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-proposed main restricted universe multiverse
```

1. **软件清单**

```
1. Albert - A desktop agnostic launcher.
2. Google Chrome - Access the Internet.
3. Atom - A hackable text editor for the 21st Century.
4. Typora - A markdown editor, markdown reader.
5. DeepinScrot - 截图工具
```

2. **中文输入法配置**
   1. 安装智能拼音输入法`sudo apt install ibus-pinyin`
   2. 在 `settings -> Region & Language -> Input Sources ` 里点击 `Manage Installed Languages` ， 修改 `Keyboard input method system` 为 `IBus`
   3. 点击`+`号 添加 `Chinese(Intelligent Pinyin)` 

3. **安装Git:** `sudo apt install git`

4. **安装Oh-my-zsh:** 

   ```shell
   sudo apt install zsh
   chsh -s /bin/zsh
   sudo apt install curl
   sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
   # 安装插件highlight, 高亮语法
   cd ~/.oh-my-zsh/custom/plugins
   git clone git://github.com/zsh-users/zsh-syntax-highlighting.git
   # 在配置文件中(~/.zshrc)添加插件
   # plugins=(plugins... zsh-syntax-highlighting)
   source ~/.zshrc
   ```

5. **安装gnome shell扩展插件**  - 通过Ubuntu Software 搜索安装即可

   - NetSpeed - 监控网速
   - Coverflow Alt-Tab - 优化 Alt-Tab

6. **安装Albert**

   ```shell
   # 添加软件源密钥
   sudo wget -nv -O Release.key \
     https://build.opensuse.org/projects/home:manuelschneid3r/public_key
   sudo apt-key add - < Release.key
   sudo apt-get update
   # 添加软件源
   sudo sh -c "echo 'deb http://download.opensuse.org/repositories/home:/manuelschneid3r/xUbuntu_18.04/ /' > /etc/apt/sources.list.d/home:manuelschneid3r.list"
   sudo apt-get update
   sudo apt-get install albert
   ```

7. **安装Google Chrome**

   ```shell
   sudo apt install gdebi-core
   wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
   sudo gdebi google-chrome-stable_current_amd64.deb
   ```

8. **安装Typora**
   ```shell
   # optional, but recommended
   sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys BA300B7755AFCFAE
   # add Typora's repository
   sudo add-apt-repository 'deb https://typora.io/linux ./'
   sudo apt-get update
   # install typora
   sudo apt-get install typora
   ```

9. **安装DeepinScrot:**

   ```shell
   sudo apt-get install python-gtk2
   sudo apt-get install afnix
   wget http://packages.linuxdeepin.com/deepin/pool/main/d/deepin-scrot/deepin-scrot_2.0-0deepin_all.deb
   sudo dpkg -i deepin-scrot_2.0-0deepin_all.deb
   deepin-scrot
   ```

   推荐配置快捷键使用 `ctrl+shift+4`

10. 

## 4. 开发环境搭建篇

### 1. Vim 配置
[See this](vim_comfig.md)
### 2. Python3.X 开发环境搭建

```shell
# 安装pip3
sudo apt install python3-pip
# 安装 virtualenv
pip3 install virtualenv
# 安装 virtualenvwrapper
pip3 install virtualenvwrapper
# 安装Pycharm 
sudo snap install pycharm-professional --classic
```

## 5. Tips



## 6. 继续学习篇

1. [Basic snap usage](basic_snap_usage.md)

## 7. FQA

1. 安装结束时报错：**Error removing initramfs-tools**

   > boot 分区太小导致，重新安装系统为boot 分区分配200M 

2. 开机启动进入**grub secure mod**

   > see grub_fix.md

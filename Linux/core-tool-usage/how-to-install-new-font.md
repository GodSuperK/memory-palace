# Linux 下安装新字体

## 1. 下载字体ttf文件
  - [字体传奇](http://www.ziticq.com/)
  - [CYhd](http://www.cyhd.net/html/resources/fonts/)
## 2. 创建新字体文件的目录
```shell
sudo mkdir -p /usr/share/fonts/truetype/your_dir
```
## 3. 将字体文件移动到新创建的目录中
```shell
sudo cp your_font_dir /usr/share/share/fonts/truetype/your_dir
```
## 4. 修改字体文件的权限
```shell
sudo chmod 644 Charlevoix-Bold.otf
```
## 5. 安装字体
```shell
sudo mkfontscale
# 创建字体的fonts.scale文件，它用来控制字体旋转缩放
sudo mkfontdir
# 创建字体的fonts.dir文件，它用来控制字体粗斜体产生
sudo fc-cache -fv
# 建立字体缓存信息，也就是让系统认识该字体
```


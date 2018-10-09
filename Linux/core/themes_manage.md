# 为你的 Ubuntu 添加额外主题

## 1. communitheme

Yaru，以前称为Communitheme，是社区建立的新Ubuntu主题。 Yaru将成为Ubuntu 18.10中默认的Ubuntu主题。 这个包允许你在Ubuntu 18.04 LTS上试用这个主题。

要试用该主题，请在Ubuntu 18.04 LTS上安装此软件包，重新启动计算机并从登录屏幕中选择“带有Communitheme snap的Ubuntu”会话。

## 2. Install theme 

[主题网站](https://www.gnome-look.org)

1. Shell themes
2. GTK3 themes
3. Cursors
4. Icons



## 3. GTK3 themes Recommended

1. [Canta theme](https://www.gnome-look.org/p/1220749/)

   ![](pics/canta_theme.png)

下载以下文件

1. [Canta.tar.xz](https://www.gnome-look.org/p/1220749/startdownload?file_id=1538352752&file_name=Canta.tar.xz&file_type=application/x-xz&file_size=305640&url=https%3A%2F%2Fdl.opendesktop.org%2Fapi%2Ffiles%2Fdownload%2Fid%2F1538352752%2Fs%2F4e8cc98f2af636454d6cb8f0fe258680%2Ft%2F1539069061%2Fu%2F%2FCanta.tar.xz)
2. [Canta-icon-theme.tar.xz](https://www.gnome-look.org/p/1220749/startdownload?file_id=1520781248&file_name=Canta-icon-theme.tar.xz&file_type=application/x-xz&file_size=771208&url=https%3A%2F%2Fdl.opendesktop.org%2Fapi%2Ffiles%2Fdownload%2Fid%2F1520781248%2Fs%2F4e8cc98f2af636454d6cb8f0fe258680%2Ft%2F1539069061%2Fu%2F%2FCanta-icon-theme.tar.xz)
3. [wallpaper.tar.xz](https://www.gnome-look.org/p/1220749/startdownload?file_id=1520598111&file_name=wallpaper.tar.xz&file_type=application/x-xz&file_size=649928&url=https%3A%2F%2Fdl.opendesktop.org%2Fapi%2Ffiles%2Fdownload%2Fid%2F1520598111%2Fs%2F4e8cc98f2af636454d6cb8f0fe258680%2Ft%2F1539069061%2Fu%2F%2Fwallpaper.tar.xz)

解压文件, 将主题移动到`~/.themes`， 将图标移动到`~/.icons`

然后安装Gnome 主题管理工具 `Gnome Tweaks`, 安装好后，默认不能修改shell主题, 需要安装`User Themes` extension



最后安装Numix Circle icons

![](pics/numix-icon-circle.png)

1. [项目地址](https://github.com/numixproject/numix-icon-theme-circle)

2. 执行以下命令

   ```shell
   sudo add-apt-repository ppa:numix/ppa
   sudo apt update
   sudo apt install numix-icon-theme-circle
   ```



## 4. 自定义dock

1. 可以将dock 放置在left right bottom，也可以修改dock 上图标的大小，直接在settings->dock选项里修改即可
2. 自定义显示所有应用程序的图标(show applications)的位置， 安装`Dconf Editor`，启动dconf， 然后搜索`show-apps-at-top`，选中该选项， 可以将其移动到dock的顶部
3. 模仿windows的样式，安装`Dash to Panel`， 安装`Arc Menu`

   ![](pics/win_theme.png)

## 5. Mac OS X Old Outlook

1. Install `Dash to Dock`
2. Visit [Cupertino iCons](https://www.gnome-look.org/p/1102582)
   - Download [macOS11.tar.xz](https://www.gnome-look.org/p/1102582/startdownload?file_id=1533641153&file_name=macOS11.tar.xz&file_type=application/x-xz&file_size=27283920&url=https%3A%2F%2Fdl.opendesktop.org%2Fapi%2Ffiles%2Fdownload%2Fid%2F1533641153%2Fs%2Fa6394dee78c247aab5edc5b6cc75d37d%2Ft%2F1539075950%2Fu%2F%2FmacOS11.tar.xz)
3. Visit [McOS-themes](https://www.gnome-look.org/p/1241688)
   - Download [McOS-Shell-themes.tar.xz](https://www.gnome-look.org/p/1241688/startdownload?file_id=1529367872&file_name=McOS-Shell-themes.tar.xz&file_type=application/x-xz&file_size=37268&url=https%3A%2F%2Fdl.opendesktop.org%2Fapi%2Ffiles%2Fdownload%2Fid%2F1529367872%2Fs%2Fb43ad14bbda3d123c7cb52e2b10b5173%2Ft%2F1539075611%2Fu%2F%2FMcOS-Shell-themes.tar.xz)
   - Download [McOS-MJV-1.1.tar.xz](https://www.gnome-look.org/p/1241688/startdownload?file_id=1537911100&file_name=McOS-MJV-1.1.tar.xz&file_type=application/x-xz&file_size=442636&url=https%3A%2F%2Fdl.opendesktop.org%2Fapi%2Ffiles%2Fdownload%2Fid%2F1537911100%2Fs%2Fb43ad14bbda3d123c7cb52e2b10b5173%2Ft%2F1539075611%2Fu%2F%2FMcOS-MJV-1.1.tar.xz)

## 6. Mac OS X Newest Outlook 

1. [themes](https://www.gnome-look.org/p/1013714/)
   - download [Sierra-light-solid.tar.xz](https://www.gnome-look.org/p/1013714/startdownload?file_id=1538628368&file_name=Sierra-light-solid.tar.xz&file_type=application/x-xz&file_size=200204&url=https%3A%2F%2Fdl.opendesktop.org%2Fapi%2Ffiles%2Fdownload%2Fid%2F1538628368%2Fs%2F4e7b4b9809fbc808956de71aefa63840%2Ft%2F1539078940%2Fu%2F%2FSierra-light-solid.tar.xz)
   - download [MacOSX-icon-theme.tar.xz](https://www.gnome-look.org/p/1013714/startdownload?file_id=1524634947&file_name=MacOSX-icon-theme.tar.xz&file_type=application/x-xz&file_size=23631624&url=https%3A%2F%2Fdl.opendesktop.org%2Fapi%2Ffiles%2Fdownload%2Fid%2F1524634947%2Fs%2F4e7b4b9809fbc808956de71aefa63840%2Ft%2F1539078940%2Fu%2F%2FMacOSX-icon-theme.tar.xz)
   - download [HighSierra-wallpapers.tar.xz](https://www.gnome-look.org/p/1013714/startdownload?file_id=1517131134&file_name=HighSierra-wallpapers.tar.xz&file_type=application/x-xz&file_size=45587296&url=https%3A%2F%2Fdl.opendesktop.org%2Fapi%2Ffiles%2Fdownload%2Fid%2F1517131134%2Fs%2F4e7b4b9809fbc808956de71aefa63840%2Ft%2F1539078940%2Fu%2F%2FHighSierra-wallpapers.tar.xz)
2. [cursors](https://www.gnome-look.org/p/1241071/)
   - download [El_Capitan_CursorsMOD.zip](https://www.gnome-look.org/p/1241071/startdownload?file_id=1529063944&file_name=El_Capitan_CursorsMOD.zip&file_type=application/zip&file_size=125654&url=https%3A%2F%2Fdl.opendesktop.org%2Fapi%2Ffiles%2Fdownload%2Fid%2F1529063944%2Fs%2F07b4a3956c55ee8a50d600500c11a1af%2Ft%2F1539079327%2Fu%2F%2FEl_Capitan_CursorsMOD.zip)
3. [shell themes](https://www.gnome-look.org/p/1213208/)
   - download [OSX.for.Dash.to.DOCK.tar.xz](https://www.gnome-look.org/p/1213208/startdownload?file_id=1527085913&file_name=OSX.for.Dash.to.DOCK.tar.xz&file_type=application/x-xz&file_size=932544&url=https%3A%2F%2Fdl.opendesktop.org%2Fapi%2Ffiles%2Fdownload%2Fid%2F1527085913%2Fs%2F83a19f1670ed97d228df04c05f18e773%2Ft%2F1539079997%2Fu%2F%2FOSX.for.Dash.to.DOCK.tar.xz)
   - download [OSX.for.Dash.to.PANEL.tar.xz](https://www.gnome-look.org/p/1213208/startdownload?file_id=1527085882&file_name=OSX.for.Dash.to.PANEL.tar.xz&file_type=application/x-xz&file_size=222704&url=https%3A%2F%2Fdl.opendesktop.org%2Fapi%2Ffiles%2Fdownload%2Fid%2F1527085882%2Fs%2F83a19f1670ed97d228df04c05f18e773%2Ft%2F1539079997%2Fu%2F%2FOSX.for.Dash.to.PANEL.tar.xz)
   - download [Retina Wallpapers.tar.xz](https://www.gnome-look.org/p/1213208/startdownload?file_id=1518654128&file_name=Retina%20Wallpapers.tar.xz&file_type=application/x-xz&file_size=24641268&url=https%3A%2F%2Fdl.opendesktop.org%2Fapi%2Ffiles%2Fdownload%2Fid%2F1518654128%2Fs%2F83a19f1670ed97d228df04c05f18e773%2Ft%2F1539079997%2Fu%2F%2FRetina%20Wallpapers.tar.xz)
4. [GDM themes](https://www.gnome-look.org/p/1207015)


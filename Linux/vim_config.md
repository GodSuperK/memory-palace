# Vim Config



# Vundle 插件管理

一个全自动的插件管理器，让我们通过维护插件列表的方式管理插件。

1. Install Vundle

   ```shell
   # 下载Vundle仓库到 ~/.vim/bundle/Vundle.vim 目录中
   git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
   # 配置Vundle
   vim ~/.vim/vimrc
   ```

   将以下内容添加到 ~/.vim/vimrc 文件中

   ```vim
   " Vundle Section Start
   set nocompatible
   filetype off
   set rpt+=~/.vim/bundle/Vundle.vim
   call vundle#begin()
   Plugin 'VundleVim/Vundle.vim'
   " ADD YOUR PLUGIN
   call vundle#end() 
   filetype plugin indent on
   " Vundle Section End
   ```

2.  如何添加插件

   将插件添加在" ADD YOUR PLUGIN 的下面， 格式为 Plugin 'path'

   path 的格式：

   - Github仓库中的插件， 安装时可以省略github域名。例如： `github.com/scrooloose/nerdtree`, 可以写为 `/scrooloose/nerdtree`
   - 虽然在Github仓库中，但是插件不在根目录下，在指定目录下，例如vim目录下 `github.com/rstacruz/sparkup`, 写为 `rstacruz/sparkup, {'rtp': 'vim/'}` 
   - 位于vim官方插件列表中的插件，也就是 github.com/vim-scripts中的插件，这部分可以直接输入插件名。例如`github.com/vim-scripts/L9`, 可以直接写为 `'L9'`
   - 本地插件，此时使用file前缀，并写上绝对路径，例如：`file:///home/simple/path/to/plugin`

3. 如何管理插件

   ```shell
   :PluginList " 列出列表中的插件
   :PluginInstall " 安装插件
   :PluginUpdate " 更新插件
   :PluginClean " 清理不在列表中的插件
   :PluginClean! " 清理时不需用户同意
   ```

   - 安装插件： 打开vim，输入命令`:PluginInstall` , 就会安装添加在`vimrc`文件中的插件
   - 删除插件：在`vimrc`文件中删除，然后重启vim，输入`:PluginClean`，vundle就会帮我们删除它。

4. 插件推荐

   ```
   https://github.com/scrooloose/nerdtree - 文件系统资源管理器。 
   https://github.com/Lokaltog/vim-powerline - 增强版状态栏
   https://github.com/nathanaelkane/vim-indent-guides - 可视化缩进
   ```


## 主题管理

推荐三款主题：

- 素雅 solarized（<https://github.com/altercation/vim-colors-solarized> ）
- 多彩 molokai（<https://github.com/tomasr/molokai> ）
- 复古 phd（<http://www.vim.org/scripts/script.php?script_id=3139> ）

 每款主题都有暗/亮之分，这样3种主题共有6种风格。

**安装主题的方法:**

将主题文件添加到 `~/.vim/colors/`目录中：

```shell
git clone https://github.com/altercation/vim-colors-solarized.git
cd vim-colors-solarized/colors
mv solarized.vim ~/.vim/colors/
```

修改 `~/.vim/vimrc` 文件：

```
syntax enable
set background=dark
colorscheme solarized
```



如何让gvim全屏？

安装图形vim `sudo apt install vim-gnome`
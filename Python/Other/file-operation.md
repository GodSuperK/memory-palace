# Python 操作文件和目录

> 在Python中对文件和目录的操作经常用到 os 模块和 shutil 模块。

- 获得当前Python脚本工作的目录路径：`os.getcwd() -> str`
- 返回指定目录下的所有文件和目录名：`os.listdir() -> list`
- 删除一个文件：`os.remove(filepath)`
- 删除多个空目录：`os.removedirs()`
- 检验给出的路径是否是一个文件：`os.path.isfile(filepath) -> bool`
- 检验给出的路径是否是一个目录：`os.path.isdir(filepath) -> bool`
- 判断是否是绝对路径： `os.path.isabs() -> bool`
- 检验路径是否真的存在：`os.path.exists() -> bool`
- 分离一个路径的目录名和文件名：`os.path.split() -> tuple`
- 分离扩展名：`os.path.splitext() -> tuple`
- 获取路径名：`os.path.dirname(filepath) -> str`
- 获取文件名：`os.path.basename(filepath) -> str`
- 读取和设置环境变量：`os.getenv(key) os.putenv(key, name)`
- 获取当前平台使用的行终止符：`os.linesep -> str`
- 指示你正在使用的平台：`os.name -> str`， 对于Windows, 它是'nt', 对于Linux/Unix用户，它是'posix'
- 重命名文件或者目录：os.rename(old, new)
- 创建多级目录，相当于`mkdir -p `：` os.makedirs(filepath)`
- 创建单个目录：`os.mkdir(filepath)`
- 获取文件属性：`os.stat(file) -> os.stat_result`
- 修改文件权限与时间戳：`os.chmod(file)`
- 获取文件大小：`os.path.getsize(filename)`
- 递归的复制目录：`shut.copytree('old dir', 'newdir')`  newdir 必须不存在
- 复制文件：`shutil.copyfile('old file', 'new file')` newfile可以是文件，也可以是目标目录
- 移动文件(目录)：`shutil.move('oldpos', 'newpos')`
- 删除空目录：`os.rmdir('dir')`
- 删除目录：`shutil.rmtree('dir')`，有内容的目录也可以删除
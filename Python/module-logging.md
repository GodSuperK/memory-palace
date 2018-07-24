### logging



## Sample Use

#### You need know

1. 默认过滤级别为warning，默认输出到控制台

```python
import logging

logging.critical("This is critical!")
logging.error("This is error!")
logging.warning("This is warning!")
logging.info("This is info!")
logging.debug("This is debug!")
```

2. 配置日志的过滤级别

```python
# critical(50)>error(40)>warning(30)>info(20)>debug(10)
logging.basicConfig(level=logging.DEBUG)
```

3. 配置日志的输出位置,  默认 filemode = "a" 表示追加

```python
logging.basicConfig(filename="mylog.log")
```

4. 配置日志的输出格式

```python
"""format参数中可能用到的格式化串
%(name)s Logger的名字
%(levelno)s 数字形式的日志级别
%(levelname)s 文本形式的日志级别
%(pathname)s 调用日志输出函数的模块的完整路径名，可能没有
%(filename)s 调用日志输出函数的模块的文件名
%(module)s 调用日志输出函数的模块名
%(funcName)s 调用日志输出函数的函数名
%(lineno)d 调用日志输出函数的语句所在的代码行
%(created)f 当前时间，用UNIX标准的表示时间的浮 点数表示
%(relativeCreated)d 输出日志信息时的，自Logger创建以 来的毫秒数
%(asctime)s 字符串形式的当前时间。
            默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
%(thread)d 线程ID。可能没有
%(threadName)s 线程名。可能没有
%(process)d 进程ID。可能没有
%(message)s用户输出的消息
"""
log_format = ("%(asctime)s %(filename)s[line:%(lineno)d]"
              "%(levelname)s - %(message)s")
logging.basicConfig(format=log_format)
```

5. 配置日志的输出的时间格式

```python
"""
	m = 月
	d = 日
	Y = 年
	I = 时
	M = 分
	S = 秒
	p = PM or AM
"""
logging.basicConfig(datefmt="%m/%d/%Y %I:%M:%S %p")
```



## Advance

**流程**

1. 创建logger实例并配置
2. 创建formatter对象
3. 创建你需要的handler对象并配置
4. 将handler加载到logger实例中

```python
import logging

from logging import handlers
# 1. 创建logger实例
logger = logging.getLogger("ABU")
# 配置过滤级别
logger.setLevel(logging.INFO)
# 2. 创建格式化对象
fmt = ("%(asctime)s %(filename)s[line:%(lineno)d]"
             "%(levelname)s - %(message)s")
formatter = logging.Formatter(fmt=fmt, datefmt="%m/%d/%Y %I:%M:%S")
"""3. 创建handler对象
logging.StreamHandler - 向控制台输出日志 
logging.FileHandler - 向文件输出
	:parm filename: 文件名
	:parm mode: 文件的打开方式
logging.handlers.RotatingFileHandler - 文件达到一定大小之后，它会自动将当前
日志文件改名，然后创建 一个新的同名日志文件继续输出。比如日志文件是chat.log。当
chat.log达到指定的大小之后，RotatingFileHandler自动把文件改名为chat.log.1。
不过，如果chat.log.1已经存在，会先把chat.log.1重命名为chat.log.2。。。最后重新
创建 chat.log，继续输出日志信息
	:parm filename: 文件名
	:parm mode: 文件的打开方式
	:parm maxBytes: 用于指定日志文件的最大文件大小。如果maxBytes为0，意味着日志文件可以无限大
	:parm backupCount: 指定保留的备份文件的个数
logging.handlers.TimedRotatingFileHandler - 间隔一定时间就 自动创建新的日志文件
	:parm filename: 文件名
	:parm backupCount: 指定保留的备份文件的个数
	:parm when:一个字符串。表示时间间隔的单位，不区分大小写。
		它有以下取值：
			S 秒
			M 分
			H 小时
			D 天
			W 每星期（interval==0时代表星期一）
			midnight 每天凌晨
	:parm interval: 时间间隔
"""
console = logging.StreamHandler()
# 3. 配置 handler
console.setLevel(logging.WARNING)
console.setFormatter(formatter)
# 4. 将 handler 加载到 logger 实例中 
logger.addHandler(console)

logger.debug("debug")
logger.info("info")
logger.warning("warning")
logger.error("error")
logger.critical("critical message")
```

#### 创建 Handler

```python
console = logging.StreamHandler()

file_logging = logging.FileHandler("example.log")

file_rotating_file = handlers.RotatingFileHandler(
    "cat.log",maxBytes=1024,backupCount=3)

file_time_rotating = handlers.TimedRotatingFileHandler(
    "app.log",when="s",interval=10,backupCount=5)
```


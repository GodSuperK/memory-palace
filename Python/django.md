# Django Note

## Command

```shell
# 查看django版本
python3 -m django --version 
# 创建django项目
django-admin startproject xxx - Creating a project xxx
# 启动django自带的简易服务器(默认配置 listen http://127.0.0.1:8000/)
python3 manage.py runserver
# ditto (listen port 8080)
python3 manage.py runserver 8080
# ditto (listen all ip and port 8000)
python3 manage.py runserver 0:8000  - 0=0.0.0.0
# 创建django应用
python3 manage.py startapp xxx - Creating an app xxx
# 为已安装的应用创建数据表, 表的结构取决于每个应用的数据库迁移文件
python3 manage.py migrate
# 为已安装的应用创建数据库迁移文件
python3 manage.py makemigrations xxx - Creating migrations of xxx app
# 查看执行 migrate 命令所要执行的创建数据表的sql语句
python3 manage.py sqlmigrate xxx 001 - show create statement
# 检查项目中的问题
python3 manage.py check
# 启动交互式Python命令行 (manage.py 会设置DJANGO_SETTINGS_MODULE环境变量)
python3 manage.py shell
# 创建admin应用的管理员账号
python3 manage.py createsuperuser
# TODO(after deploying Django Project)
python3 manage.py collectstatic
# 运行测试
python3 manage.py test app_name
```



## settings.py
1. TIME_ZONE = 'Asia/Shanghai'
2. USE_TZ = False


## URLConf



## Models



## Views



## templates



## static files



## Django admin





## See Also

### 项目 VS 应用

> 项目和应用有啥区别？应用是一个专门做某件事的网络应用程序——比如博客系统，或者公共记录的数据库，或者简单的投票程序。项目则是一个网站使用的配置和应用的集合。项目可以包含很多个应用。应用可以被很多个项目使用


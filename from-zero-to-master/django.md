# Django

## Django项目启动流程
1. 创建项目

   ```shell
   django-admin startproject [project_name]
   ```

2. 创建应用

   ```shell
   python manage.py startapp [app_name]
   ```

3. 创建目录结构

   ```
   ├── apps - 管理应用
   ├── log  - 管理日志
   ├── manage.py
   ├── media - 管理用户上传的内容
   ├── project_name
   ├── static - 管理项目的静态文件
   └── templates - 管理项目的模板文件
   ```

4. 配置数据库

   使用 pymysql 作为 数据库驱动

   ```python
   # project_name/manage.py
   
   import pymysql
   
   pymysql.install_as_MySQLdb()
   ```

   配置数据库引擎等用户信息

   ```python
   # project_name/settings.py
   
   # Mysql的配置
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': "django",
           'USER': 'root',
           'PASSWORD': "Khalid0806.",
           'HOST': ""
       }
   }
   ```

5. 创建迁移，创建Django默认已安装应用的数据表

   ```shell
   python manage.py makemigrations
   python manage.py migrate
   ```

6. 配置项目模板路径

   ```python
   # project_name/settings.py
   
   TEMPLATES = [
       {   
           ...
           'DIRS': [os.path.join(BASE_DIR, 'templates')],
           ...   
       },
   ]
   ```

7. 配置项目静态文件路径

   ```python
   # project_name/settings.py
   STATICFILES_DIRS = [
       os.path.join(BASE_DIR, 'static'),
   ]
   ```

8. 在Pycharm 中将项目根目录 加入解释器搜索路径

   ```
    鼠标右键项目根目录 -> Mark Directory as -> Sources Root
   
   ```

9. 编写测试视图

   ```python
   # apps/app_name/views.py
   
   def test_launch(request):
       pass
   ```

10. 配置与测试视图对应的url

    ```python
    # project_name/urls.py

    from apps.app_name import views as app_name_views

    urlpatterns = [
	path('admin/', admin.site.urls),
	path('test_launch/', app_name_views.test_launch),
    ]

    ```
11. 启动服务器，测试项目

    ```shell
    python manage.py runserver [ip:port]
    ```

    

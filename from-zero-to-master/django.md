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

4. 注册应用

   ```python
   # project_name/settings.py

   INSTALLED_APPS = [
       ...,
       app_name,
   ] 
   ```

5. 配置数据库

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

6. 创建迁移，创建Django默认已安装应用的数据表

   ```shell
   python manage.py makemigrations
   python manage.py migrate
   ```

7. 配置项目模板路径

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

8. 配置项目静态文件路径

   ```python
   # project_name/settings.py
   STATICFILES_DIRS = [
       os.path.join(BASE_DIR, 'static'),
   ]
   ```

9. 在Pycharm 中将项目根目录 加入解释器搜索路径

   ```
    鼠标右键项目根目录 -> Mark Directory as -> Sources Root
   
   ```

   ```python
    import os
    import sys

    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
   ```

10. 编写测试视图

   ```python
   # apps/app_name/views.py
   
   def test_launch(request):
       pass
   ```

11. 配置与测试视图对应的url

    ```python
    # project_name/urls.py

    from apps.app_name import views as app_name_views

    urlpatterns = [
	path('admin/', admin.site.urls),
	path('test_launch/', app_name_views.test_launch),
    ]

    ```
12. 启动服务器，测试项目

    ```shell
    python manage.py runserver [ip:port]
    ```

    
## 自定义UserModel
> 当django默认的`auth_user`表提供的字段不满足我们的项目需求的时候，我们就需要扩展django的User模型。

```python
# users/models.py
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    # 扩展字段
    pass

```
```python
# project_name/settings.py

AUTH_USER_MODEL = "users.UserProfile"
```
最后创建迁移，会删除掉django自带的`auth_user`表


## Django Admin

1. 注册模型

```python
# users/admin.py

from django.contrib import admin

from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserProfile, UserProfileAdmin)
```

## XAdmin for Django
[项目地址](https://github.com/sshwsfc/xadmin)

1. Install xadmin

   ```python
   pip install git+git://github.com/sshwsfc/xadmin.git@django2
   ```

2. Config xadmin on Django

   ```python
   # project_name/settings.py
   INSTALLED_APPS = [
       ...,
       'xadmin',
       'crispy_forms'
   ]
   ```

   ```python
   # project_name/urls.py
   
   # from django.contrib import admin
   from django.urls import path
   
   import xadmin
   
   urlpatterns = [
       # path('admin/', admin.site.urls),
       path('xadmin/', xadmin.site.urls),
   
   ]
   ```

   最后，应用xamdin的数据库迁移

   ```python
   python manage.py migrate
   ```

3. Test xadmin site
  ```visit http://localhost:8000/xadmin/```

4. 源码安装xadmin

   > 拷贝xadmin 的源码到项目根目录下，然后新建一个目录`extra_apps`来作为第三方应用的容器，将该目录Mark 为Sources Root 即可， 然后 `pip uninstall xadmin` 卸载掉之前安装的xadmin, 其他依赖不需要卸载，我们仍然需要用到


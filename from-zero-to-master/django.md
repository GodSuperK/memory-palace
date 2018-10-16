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

5. 为每个应用注册模型

     先在每个应用下新建一个`adminx.py`，用来编写我们的注册模型的代码

     ```python
     # app_name/adminx.py
     import xadmin
     
     from .models import EmailVerifyCode
     
     
     class EmailVerifyCodeAdmin:
         # 自定义显示字段
         list_display = ['email', 'code', 'send_type', 'send_time']
         # 自定义搜索字段
         search_fields = ['email', 'code', 'send_type']
         # 自定义筛选字段
         list_filter = ['email', 'code', 'send_type', 'send_time']
     
     
     xadmin.site.register(EmailVerifyCode, EmailVerifyCodeAdmin)
     ```

6. 全局配置

     ```python
     # users/adminx.py
     
     import xadmin
     from xadmin import views
     
     
     class BaseSettings:
         enable_themes = True  # 启动切换主题功能
         use_bootswatch = True  # 添加bootstrap主题
     
     
     class GlobalSettings:
         site_title = "GMOOC"  # 页面标题
         site_footer = "gmooc"  # 页面版权
         menu_style = "accordion"  # 折叠标签
     
     
     xadmin.site.register(views.BaseAdminView, BaseSettings)
     xadmin.site.register(views.CommAdminView, GlobalSettings)
     ```

7. 配置中文标签

     ```python
     # app_name/apps.py
     
     from django.apps import AppConfig
     
     
     class UsersConfig(AppConfig):
         name = 'users'
         verbose_name = "用户信息"
     ```

     ```python
     # app_name/__init__.py
     
     default_app_config = "users.apps.UsersConfig"
     ```

     

## 用户应用功能实现

### 1. 用户登陆

1. 配置用户登陆前端相关页面，修改页面中的静态文件路径，以及跳转路径，配置`urlConf`，最后测试页面是否配置成功

   ```python
   # project_name/urls.py
   
   from django.views.generic import TemplateView
   
   
   urlpatterns = [
       ...,
       # 配置
       path('', TemplateView.as_view(template_name="index.html"), name="index"),
       # 登陆页面
       path('login/', TemplateView.as_view(template_name="login.html"), name="login"),
   ]
   ```

2. 用户登陆逻辑编写

   1. 判断请求类型

      - GET -> 登陆表单

        ```python
        # views.py
        
        from django.shortcuts import render
        
        if request.method == "GET":
            return render(request, 'login.html', {})
        ```

      - POST -> Step 2

   2. 登陆验证处理

      1. 获取表单中提交的`用户名` 及 `密码`，（所有POST请求提交的内容都保存在一个字典形式的`request.POST`中）

      2. 使用 django 提供的认证方法，默认使用用户名进行认证

         ```python
         from django.contrib import auth
         
         # 将用户名及密码作为关键字参数传入, 该方法会对数据库进行查询，进行认证
         # 认证成功，会返回一个 UserProfile model 的实例化对象
         # 认证失败，返回None
         user = auth.authenticate(username=username, password=password)
         ```

      3. 认证成功，使用 django 提供的登陆方法进行登陆, 然后跳转到首页

         ```python
         if not user:
             auth.login(request,user)
             return render(request, 'index.html', {})
         ```

      4. 认证失败，继续返回登陆页面，同时显示错误信息

         ```python
         else:
             return return render(request, 'login.html', {"msg":"用户名或密码错误"})
         ```

      5. 前端首页使用模板语言(if)进行判断用户是否登陆

         ```html
         <!--如果用户登陆，显示用户名-->
         {% if request.user.is_authenicated %}
         用户名
         {% else %}
         <!--如果用户未登陆，显示注册及登陆按钮-->
         登陆，注册
         {% endif %}
         ```

      6. 自定义认证方法

         ```python
         # views.py
         from django.contrib.auth.backends import ModelBackend
         from django.db.models import Q
         
         from .models import UserProfile
         
         
         class CustomBackend(ModelBackend):
         
             def authenticate(self, request, username=None, password=None, **kwargs):
                 try:
                     user = UserProfile.objects.get(Q(username=username) | Q(email=username))
                     if user.check_password(password):
                         return user
                 except Exception:
                     return None
         ```

         ```python
         # settings.py
         AUTHENTICATION_BACKENDS = (
         	'users.views.CustomBackend',
         )
         ```

         

   3. 
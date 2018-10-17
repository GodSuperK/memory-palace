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
   ```html
   <!-- 模板文件中引用静态文件 -->
   <html>
   {% load staticfiles %}
   <!-- 相当于在相对路径的前面自动加上 /static/ -->
   <link rel="stylesheet" type="text/css" href="{% static 'css/reset.css' %}">
   </html>
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
         if user:
             auth.login(request,user)
             return render(request, 'index.html', {})
         ```

      4. 认证失败，返回登陆页面，同时显示错误信息

         ```python
         else:
             return render(request, 'login.html', {"msg":"用户名或密码错误"})
         ```

      5. 前端首页使用模板语言(if)进行判断用户是否登陆

         ```html
         <!--如果用户登陆，显示用户名-->
         {% if request.user.is_authenticated %}
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

         

   3. 使用类编写登陆 view

      ```python
      # views.py
      from django.http import HttpResponseRedirect
      from django.views import generic
      
      
      class LoginView(generic.View):
      
          def get(self, request):
              return render(request, 'login.html', {})
      
          def post(self, request):
              username = request.POST.get("username", "")
              password = request.POST.get("password", "")
              user = auth.authenticate(username=username, password=password)
              if user:
                  auth.login(request, user)
                  return HttpResponseRedirect("/")
              else:
                  return render(request, "login.html", {"error_msg": '用户名或密码错误'})
      ```

      ```python
      # project_name/urls.py
      
      from users import views as users_views
      
      urlpatterns = [
          ...,
          path('login/', users_views.LoginView.as_view(), name="login"),
      ]
      ```

   4. 使用 django 表单验证, 对用户输入进行预处理

      ```python
      # app_name/forms.py
      
      from django import forms
      
      
      class LoginForm(forms.Form):
          # required=True, 表示该字段不可为空
          username = forms.CharField(required=True)
          password = forms.CharField(required=True)
      ```

      ```python
      # app_name/views.py
      
      from .forms import LoginForm
      
      class LoginView(generic.View):
          
          def post(self, request):
              login_form = LoginForm(request.POST)
              # 如果提交的数据满足django表单预定义，则返回True
              if login_form.is_valid():
                  username = request.POST.get("username", "")
                  password = request.POST.get("password", "")
                  user = auth.authenticate(username=username, password=password)
                  if user:
                      auth.login(request, user)
                      return HttpResponseRedirect("/")
                  else:
                      return render(request, "login.html", {"error_msg": '用户名或密码错误'})
              else:
                  # 将表单传回前端，使用模板语言提取错误信息
                  return render(request, "login.html", {"login_form": login_form})
      ```

      ```html
      <!-- login.html -->
      
      <!-- 如果验证失败，errors里的key会有错误提示， 为输入框添加一个红色边框，来指示用户信息输入有误 -->
      <div class="form-group marb20 {% if login_form.errors.username %}errorput{% endif %}"><label>用&nbsp;户&nbsp;名</label><input name="username" id="account_l" type="text" placeholder="手机号/邮箱"/></div>
      
      <!--提取错误信息进行显示-->
      <div class="error btns login-form-tips" id="jsLoginTips">{{ login_form.errors.username }}</div>
      
      <div class="form-group marb8 {% if login_form.errors.password %}errorput{% endif %}"><label>密&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;码</label><input name="password" id="password_l" type="password" placeholder="请输入您的密码"/></div>
      
      <div class="error btns login-form-tips" id="jsLoginTips">{{ login_form.errors.password }}</div>
      
      <!-- 循环的形式遍历错误信息 -->
      {% for k,v in login_form.errors.items %}
      <div class="error btns login-form-tips" id="jsLoginTips">{{ k }}:{{ v }}</div>
      {% endfor %}
      <div class="error btns login-form-tips" id="jsLoginTips">{{ error_msg }}</div>
      ```

### 2. 用户注册

1. 配置用户注册前端相关页面，修改页面中的静态文件路径，以及跳转路径，配置`urlConf`，最后测试页面是否配置成功

2. 编写 `RegisterView`

   ```python
   # GET 返回 注册表单页面
   def get(self, request):
   	return render(request, "register.html")
   ```

   ```python
   # POST 注册逻辑
   def post(self, request):
       pass
   ```

3. 配置第三方验证码库 `django-simple-captcha` [官方文档](https://django-simple-captcha.readthedocs.io/en/latest/usage.html#installation)

   ```
   # Installation
   1. Install django-simple-captcha via pip: pip install  django-simple-captcha
   2. Add captcha to the INSTALLED_APPS in your settings.py
   3. Run python manage.py migrate
   
   4. Add an entry to your urls.py:
   ```

   ```python
   urlpatterns += [
       path('captcha/', include('captcha.urls')),
   ]
   ```

4. 编写表单RegisterForm, 对用户注册所需的字段进行验证(邮箱，密码，验证码)

   ```python
   # forms.py
   from django import Form
   from captcha.fields import CaptchaField
   
   
   class RegisterForm(forms.Form):
   	email = forms.EmailField(required=True)
       password = forms.CharField(required=True, min_length=8)
       captcha = CaptchaField()
   ```

5. 将验证码图片渲染到前端页面

   ```python
   # views.py
   from .forms import RegisterForm
   
   def get(self, request):
       register_form = RegisterForm()
   	return render(request, "register.html", {'register_form': register_form})
   ```

   ```html
   <!-- register.html -->
   {{ register_form.captcha }}
   ```

6. 完成注册逻辑

   1. 邮箱注册逻辑

      ```python
      def post(self, request):
          """用户邮箱注册逻辑"""
          # 1. 先使用注册表单验证数据字段是否有效
          register_form = RegisterForm(request.POST)
          if register_form.is_valid():
              email = request.POST.get("email", "")
              password = request.POST.get("password", "")
              # TODO 对邮箱进行数据库查询，是否已经注册
              # 实例化一个UserProfile对象，然后保存到数据库
              user = UserProfile()
              user.email = email
              # 将用户名暂时初始化为邮箱
              user.username = email
              # 对密码进行加密，保存密文
              user.password = hashers.make_password(password=password)
              # 为用户注册账户，但并为激活账号
              user.save()
              # TODO 发送邮箱激活链接
      
          return render(request, "register.html", {'register_form': register_form})
      ```

      


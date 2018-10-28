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
   │   └── utils - 管理工具函数
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




## Django 表单应用

```python
# forms.py

from django import forms
from captcha.fields import CaptchaField

class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=8)
    captcha = CaptchaField() # error_message 可以自定义错误消息
```



1. 前台渲染表单控件

   ```html
   <!-- 首先需要后台回传 表单实例 register_form-->
   <p>邮箱： {{ register_form.email }}</p>
   <p>密码： {{ register_form.password }}</p>
   <p>验证码： {{ register_form.captcha }}</p>
   ```

2. 表单填充默认值

   ```python
   <p>
   邮箱： <input type="text" name="email" value="{{ register_form.email.value }}" >
   </p>
   ```

3. 显示错误信息

   ```html
   {% for k,v in register_form.errors.items %}
   <div class="error">{{ k }}:{{ v }}</div>
   {% endfor %}
   
   {{ register_form.errors.email }}
   {{ register_form.errors.password }}
   {{ register_form.errors.captcha }}
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
       captcha = CaptchaField(error_message="验证码错误")
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
      from django.contrib.auth import hashers
      
      def post(self, request):
          """用户邮箱注册逻辑"""
          # 1. 先使用注册表单验证数据字段是否有效
          register_form = RegisterForm(request.POST)
          if register_form.is_valid():
              # 2. 提取注册字段
              email = request.POST.get("email", "")
              password = request.POST.get("password", "")
              # 对邮箱进行数据库查询，是否已经注册
              u = UserProfile.objects.filter(email=email).first()
              if u:
             	    return render(request, 'register.html', 
                                    {"register_form": register_form, 
                                     "error_msg": '该邮箱已经注册'})
              # 3. 实例化一个UserProfile对象，然后保存到数据库
              user = UserProfile()
              user.email = email
              # 将用户名暂时初始化为邮箱
              user.username = email
              # 对密码进行加密，保存密文
              user.password = hashers.make_password(password=password)
              # 不激活账户
              user.is_active = False
              user.save()
              # 4. 发送邮箱激活链接
              status_code = email_send.send_email(email, "register")
              if status_code:
                  return HttpResponse("激活链接已发送到您的邮箱")
              else:    
              	return HttpResponse("无效邮箱，发送激活链接失败")
              # 最后，跳转到登陆页面
              # return HttpResponseRedirect('/login/')
          return render(request, "register.html", {'register_form': register_form})
      ```

   2. 配置邮件系统

      ```python
      # settings.py
      
      # 邮件发送信息配置
      EMAIL_HOST = None  # 邮件服务器
      EMAIL_PORT = None  # 端口
      EMAIL_HOST_USER = None  # 发送人的邮箱
      EMAIL_HOST_PASSWORD = None  # 客户端授权码
      EMAIL_USE_TLS = False
      EMAIL_FROM = EMAIL_HOST_USER  # 邮件发送者
      ```

   3. 在工具包(utils)里编写发送邮箱链接函数

      ```python
      # utils/email_send.py
      
      from django.core import mail
      
      from users.models import EmailVerifyCode
      from utils.basic_settings import EMAIL_FROM
      import random
      
      
      def send_email(email, send_type="register"):
          """ 发送邮箱链接
          激活链接原理：
          1. Server 随机生成一段随机字符串，并保存到数据库，将其和url地址连接起来
          2. 将邮箱验证链接发送到用户的邮箱
          3. 当用户点击 url 链接后，进入到 Server 的路由匹配，Server 提取出随机字符串
          4. 将随机字符串和数据库中的字段进行对比
          5. 如果一致，则邮箱激活成功
          6. 如果不一致，则邮箱激活失败
          :param email: 目标邮箱
          :param send_type: `register` 表示是激活链接 `forget` 表示是找回密码链接
          :return:
          """
          # 1. 先实例化一个EmailVerifyCode对象，将其保存到数据库，供后面验证一致性
          email_record = EmailVerifyCode()
          email_record.email = email
          if send_type in ["register", "forget"]:
              email_record.send_type = send_type
          # generate_random_str() 用来生成随机字符串
          email_record.code = generate_random_str(length=16)
          email_record.save()
      
          # 2. 定义邮件 e 的主题和消息
          e_subject = ""
          e_message = ""
      
          if send_type == "register":
              e_subject = "慕学在线网注册激活链接"
              e_message = "请点击下面的链接激活您的账户 http://127.0.0.1:8000/active/{}".format(email_record.code)
          elif send_type == "forget":
              # TODO 找回密码链接
              pass
          else:
              pass
      
          # 3. 使用django提供的发送邮件函数 django.core.mail.send_mail
          # 需要提前配置好 邮件发送者的信息
          send_status = mail.send_mail(subject=e_subject,
                                       message=e_message,
                                       from_email=EMAIL_FROM,
                                       recipient_list=[email, ])
          # 返回状态码
          return send_status
      
      
      def generate_random_str(length=8):
          """
          生成随机字符串
          :param length: int 随机字符串字符串长度
          :return: str s
          """
      
          # 生成chars可选字符序列的算法
          # chars_li = [chr(i) + chr(i).lower() for i in range(65, 91)]
          # chars_li += [str(i) for i in range(10)]
          # chars_str = ''.join(chars)
          chars = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789"
      
          # 每次循环随机生成一个整数（避免出界，需要在chars的长度范围内）
          # 然后索引取出，循环次数由随机字符串长度决定
          s = ''.join([chars[random.randint(0, len(chars) - 1)] for i in range(length)])
          return s
      ```

   4. 编写激活链接验证ActiveUserView

      ```python
      class ActiveUserView(generic.View):
          """
          激活链接验证 View
          """
      
          def get(self, request, code):
              # 1. 数据库查询
              email_is_exist = EmailVerifyCode.objects.filter(code=code).first()
              if email_is_exist:
                  # 2. 将该邮箱所属的账户激活
                  user = UserProfile.objects.get(email=email_is_exist.email)
                  user.is_active = True
                  user.save()
                  # 3. 删除该记录，以防止用户重复激活
                  email_is_exist.delete()
                  # 4. 跳转到用户个人中心或者首页,登陆页面
                  return HttpResponse("您的账户已经成功激活")
              else:
                  return HttpResponse("验证失败")
      ```

   5. 配置ActiveUserView URLConf

      ```python
      # urls.py
      from django.urls import re_path
      
      urlpatterns += [
          re_path(r'^active/(?P<code>\w+)/$', users_views.ActiveUserView.as_view(), name="active"),
      ]
      ```

   6. 更新LoginVIew，只有账户已激活的情况下，才能登陆

      ```python
      # 只有账户已激活的情况下，才能登陆
      if user.is_active:
      	auth.login(request, user)
      	return HttpResponseRedirect("/")
      else:
      	return render(request, "login.html", {"error_msg": '账户未激活'})
      ```

### 3. 找回密码

原理：用户点击忘记密码后，返回忘记密码页面，用户输入邮箱，及验证码，当表单验证通过后，后台拿到用户的邮箱，然后给用户发送一个找回密码的链接，当用户点击链接后，进入到服务器的路由匹配，根据正则提取随机字符串，进行数据库查询，如果该随机字符串存在，则验证成功，跳转到修改密码页面，同时将邮箱字段也传到前端，用户输入密码，以及确认密码，提交到后台，后台进行表单验证，如果验证通过，则根据邮箱查询用户实例，修改密码，保存新密码的密文，然后保存到数据库即可，最后跳转到登陆页面。

1. 配置静态页面(一个忘记密码页面[需要用户输入账号及验证码]，一个修改密码页面[用户输入新密码及确认密码]及url
2. 编写django表单
3. 编写View



## 4. 机构功能

#### 1. 机构动态数据展示及分页

1. 使用django模板继承复写html页面，将多个页面公用的部分，抽象到base.html中，让子模板继承

2. 配置上传文件的路径，这样在后台管理系统中上传文件的时候，会在字段的`upload_to`参数指定的相对路径前面加上`/media/`，文件会上传到该路径下

   ```python
   # settings.py
   
   TEMPLATES['options']['context_processors'] += ['django.template.context_processors.media',]
   
   MEDIA_URL = "/media/"
   MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
   ```

   配置上传文件的访问处理函数的URLConf

   ```python
   # urls.py
   from django.views.static import serve
   from mxonline.settins import MEDIA_ROOT
   
   urlpatterns += [re_path(r'^media/(?P<path>.*)/$', serve, {'document_root': MEDIA_ROOT})]
   ```

3. 使用后台管理系统添加一些待展示数据

4. 分页实现，使用 [django-pure-pagination](https://github.com/jamespacileo/django-pure-pagination)

   ```html
   <!-- 自定义分页html样式 -->
   <!-- 进行判断，是否还有上一页 -->
   上一页
   1
   2
   3
   <!-- 进行判断，是否还有下一页 -->
   下一页
   
   <ul class="pagelist">
   	{% if orgs.has_previous %}
   		<li class="long"><a href="?{{ orgs.previous_page_number.querystring }}">上一页</a>
       </li>
   	{% endif %}
   	{% for i in orgs.pages %}
   		{% if i %}
   			{% ifequal i orgs.number %}
   				<li class="active"><span>{{ i }}</span></li>
   			{% else %}
   				<li><a href="?{{ i.querystring }}" class="page">{{ i }}</a></li>
   			{% endifequal %}
   		{% else %}
   			<li class="none"><a href="">...</a></li>
   		{% endif %}
   	{% endfor %}
   	{% if orgs.has_next %}
   		<li class="long"><a href="?{{ orgs.next_page_number.querystring }}">下一页</a>
       	</li>
   	{% endif %}
   </ul>
   ```

#### 2. 根据城市筛选机构

1. 当用户点击城市时，为get请求添加一个`city`参数

   ```html
   {% for i in cities %}
   	<a href="?city={{ i.id }}"><span class="">{{ i.name }}</span></a>
   {% endfor %}
   ```

2. 后台取出参数，进行数据库查询，将查询结果返回以及city_id返回

   ```python
   city_id = request.GET.get('city', '')
   # CourseOrg 中的city 外键在数据表中存储为 city_id
   if city_id:
   	all_orgs = CourseOrg.objects.filter(city_id=int(city_id))
   return query_result, city_id
   ```

3. 将已选中的条件高亮显示, 同时将全部标签取消高亮

   ```html
   <a href=""><span class="{% if not city_id %}active2{% endif %}">全部</span></a>
   {% for i in cities %}
   <a href="?city={{ i.id }}">
   <!-- stringformat:'i'是将i.id转为字符串类型 -->
   <span class="{% ifequal city_id i.id|stringformat:'i' %}active2{% endifequal %}">
   	{{ i.name }}
   </span>
   </a>
   {% endfor %}
   ```

4. 增加机构类别筛选的逻辑

   ```html
   <a href="?city={{ city_id }}">
       <span class="{% if not ct %}active2{% endif %}">全部</span>
   </a>
   <a href="?ct=1&city={{ city_id }}">
       <span class="{% ifequal ct 1 %}active2{% endifequal %}">培训机构</span>
   </a>
   <a href="?ct=2&city={{ city_id }}">
       <span class="{% ifequal ct 2 %}active2{% endifequal %}">高校</span>
   </a>
   <a href="?ct=3&city={{ city_id }}">
       <span class="{% ifequal ct 3 %}active2{% endifequal %}">个人</span>
   </a>
   ```

5. 完善城市筛选加机构类别筛选

   ```html
   <a href="?ct={{ ct }}">
       <span class="{% if not city_id %}active2{% endif %}">全部</span>
   </a>
   {% for i in cities %}
   	<a href="?city={{ i.id }}&ct={{ ct }}">
   	<span class="{% ifequal city_id i.id %}active2{% endifequal %}">
           {{ i.name }}
           </span>
   	</a>
   {% endfor %}
   ```

6. `OrgListView` 的完整逻辑

   ```python
   # views.py
   
   class OrgListView(generic.View):
   	
       # TODO 逻辑有待优化
       def get(self, request):
           cities = CityDict.objects.all()
           all_orgs = None
           ct = request.GET.get('ct', '')
           city_id = request.GET.get('city', '')
           if ct and city_id:
               ct = int(ct)
               city_id = int(city_id)
               # CourseOrg 中的city 外键在数据表中存储为 city_id
               all_orgs = CourseOrg.objects.filter(category=ct, city_id=city_id)
           elif ct:
               ct = int(ct)
               all_orgs = CourseOrg.objects.filter(category=ct)
           elif city_id:
               city_id = int(city_id)
               all_orgs = CourseOrg.objects.filter(city_id=city_id)
           else:
               all_orgs = CourseOrg.objects.all()
   
           # 机构数量
           nums_org = all_orgs.count()
   
           # 对机构进行分页
           try:
               page = request.GET.get('page', 1)
           except PageNotAnInteger:
               page = 1
   
           # per_page 表示每页显示的记录条数
           p = Paginator(all_orgs, request=request, per_page=5)
   
           orgs = p.page(page)
   
           return render(request, 'org-list.html', {
               'orgs': orgs,
               'cities': cities,
               'nums_org': nums_org,
               'city_id': city_id,
               'ct': ct
           })
   	
   ```



#### 3. 热门机构排名

根据点击人数排名，显示3个点击人数最多的机构

```python
hot_orgs = CourseOrg.objects.order_by("-hits")[:3]
return hot_orgs
```

#### 4. 根据学习人数和课程数对机构进行排序 

机构的学习人数：当用户点击我要学习某个课程后,找到该课程的所属机构，机构的学习人数即加1，不是实际学习人数（一个用户可能会被计算多次）

机构的课程数：当前机构发布的课程总数

1. 更新课程机构模型的结构

   ```python
   # models.py
   # 新增以下字段
   nums_of_students = models.IntegerField(verbose_name="学习人数", default=0)
   nums_of_courses = models.IntegerField(verbose_name="课程数", default=0)
   ```

2. 为请求增加排序参数

   ```html
   <li class=""><a href="?sort=nums_of_students">学习人数 &#8595;</a></li>
   <li class=""><a href="?sort=nums_of_courses">课程数 &#8595;</a></li>
   ```

3. 排序参数之间添加关联

   ```html
   <li class="{% if not sort %}active{% endif %}">
       <a href="?ct={{ ct }}&city={{ city_id }}">全部</a>
   </li>
   <li class="{% ifequal sort 'nums_of_students' %}active{% endifequal %}">
       <a href="?ct={{ ct }}&city={{ city_id }}&sort=nums_of_students">
           学习人数 &#8595;
       </a>
   </li>
   <li class="{% ifequal sort 'nums_of_courses' %}active{% endifequal %}">
       <a href="?ct={{ ct }}&city={{ city_id }}&sort=nums_of_courses">
           课程数 &#8595;
       </a>
   </li>
   ```

4. 机构课程View的完整逻辑（已优化查询逻辑）

   ```python
   class OrgListView(generic.View):
   
       def get(self, request):
   
           # 热门机构根据收藏人数排序，显示3个机构
           hot_orgs = CourseOrg.objects.order_by("-hits")[:3]
           # 显示已有城市
           cities = CityDict.objects.all()
   
           # 获取所有查询参数
           ct = request.GET.get('ct', '')
           city_id = request.GET.get('city', '')
           # 获取排序参数
           sort = request.GET.get('sort', '')
           # 查询所有机构
           all_orgs = CourseOrg.objects.all()
           # 机构筛选 by 机构类别(category)
           if ct:
               all_orgs = all_orgs.filter(category=int(ct))
           # 机构筛选 by 城市(city_id)
           if city_id:
               # CourseOrg 中的city 外键在数据表中存储为 city_id
               all_orgs = all_orgs.filter(city_id=int(city_id))
   
           # 机构数量
           nums_org = all_orgs.count()
           if sort in ['nums_of_students', 'nums_of_courses']:
               # 排序 by 学习人数(nums_of_students)或课程数(nums_of_courses)
               all_orgs = all_orgs.order_by("-{}".format(sort))
   
           # 对机构进行分页
           try:
               page = request.GET.get('page', 1)
           except PageNotAnInteger:
               page = 1
   
           # per_page 表示每页显示的记录条数
           p = Paginator(all_orgs, request=request, per_page=5)
   
           orgs = p.page(page)
   
           return render(request, 'org-list.html', {
               'orgs': orgs,
               'cities': cities,
               'nums_org': nums_org,
               'city_id': city_id,
               'ct': ct,
               'sort': sort,
               'hot_orgs': hot_orgs
           })
   ```

#### 5. 使用ModelForm 来完成 用户咨询的功能

1. 使用`URLConf include`机制， 重新优化所有url

   ```python
   # mxonline/urls.py
   from django.urls import path, include
   
   urlpatterns = [
       path('org/', include('organization.urls')),
   ]
   ```

   ```python
   # organization/urls.py
   from django.urls import path, re_path
   
   app_name="organization"
   
   urlpatterns = [
       path('list/', views.OrgListView.as_view(), name="list"),
   ]
   ```

   ```html
   {% url 'organization:list' %}
   ```

2. 编写`UserAskModelForm`

   ```python
   # forms.py
   
   class UserAskModelForm(forms.ModelForm):
       """
       ModelForm 可以继承 模型的字段，同时也可以新增字段
       """
   
       class Meta:
           model = UserAsk
           fields = ['name', 'phone', 'course_name']
   
       def clean_phone(self):
           """正则：手机号（精确）,验证手机号是否合法
   
           移动：134(0-8)、135、136、137、138、139、147、150、151、152、157、158、159、178、182、183、184、187、188、198
           联通：130、131、132、145、155、156、175、176、185、186、166
           电信：133、153、173、177、180、181、189、199
           全球星：1349
           虚拟运营商：170
           :return:
           """
           phone = self.cleaned_data["phone"]
           REGEX_PHONE_EXACT = "^((13[0-9])|(14[5,7])|(15[0-3,5-9])|(17[0,3,5-8])|(18[0-9])|166|198|199|(147))\\d{8}$"
           # 将正则表达式编译为pattern对象
           pattern = re.compile(REGEX_PHONE_EXACT)
           # 验证用户输入的手机号是否符合我们的 pattern 规则
           if pattern.match(phone):
               return phone
           # 不符合规则，抛出 forms.ValidationError 异常
           else:
               raise forms.ValidationError(message="手机号码非法", code="phone_invalid")
   ```

3. Ajax补充，浏览器发送异步请求，服务器返回`json`数据，使页面不会刷新，提升用户体验。

   ```html
   // 发送异步请求的流程
   // 1. 获取按钮元素
   // 2. 添加点击事件
   // 3. 绑定函数
   // 4. 编写异步请求
   
   <script>
       $(function () {
           $(document).ready(function () {
               $('#jsStayBtn').on('click', function () {
                   $.ajax({
                       cache: false,
                       type: "POST",
                       url: "{% url 'organization:add_ask' %}",
                       data: $('#jsStayForm').serialize(),
                       async: true,
                       success: function (data) {
                           if (data.status === "success") {
                               console.log(data);
                               $('#jsStayForm')[0].reset();
                               alert("提交成功")
                           } else if (data.status === "failed") {
                               $('#jsCompanyTips').html(data.error)
                           }
                       },
                   });
               });
           });
       })
   </script>
   ```

4. 编写`UserAskView`

   ```python
   class UserAskView(generic.View):
       """用户咨询View
       该功能客户端使用ajax发送异步请求，
       当用户点击提交按钮后，页面不能刷新, 我们需要返回json格式的数据
       """
   
       def post(self, request):
           # 定义返回的json数据
           result = dict()
           user_ask_form = UserAskModelForm(request.POST)
           if user_ask_form.is_valid():
               # 使用表单的快捷方式save 来对模型进行快速实例化，并保存到数据库中
               user_ask_form.save(commit=True)
               result["status"] = "success"
               # 告诉浏览器，我们返回的是json数据, 让浏览器交给 ajax 去解析
               return HttpResponse(json.dumps(result), content_type="application/json")
           else:
               result["status"] = "failed"
               result["error"] = "添加出错"
               return HttpResponse(json.dumps(result), content_type="application/json")
   ```

5. 配置url

   ```python
   # organization/urls.py
   
   urlpatterns += [
       path('add_ask/', views.UserAskView.as_view(), name="add_ask"),
   ]
   ```


#### 6. 机构详情页

1. 使用Django 模板继承重构前端模板(1个base, 4个子页面), 配置测试url
2. 进行数据库查询，并将数据传到前端展示即可

#### 7. 收藏功能以及取消收藏 

后端逻辑：执行该操作的前提，用户必须登陆，所以在逻辑中需要添加判断用户是否登陆的逻辑，用户点击收藏对象后，将对象的id，和类型值传递到后台，进行一个数据库插入即可，该操作使用ajax发起一个异步GET请求。如果用户已经收藏过了，然后又一次发起请求，则取消收藏（数据库删除操作）。

前台页面逻辑：Ajax根据返回值判断该对象是否已经被用户收藏，如果已被收藏则显示已收藏，否则显示收藏。同时每个页面也需要进行判断（可以在渲染页面的时候，后台传入一个是否已收藏的变量来进行判断），避免用户点击收藏后，进行页面刷新，又显示回收藏。

### 课程功能

1. 相关课程推荐

   为课程添加一个`tag`字段，根据`tag`过滤课程。



### 8. 使用videojs 播放视频

### 9. 配置首页全局导航

原理：根据url地址中的相对路径来判断当前的位置

在模板中 `request.path` 可以拿到当前url的相对路径

使用 template filter `slice` 来切片路径进行判断位置 



### 10. 全局搜索功能

根据关键词进行搜索，将查询内容显示在数据列表页

### 11. 用户头像上传

1. 配置上传url
2. 编写View
3. 表单中要增加`enctype="multipart/form-data"`


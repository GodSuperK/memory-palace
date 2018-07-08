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




## URLconfs (urls.py)

```python
# polls/urls.py

from django.urls import path

# 在根URLconf中添加命名空间
app_name = 'polls'
urlpatterns = [
    path('', view.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

"""path()

route: route 是一个匹配 URL 的准则（类似正则表达式）
view: 当 Django 找到了一个匹配的准则，就会调用这个特定的视图函数，并传入
	  一个HttpRequest 对象作为第一个参数，被“捕获”的参数以关键字参数的形式传入
kwargs: 任意个关键字参数可以作为一个字典传递给目标视图函数
name: 为你的 URL 取名能使你在 Django 的任意地方唯一地引用它，尤其是在模板中
"""

"""
当某人请求你网站的某一页面时——比如说， "/polls/34/" ，Django 将会载入 mysite.urls
模块，因为这在配置项 ROOT_URLCONF 中设置了。然后 Django 寻找名为 urlpatterns 变量
且按序匹配正则表达式。在找到匹配项 'polls/'，它切掉了匹配的文本（"polls/"），将剩余
本——"34/"，发送至 'polls.urls' URLconf 做进一步处理。在这里剩余文本匹配了
'<int:question_id>/'，使得我们 Django 以如下形式调用 detail():

detail(request=<HttpRequest object>, question_id=34)

question_id=34 由 <int:question_id> 匹配生成。使用尖括号“捕获”这部分 URL，且以关
字参数的形式发送给视图函数。上述字符串的 :question_id> 部分定义了将被用于区分匹配模式
变量名，而 int: 则是一个转换器决定了应该以什么变量类型匹配这部分的 URL 路径。
"""
```

```python
# mysite/urls.py

from django.urls import path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]

"""include()

允许引用其他URLconfs, 它会截断与此项匹配的URL的部分,并将剩于的字符串发送到
URLconf以供进一步处理
"""
```

#### 在模板中引用 url route

```html
<!-- 去除模板中的硬编码 URL -->
<li>
    <a href="{% url 'polls:detail' question.id %}">
        {{ question.question_text }}
    </a>
</li>
```

#### 在视图中引用 url route

```python
# 去除视图中的硬编码 URL
from django.urls import reverse
def vote(request, question_id):
	...
	return HttpResponseRedirect(
        reverse('polls:results', args=(question_id,)))
```
## Models (models.py)



## Views (views.py)



## templates



## static files



## Django admin





## See Also

### 项目 VS 应用

> 项目和应用有啥区别？应用是一个专门做某件事的网络应用程序——比如博客系统，或者公共记录的数据库，或者简单的投票程序。项目则是一个网站使用的配置和应用的集合。项目可以包含很多个应用。应用可以被很多个项目使用


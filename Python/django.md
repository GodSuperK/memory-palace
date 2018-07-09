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

#### 数据库配置

详见 setting.py

#### 创建模型

```python
# polls/models.py
"""
每个模型被表示为 django.db.models.Model 类的子类。
每个模型有一些类变量，它们都表示模型里的一个数据库字段
"""
import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text
 
```

#### 激活模型

```shell
# 1. install app 详见 setting.py
# 2. 检测你对模型文件的修改, 并且把修改的部分储存为一次 迁移
python3 manage.py makemigrations polls
# 3. 在数据库里创建新定义的模型的数据表
python3 manage.py migrate
```

#### 改变模型

1. 编辑 `models.py` 文件，改变模型。
2. 运行 `python manage.py makemigrations` 为模型的改变生成迁移文件。
3. 运行 `python manage.py migrate` 来应用数据库迁移。

#### PS

1.  输出的内容和你使用的数据库有关，上面的输出示例使用的是 PostgreSQL
2.  数据库的表名是由应用名(polls)和模型名的小写形式( question 和 choice)连接而来
3.  主键(IDs)会被自动创建
4.  默认的，Django 会在外键字段名后追加字符串 "_id" 
5.  外键关系由 FOREIGN KEY 生成



#### Database API

##### C(reating objects)

```python
from django.utils import timezone
q = Question(question_text="What's new?", pub_date=timezone.now())
q.save()
```

##### R(eading objects)

```python
"""
1. filter(**kwargs)
Returns a new QuerySet containing objects that match the given lookup parameters.

2. exclude(**kwargs)
Returns a new QuerySet containing objects that do not match the given 
lookup parameters.

3. 
"""

# Retrieveing all objects
# Itreturns a QuerySet that contains all Question objects in the database.
Question.objects.all()
# See doc string 1
Question.objects.filter(id=1)
Question.objects.filter(question_text__startswith='What')
# Limiting QuerySets
# Negative indexing (i.e. Question.objects.all()[-1]) is not supported.
# this returns the first 5 objects(LIMIT 5)
Question.objects.all()[:5]
# this returns sixth through tenth objects (OFFSET 5 LIMIT 5)
Question.objects.all()[5:10]
# Retrieving a single object 
# If there are no results that match the query, 
# that will raise a DoesNotExist exception
# Django provides a pk lookup shortcut, which stands for "primary key
Question.objects.get(pk=1)

"""Retriving related objects

When you define a relationship in a model (i.e., a ForeignKey, OneToOneField, 
or ManyToManyField), instances of that model will have a convenient API 
to access the related object(s).
"""

# one-to-many relationships: Forward
# If a model has a ForeignKey, instances of that model will have 
# access to the related (foreign) object via a simple attribute of the model.
c = Choice.objects.get(id=2)
# Returns the related Question object.
c.question

# If a ForeignKey field has null=True set (i.e., it allows NULL values), 
# you can assign None to remove the relation. 
c = Choice.objects.get(id=1)
c.question = None
c.save()

# one-to-many relationships: Backward
q = Question.objects.get(id=1)
# Returns all Choice objects related to Question 
q.choice_set.all()
# q.choice_set is a Manager that returns QuerySets
q.choice_set.filter(question_text__contains='What')
q.choice_set.count()
"""Additional methods to handle related objects

1. add(obj1, obj2, ...): Adds the specified model objects to the related object set.
2. create(**kwargs): Creates a new object, saves it and puts it in the related 
   object set. Returns the newly created object.
3. remove(obj1, obj2, ...): Removes the specified model objects from the 
   related object set.
4. clear(): Removes all objects from the related object set.
5. set(objs): Replace the set of related objects.
   To assign the members of a related set, use the set() method with an iterable 
   of object instances.
"""

# TODO(later Many-to-many relationships)
# TODO(later One-to-one relationships)
# TODO(later fields lookup)
```

##### U(pdating objects)

```python
# first, get object in the database
q = Question.objects.get(pk=1)
# Change values by changing the attributes, then calling save().
q.question_text = "What's up?"
q.save()
```

##### D(eleting objects)

```python
# delete one object
q = Question.objects.get(pk=2)
q.delete()

# delete more objects
# Every QuerySet has a delete() method, which deletes all members of that QuerySet.
Question.objects.all().delete()
Question.objects.filter(question_text__startswith='What').delete()
```



## Views (views.py)



## templates



## Manage static files

#### 管理应用的静态文件

```shell
polls ## app root directory
└── static
    └── polls
        ├── css    # store css files
        ├── images # store images 
        └── js     # store js files
```

Django 的 STATICFILES_FINDERS 设置包含了一系列的查找器，它们知道去哪里找到 static 文件。AppDirectoriesFinder 是默认查找器中的一个，它会在每个 INSTALLED_APPS 中指定的应用的子文件中寻找名称为 static 的特定文件夹，就像我们在 polls 中刚创建的那个一样。管理后台采用相同的目录结构管理它的静态文件



#### 在模板中引用静态文件

```html
<!-- polls/templates/polls/index.html -->

<!-- 在模板中引用静态文件 -->
{% load static %}
<link rel="stylesheet" type="text/css" href="{% static 'polls/style.css' %}" />
```

{% static %} 模板标签会生成静态文件的绝对路径



#### 静态文件之间使用相对路径互相引用

```css
/** polls/static/polls/style.css 

在css文件中引用图片文件
*/

body {
	background: white url("images/background.gif") no-repeat;
}
```



## Django admin

#### 注册模型

```python
# polls/admin.py

from django.contrib import admin

from .models import Question

# 定义关联对象
# admin.StackedInline 样式: 堆放表单,占据大量空间
# admin.TabularInline 样式: 关联对象以一种表格式的方式展示，显得更加紧凑
class ChoiceLine(admin.StackedInline):
    # 指定模型
    model = Choice
    # 指定默认的添加数量(不可在表单中移除)
    extra = 3
    
    
class QuestionAdmin(admin.ModelAdmin):
    # 按照列表中字段的顺序排列表单
    # fields = ['pub_date', 'question_text']
    # 将表单分为几个字段集, fieldsets 元组中的第一个元素是字段集的标题
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    # 添加关联的对象(高效实现,可以一次添加多个对象)
    inlines = [ChoiceInline]
    # 自定义 change list 中显示的对象的属性(数据库中记录的字段)
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # add filter
    list_filter = ['pub_date']
    # add search box (后台使用 LIKE 来查询数据)
    search_fields = ['question_text']
    
# 使用默认的表单用于展示模型
# admin.site.register(Question)
# 自定义表单的外观和工作方式
admin.site.register(Question, QuestionAdmin)
```

##### 优化字段在change list 中的显示

```python
# polls/models.py

class Question(models.Model):
    #...
    def was_published_recently(self):
        ...
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
    
```

##### 自定义你的工程的模板

```
mysite
├── manage.py
├── mysite
│   ├── init.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── templates
    └── admin
```

将存放 Django 默认模板的目录（`django/contrib/admin/templates`）内的模板文件 

`admin/base_site.html`复制到`mysite/templates/admin/`中

```python
# mysite/settings.py

# 在TEMPLATES中添加DIRS选项
# DIRS 是一个包含多个系统目录的文件列表，用于在载入 Django 模板时使用，是一个待搜索路径
TEMPLATES = [
    # ...
    'DIRS': [os.path.join(BASE_DIR, 'templates')],
    # ...
]
```

```shell
# 查看 Django源文件的位置
python -c "import django; print(django.__path__)"
```

```html
<!-- 修改大标题(默认为Django administration) -->
{% block branding %}
<h1 id="site-name"><a href="{% url 'admin:index' %}">Polls Administration</a></h1>
{% endblock %}
```



## See Also

### 项目 VS 应用

> 项目和应用有啥区别？应用是一个专门做某件事的网络应用程序——比如博客系统，或者公共记录的数据库，或者简单的投票程序。项目则是一个网站使用的配置和应用的集合。项目可以包含很多个应用。应用可以被很多个项目使用


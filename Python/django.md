# Django Command

1. python3 -m django --version 
2. django-admin startproject xxx - Creating a project xxx
3. python3 manage.py runserver
4. python3 manage.py runserver 8080
5. python3 manage.py runserver 0:8000  - 0=0.0.0.0
6. python3 manage.py startapp xxx - Creating an app xxx
7. python3 manage.py migrate
8. python3 manage.py makemigrations xxx - Creating migrations of xxx app
9. python3 manage.py sqlmigrate xxx 001 - show create statement
10. python3 manage.py check
11. python3 manage.py shell
12. python3 manage.py createsuperuser

## Common Function
1. include()
2. path(route, view, [kwargs, name])
3. 

## timezone settings
1. TIME_ZONE = 'Asia/Shanghai'
2. USE_TZ = False
## 项目 VS 应用

> 项目和应用有啥区别？应用是一个专门做某件事的网络应用程序——比如博客系统，或者公共记录的数据库，或者简单的投票程序。项目则是一个网站使用的配置和应用的集合。项目可以包含很多个应用。应用可以被很多个项目使用


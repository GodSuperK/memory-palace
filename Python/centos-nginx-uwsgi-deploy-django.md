# Cent OS 7 下通过Nginx+uwsgi部署Django应用

### 1. Install python3.7.0

```shell
# 不安装这个库,django自带的sqllite无法使用
sudo yum install sqlite-devel
# 1. Get python interpreter
wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tar.xz
tar -xvf Python-3.7.0.tar.xz -C /tmp
cd /tmp/Python-3.7.0
# 2. Install python by source code compile
./configure --with-ssl --prefix=/usr/local
make
sudo make altinstall
# 3. Create soft link
sudo ln -s /usr/local/bin/pyhton3.7 /usr/bin/python3.7
sudo ln -s /usr/local/bin/pip3.7 /usr/bin/pip3.7

# tips: Install package via douban mirror
sudo pip3.7 install -i https://pypi.douban.com/simple package-name
```

### 2. Install virtualenv

```shell
sudo yum install python34-setuptools python34-devel
sudo pip3.7 install virtualenv
sudo pip3.7 install virtualenvwrapper

# how to use
# 1. create a virtualenv
virtualenv uwsgi-tutorial
cd uwsgi-tutorial
# 2. start virtualenv
source bin/activate
```

### 3. Install Nginx

```shell
sudo yum install epel-release
sudo yum install nginx
# start service Centos
sudo systemctl start nginx
# Ubuntu
sudo /etc/init.d/nginx start
```

### 4. Install uWSGI

```shell
# 如果报错是因为没有安装python开发包 ubuntu(pythonX.Y-dev) centos(python34-devel)
sudo pip3.7 install uwsgi
# test uwsgi visit django app
uwsgi --http :8000 --module core-app-name.wsgi
# visit localhost:8000/
# if success, it means [the web client <-> uWSGI <-> Django] work
```

### 5. uWSGI TEST

```python
# test.py
def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return [b"Hello World"] # python3
```

```shell
uwsgi --http :8000 --wsgi-file test.py
# visit localhost:8000/
# if success, it means [the web client <-> uWSGI <-> Python] work
```



### 5. Configure Nginx

You will need the `uwsgi_params` file, which is available in the `nginx` directory of the uWSGI distribution, or from <https://github.com/nginx/nginx/blob/master/conf/uwsgi_params>

Copy it into your project directory. In a moment we will tell nginx to refer to it.

Now create a file called mysite_nginx.conf, and put this in it:

```
# mysite_nginx.conf

# the upstream component nginx needs to connect to
upstream django {
    # server unix:///path/to/your/mysite/mysite.sock; # for a file socket
    server 127.0.0.1:8001; # for a web port socket (we'll use this first)
}

# configuration of the server
server {
    # the port your site will be served on
    listen      8000;
    # the domain name it will serve for
    server_name .example.com; # substitute your machine's IP address or FQDN
    charset     utf-8;

    # max upload size
    client_max_body_size 75M;   # adjust to taste

    # Django media
    location /media  {
        alias /path/to/your/mysite/media;  # your Django project's media files - amend as required
    }

    location /static {
        alias /path/to/your/mysite/static; # your Django project's static files - amend as required
    }

    # Finally, send all non-media requests to the Django server.
    location / {
        uwsgi_pass  django;
        include     /path/to/your/mysite/uwsgi_params; # the uwsgi_params file you installed
    }
}
```

This conf file tells nginx to serve up media and static files from the filesystem, as well as handle requests that require Django’s intervention. For a large deployment it is considered good practice to let one server handle static/media files, and another handle Django applications, but for now, this will do just fine.

Symlink to this file from /etc/nginx/sites-enabled so nginx can see it:

```shell
sudo ln -s ~/path/to/your/mysite/mysite_nginx.conf /etc/nginx/sites-enabled/
```

#### Deploying static files

Before running nginx, you have to collect all Django static files in the static folder. First of all you have to edit mysite/settings.py adding:

```python
STATIC_ROOT = os.path.join(BASE_DIR, "static")
```

and then run

```shell
python manage.py collectstatic
```

#### nginx and uWSGI and test.py

Let’s get nginx to speak to the “hello world” `test.py` application.

```
uwsgi --socket :8001 --wsgi-file test.py
```

nginx meanwhile has been configured to communicate with uWSGI on that port, and with the outside world on port 8000. 

to check. And this is our stack:

```
the web client <-> the web server <-> the socket <-> uWSGI <-> Python
```







## PS

1. `pkill -f uwsgi` # 重启uwsgi

2. `uwsgi -i uwsgi.ini` # 启动uwsgi

3. `sudo systemctl restart nginx`

4. `sudo systemctl start nginx`

5. `python3.7 manage.py collectstatic`

6. `DEBUG=False` # 关闭开发者模式

7. ```
   nginx -t -c /etc/nginx/nginx.conf
   ```

8. ```shell
   sudo pkill -f nginx # 关闭默认的nginx用户创建的进程
   sudo nginx # 使用root用户创建nginx服务进程
   ```

### See Also

1. [Setting up Django and your web server with uWSGI and nginx](https://uwsgi.readthedocs.io/en/latest/tutorials/Django_and_nginx.html)
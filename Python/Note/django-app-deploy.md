# Cent OS 7 下通过Nginx+uWSGI部署Django应用

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
# 3. exit virtualenv
deactivate
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

#### Using Unix sockets instead of ports

So far we have used a TCP port socket, because it’s simpler, but in fact it’s better to use Unix sockets than ports - there’s less overhead.

Edit `mysite_nginx.conf`, changing it to match:

```
server unix:///path/to/your/mysite/mysite.sock; # for a file socket
# server 127.0.0.1:8001; # for a web port socket (we'll use this first)
```

and restart nginx.

Run uWSGI again:

```
uwsgi --socket mysite.sock --wsgi-file test.py
```

#### If that doesn’t work

Check your nginx error log(/var/log/nginx/error.log). If you see something like:

```
connect() to unix:///path/to/your/mysite/mysite.sock failed (13: Permission
denied)
```

then probably you need to manage the permissions on the socket so that nginx is allowed to use it.

Try:

```
uwsgi --socket mysite.sock --wsgi-file test.py --chmod-socket=666 # (very permissive)
```

You may also have to add your user to nginx’s group (which is probably www-data), or vice-versa, so that nginx can read and write to your socket properly.

It’s worth keeping the output of the nginx log running in a terminal window so you can easily refer to it while troubleshooting.

 #### Running the Django application with uwsgi and nginx

Let’s run our Django application:

```
uwsgi --socket mysite.sock --module mysite.wsgi --chmod-socket=664
```

Now uWSGI and nginx should be serving up not just a “Hello World” module, but your Django project.

#### Configuring uWSGI to run with a .ini file

We can put the same options that we used with uWSGI into a file, and then ask uWSGI to run with that file. It makes it easier to manage configurations.

Create a file called ``mysite_uwsgi.ini``:

```
# mysite_uwsgi.ini file
[uwsgi]

# Django-related settings
# the base directory (full path)
chdir           = /path/to/your/project
# Django's wsgi file
module          = project.wsgi
# the virtualenv (full path)
home            = /path/to/virtualenv

# process-related settings
# master
master          = true
# maximum number of worker processes
processes       = 10
# the socket (use the full path to be safe
socket          = /path/to/your/project/mysite.sock
# ... with appropriate permissions - may be needed
# chmod-socket    = 664
# clear environment on exit
vacuum          = true
```

And run uswgi using this file:

```
uwsgi --ini mysite_uwsgi.ini # the --ini option is used to specify a file
```

Once again, test that the Django site works as expected.

#### Install uWSGI system-wide

So far, uWSGI is only installed in our virtualenv; we'll need it installed system-wide for deployment purposes.

Deactivate your virtualenv:

```
deactivate
```

and install uWSGI system-wide:

```
sudo pip install uwsgi

# Or install LTS (long term support).
pip install https://projects.unbit.it/downloads/uwsgi-lts.tar.gz
```

The uWSGI wiki describes several [installation procedures](https://projects.unbit.it/uwsgi/wiki/Install). Before installing uWSGI system-wide, it’s worth considering which version to choose and the most apppropriate way of installing it.

Check again that you can still run uWSGI just like you did before:

```
uwsgi --ini mysite_uwsgi.ini # the --ini option is used to specify a file
```

#### Emperor mode

uWSGI can run in ‘emperor’ mode. In this mode it keeps an eye on a directory of uWSGI config files, and will spawn instances (‘vassals’) for each one it finds.

Whenever a config file is amended, the emperor will automatically restart the vassal.

```
# create a directory for the vassals
sudo mkdir /etc/uwsgi
sudo mkdir /etc/uwsgi/vassals
# symlink from the default config directory to your config file
sudo ln -s /path/to/your/mysite/mysite_uwsgi.ini /etc/uwsgi/vassals/
# run the emperor
uwsgi --emperor /etc/uwsgi/vassals --uid www-data --gid www-data
```

You may need to run uWSGI with sudo:

```
sudo uwsgi --emperor /etc/uwsgi/vassals --uid www-data --gid www-data
```

The options mean:

- `emperor`: where to look for vassals (config files)
- `uid`: the user id of the process once it’s started
- `gid`: the group id of the process once it’s started

Check the site; it should be running.

#### Make uWSGI startup when the system boots

The last step is to make it all happen automatically at system startup time.

For many systems, the easiest (if not the best) way to do this is to use the `rc.local` file.

Edit `/etc/rc.local` and add:

```
/usr/local/bin/uwsgi --emperor /etc/uwsgi/vassals --uid www-data --gid www-data --daemonize /var/log/uwsgi-emperor.log
```

before the line “exit 0”.

And that should be it!



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


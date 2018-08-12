# Tornado



## Basic Use

```python
import tornado.ioloop
import tornado.web


# TODO [User's guide](http://www.tornadoweb.org/en/stable/)

class MainHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("Hello, World!")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

```


# json

## What is JSON?

JSON 是 JavaScript 对象表示法 （JavaScript Object Notation）, 用于存储和交换文本信息。JSON 比 XML更小、更快、更易解析，因此JSON在网络传输中，尤其是Web前端中运用非常广泛。JSON使用 JavaScript 语法来描述数据对象，但是JSON 仍然独立于语言和平台。 JSON解析器和JSON库支持许多不同的编程语言，其中就包括Python。

## How to use json?

```python
import json

user = [
  'ABU', {'age':20, 'job': 'coder'},
  'Rose', {'age':20, 'job': 'coder'},
  'Jack', {'age':20, 'job': 'coder'},
]
# 将python 对象 序列化为 JSON 字符串
json_str = json.dumps(user)

# 将 JSON 字符串 反序列化为 Python 对象
py_obj = json.loads(json_str)
with open('user.json', 'w') as f:
    # 序列化到文件中
    json.dump(user, f)
    
with open('user.json', 'r') as f:
    # 从文件中加载JSON字符串 并反序列化为 Python 对象
    py_objs = json.load(f)
```

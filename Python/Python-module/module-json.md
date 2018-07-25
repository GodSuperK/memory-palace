# json

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

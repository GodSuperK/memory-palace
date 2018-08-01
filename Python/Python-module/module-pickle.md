# Pickle



## 序列化 Python obj -> str

```python
import pickle
d = {'name': 'GodSuperK', 'age': 22}
# 将任意对象序列化成一个str
d_str = pickle.dumps(d)

# 将序列化后的对象直接写入文件中
f = open('db', 'a')
pickle.dump(d, f)
```



## 反序列化 str -> Python obj

```python
# 将序列化后的对象反序列化为Python对象
d_obj = pickle.loads(d_str)

f = open('db')
# 将文件直接凡序列化为对象
d_obj2 = pickle.load(f)
```


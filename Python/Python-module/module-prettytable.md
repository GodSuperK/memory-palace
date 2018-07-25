# prettytable

> PrettyTable是一个简单的Python库，旨在快速，轻松地在视觉上吸引人的ASCII表中表示表格数据。 它的灵感来自PostgreSQL shell psql中使用的ASCII表。 PrettyTable允许选择要打印的列，列的独立对齐（左对齐或右对齐或居中）以及通过指定行范围打印“子表”。



## How to install?

`pip install PrettyTable`



## How to use?

初始化 PrettyTable 对象时 常用的关键字参数

1. encoding - 用于解码任何编码输入的Unicode编码方案
2. field_names - list or tuple of field names
3. header_style - 为 title 设置样式 ("cap", "title", "upper", "lower" or None)
4. border - 是否添加 border 默认为True  (True or False)
5. padding_width - 设置内边距

```python
# 1. 导入PrettyTable类
from prettytable import PrettyTable
# 2. 设置 table 的列数 和列名
table = PrettyTable(header_style='upper', padding_width=5,field_names=['No.', 'name', 'score']) # 传入一个列表即可
# 3. 设置 table 的对齐方式
table.align = 'l'
trigger_rules = []
# 4. 向 table 中插入行
row = ['1.', 'ABU', '100']
table.add_row(row)
print(table)
```


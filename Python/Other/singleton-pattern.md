# Python Singleton Pattern(单例模式)
> 确保某一个类只有一个实例，而且自行实例化并向整个系统提供这个实例，这个类称为单例类，它提供全局访问的方法。



```python
class Earth:
    __instance = None
    
    def __init__(self, *args, **kwargs):
        pass
    
    def __new__(cls, *args, **kwargs):
        if cls.__instance == None:
            cls.__instance == super().__new__(cls, *args, **kwargs)
            return cls.__instance
        else:
            return cls.__instance
```

```python
class Earth:
    
	def __init__(self, *args, **kwargs):
		pass

	def __new__(cls, *args, **kwargs):
		if not getattr(cls, 'INS', None):
			cls.INS = super().__new__(cls, *args, **kwargs)
			return cls.INS
		else:
			return cls.INS
```


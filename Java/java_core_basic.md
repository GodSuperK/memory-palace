# Java 基础语法

## 关键字

被Java语言赋予特定含义的单词, 组成关键字的字母全部小写

![Java KeyWord](images/java_keyword_1.png)

![](images/java_keyword_2.png)

## 注释

```java
/*多行注释
多行注释
多行注释
*/

// 单行注释

/**
文档注释
*/
```

## 数据类型

### 基本数据类型(4类8种)

1. byte(1), short(2), int(4), long(8)
2. float(4), double(4)
3. char(2)
4. boolean(1)

### 默认类型转换

> 一般来说, 我们在运算的时候, 要求参与运算的数据类型必须一样. 小类型的数据类型与大类型的数据类型运算的时候, 需要先转换为大的数据类型,再参与运算

1. boolean 不能转换为其他的数据类型
2. byte, short, char --> int --> long --> float --> double 数据类型: 小变大
3. 两个 byte 类型运算也会同时提升为 int 类型
4. 字符串和其他数据类型做+ ,结果是字符串类型, 表示为字符串连接

### 强制类型转换

> 大的数据类型 --> 小的数据类型 

格式: 目标数据类型 变量 = (目标数据类型) (被转换的数据)

### Java字节码反编译软件 jd-gui

[GitHub Address](https://github.com/java-decompiler/jd-gui)



#### 注意:

1. 整数默认int
2. 小数默认double
3. long 要加 L or l
4. float 要加 F or f
5. 作用域: 大括号范围内, 不能有同名变量
6. 没有初始化值的变量不能直接使用
7. 变量运算, 先进行类型提升
8. 常量运算, 先计算结果,再确定类型
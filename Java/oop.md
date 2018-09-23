# Java 面向对象程序设计
> 面向对象程序设计(简称OOP)是当今主流的程序设计范型。面向对象的程序是由对象组成的，每个对象包含对用户公开的特定功能部分和隐藏的实现部分。
程序中的很多对象来自标准库，还有一些是自定义的。究竟是自己构造对象，还是从外界购买对象完全取决于开发项目的预算和时间。但是，从根本上说，只要对象能够满足要求，就不必关心其功能的具体实现过程。
在OOP中，不必关心对象的具体实现，只要能够满足用户的需求即可。

1. 类(class) - 是构造对象的模板或蓝图。由类构造(construct)对象的过程称为创建类的实例(instance)
2. 封装(encapsulation, 有时称为数据隐藏) - 从形式上看，封装不过是将数据和行为组合在一个包中，并对对象的使用者隐藏了数据的实现方式。
对象中的数据称为实例域(instance field), 操纵数据的过程称为方法(method)。对于每个特定的类实例(对象)都有一组特定的实例域值。
这些值的集合就是这个对象的当前状态(state)。无论何时，只要向对象发送一个消息，它的状态就可能发生改变。
实现封装的关键在于绝对不能让类中的方法直接地访问其他类的实例域。程序仅通过对象的方法与对象数据进行交互。
3. 继承(inheritance) - 通过扩展一个类来建立另外一个类的过程。
4. 对象，对象的三个主要特性：
    - 对象的行为(behavior) ---- 可以对对象施加哪些操作？
    - 对象的状态(state) ---- 当施加那些方法时，对象如何项英？
    - 对象标识(identity) ---- 如何辨别具有相同行为与状态的不同对象？
5. 如何编写面向对象程序，从设计类开始，然后再往每个类中添加方法。
识别类的规则是在分析问题的过程中寻找名词，而方法对应着动词。
6. 类之间的关系
    - 依赖(uses-a) 如果一个类的方法操纵另一个类的对象，我们就说一个类依赖于另外一个类。
    - 聚合(has-a) 聚合关系意味着类A的对象包含类B的对象
    - 继承(is-a) 用于表示特殊与一般的关系





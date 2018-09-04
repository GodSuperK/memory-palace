# Java Basic Note

## Java基础概述
一个Java程序可以认为是一系列对象的集合，而这些对象通过调用彼此的方法来协同工作一个Java程序。

1. **对象**: 对象是类的一个实例。
2. **类**: 类是一个模板。
3. **方法**: 方法就是行为，一个类可以有很多方法。
4. **实例变量**: 每个对象都有独特的实例变量，对象的状态由这些实例变量的值决定。

### 编写 Java 程序时应注意以下几点：
 - 大小写敏感。
 - 对于类名，首字母大写, 如果由若干单词组成，则后面的每个单词的首字母都要大写。
 - 对于方法名, 首字母小写，如果由若干单词组成，则后面的每个单词的首字母都要大写。
 - 源文件名必须和类名相同。
 - 主方法入口，所有的java 程序由`public staic void main(String[] args)` 方法开始执行。

### Java 修饰符
1. **访问控制修饰符**: default, public, protected, private
> Java中，可以使用访问控制符来保护对类、变量、方法和构造方法的访问。Java 支持 4 种不同的访问权限。
 - default (即缺省，什么也不写）: 在同一包内可见，不使用任何修饰符。使用对象：类、接口、变量、方法。
 - private: 在同一类内可见。使用对象：变量、方法。 注意：不能修饰类（外部类）
 - public: 对所有类可见。使用对象：类、接口、变量、方法
 - protected : 对同一包内的类和所有子类可见。使用对象：变量、方法。 注意：不能修饰类（外部类）。
 - 接口里的变量都隐式声明为public static final, 而接口里的方法默认情况下访问权限为public
2. **非访问控制修饰符**: final, abstract, strictfp

## Java 变量
1. 局部变量
> 在方法、构造方法或者语句块中定义的变量被称为局部变量。变量声明和初始化都是在方法中，方法结束后，变量就会自动销毁。
2. 成员变量（非静态变量）
> 成员变量是定义在类中，方法体之外的变量。这种变量在创建对象的时候实例化。成员变量可以被类中方法、构造方法和特定类的语句块访问
3. 类变量（静态变量）
> 类变量也声明在类中，方法体之外，但必须声明为static类型。

```java
/*  局部变量
 1. 访问修饰符不能用于局部变量
 2. 局部变量只在声明它的方法、构造方法或者语句块中可见；
 3. 局部变量没有默认值，所以局部变量被声明后，必须经过初始化，才可以使用。 

*/
public class Variable {
    static int allClicks=0;  // 类变量
    String str = "Hello, World!" //实例变量
    public void method() {
	int i = 0;  // 局部变量	
    }
}
```

**局部变量**: 在以下实例中age是一个局部变量。定义在pupAge()方法中，它的作用域就限制在这个方法中。
```java
package com.runoob.test;
 
public class Test{ 
   public void pupAge(){
      int age = 0;
      age = age + 7;
      System.out.println("小狗的年龄是: " + age);
   }
   
   public static void main(String[] args){
      Test test = new Test();
      test.pupAge();
   }
}
```
**实例变量**:
```java
/*
    1. 访问修饰符可以修饰实例变量
    2. 实例变量对于类中的方法、构造方法或者语句块是可见的。一般情况下应该把
		实例变量设为私有。通过使用访问修饰符可以使实例变量对子类可见
    3. 实例变量具有默认值。数值型变量的默认值是0，布尔型变量的默认值是false，
		引用类型变量的默认值是null。变量的值可以在声明时指定，也可以在构造方法中指定；
    4. 实例变量可以直接通过变量名访问。但在静态方法以及其他类中，就应该使用
		完全限定名：ObejectReference.VariableName。
*/
import java.io.*;
public class Employee{
   // 这个实例变量对子类可见
   public String name;
   // 私有变量，仅在该类可见
   private double salary;
   //在构造器中对name赋值
   public Employee (String empName){
      name = empName;
   }
   //设定salary的值
   public void setSalary(double empSal){
      salary = empSal;
   }  
   // 打印信息
   public void printEmp(){
      System.out.println("名字 : " + name );
      System.out.println("薪水 : " + salary);
   }
 
   public static void main(String[] args){
      Employee empOne = new Employee("RUNOOB");
      empOne.setSalary(1000);
      empOne.printEmp();
   }
}
```
**类变量（静态变量）**:
```java
*/*
    1. 静态变量除了被声明为常量外很少使用。常量是指声明为public/private，
		final和static类型的变量。常量初始化后不可改变。
    2. 与实例变量具有相似的可见性。但为了对类的使用者可见，大多数静态变量声明为public类型。
    3. 静态变量可以通过：ClassName.VariableName的方式访问。
    4. 类变量被声明为public static final类型时，类变量名称一般建议使用大写字母。
		如果静态变量不是public和final类型，其命名方式与实例变量以及局部变量的命名方式一致。
*/
import java.io.*;
 
public class Employee {
    //salary是静态的私有变量
    private static double salary;
    // DEPARTMENT是一个常量
    public static final String DEPARTMENT = "开发人员";
    public static void main(String[] args){
    salary = 10000;
        System.out.println(DEPARTMENT+"平均工资:"+salary);
    }
}
```


## Java 数组
“数组是储存在堆上的对象，可以保存多个同类型变量。

## Java 枚举
Java 5.0引入了枚举，枚举限制变量只能是预先设定好的值。使用枚举可以减少代码中的bug。 枚举可以单独声明或者声明在类里面。方法、变量、构造函数也可以在枚举中定义。

## Java 关键字
关键字全部是小写，这些关键字不能用于常量，变量和任何标识符的名称。

## Java 注释
```java
public static void main(String[] args) {
    // 这是单行注释
    /*
	这是第一行注释
	这是第二行注释
	这是第三行注释
    */
}
``` 

## Java 空行
空白行，或者有注释的行, Java编译器都会忽略掉。

## 继承
在Java中，一个类可以由其他类派生。如果你要创建一个类，而且已经存在一个类具有你所需要的属性或方法，那么你可以将新创建的类继承该类。

##  接口
在Java中，接口可理解为对象间相互通信的协议。接口在继承中扮演着很重要的角色。 接口只定义派生要用到的方法，但是方法的具体实现完全取决于派生类。

## 构造方法
每个类都有构造方法。如果没有显式地为类定义构造方法，Java编译器将会为该类提供一个默认构造方法。 在创建一个对象的时候，至少要调用一个构造方法。构造方法的名称必须与类同名，一个类可以有多个构造方法。
```java
public class Puppy {

    public Puppy() {}	

    public Puppy(String name) {}

    }
```

## 创建对象
对象是根据类创建的。在Java 中，使用关键字new来创建一个新的对象。创建对象需要以下三步:
1. **声明**：声明一个对象，包括对象名称和对象类型。
2. **实例化**： 使用关键字来new一个对象
3. **初始化**： 使用new创建对象时，会调用构造方法初始化对象。

```java
public class Puppy {

    public Puppy(String name) {}

    public static void main(String[] args) {
	Puppy puppy = new Puppy("Jack");
    
    }

}
```
## 访问实例变量和方法
```java
public class Puppy{
   int puppyAge;
   public Puppy(String name){
      // 这个构造器仅有一个参数：name
      System.out.println("小狗的名字是 : " + name ); 
   }
 
   public void setAge( int age ){
       puppyAge = age;
   }
 
   public int getAge( ){
       System.out.println("小狗的年龄为 : " + puppyAge ); 
       return puppyAge;
   }
 
   public static void main(String []args){
      /* 创建对象 */
      Puppy myPuppy = new Puppy( "tommy" );
      /* 通过方法来设定age */
      myPuppy.setAge( 2 );
      /* 调用另一个方法获取age */
      myPuppy.getAge( );
      /*你也可以像下面这样访问成员变量 */
      System.out.println("变量值 : " + myPuppy.puppyAge ); 
   }
}

```

## 源文件声明规则
1. 一个源文件中只能有一个public类
2. 一个源文件可以有多个非public类
3. 源文件的名称应该和public的类的类名保持一致
4. 如果一个类定义在某个包中，那么package语句应该在源文件的首行
5. 如果源文件包含import 语句，那么应该放在package语句和类定义之间
6. import 语句和package语句对源文件中定义的所有类都有效。在同一源文件中，不能给不同的类不同的包声名。


## Java 包
包主要用来对类和接口进行分类。

## import 语句
在Java中，如果给出一个完整的限定名，包括包名、类名，那么Java编译器就可以很容易地定位到源代码或者类。Import语句就是用来提供一个合理的路径，使得编译器可以找到某个类。

例如，下面的命令行将会命令编译器载入`java_installation/java/io`路径下的所有类
```java
import java.io.*;
```

## Java 基本数据类型
变量就是申请内存来存储值。也就是说，当创建变量的时候，需要在内存中申请空间。
内存管理系统根据变量的类型为变量分配存储空间，分配的空间只能用来存储该类型数据。
因此，通过定义不同的变量，可以在内存中存储整数、小数或者字符。
Java 的两大数据类型：
1. 内置数据类型
2. 引用数据类型

### 内置数据类型
![](images/basic_type.png)

对于数值类型的基本类型的取值范围，我们无需强制去记忆，因为它们的值都已经以常量的形式定义在对应的包装类中了。
```java
public class PrimitiveTypeTest {  
    public static void main(String[] args) {  
        // byte  
        System.out.println("基本类型：byte 二进制位数：" + Byte.SIZE);  
        System.out.println("包装类：java.lang.Byte");  
        System.out.println("最小值：Byte.MIN_VALUE=" + Byte.MIN_VALUE);  
        System.out.println("最大值：Byte.MAX_VALUE=" + Byte.MAX_VALUE);  
        System.out.println();  
  
        // short  
        System.out.println("基本类型：short 二进制位数：" + Short.SIZE);  
        System.out.println("包装类：java.lang.Short");  
        System.out.println("最小值：Short.MIN_VALUE=" + Short.MIN_VALUE);  
        System.out.println("最大值：Short.MAX_VALUE=" + Short.MAX_VALUE);  
        System.out.println();  
  
        // int  
        System.out.println("基本类型：int 二进制位数：" + Integer.SIZE);  
        System.out.println("包装类：java.lang.Integer");  
        System.out.println("最小值：Integer.MIN_VALUE=" + Integer.MIN_VALUE);  
        System.out.println("最大值：Integer.MAX_VALUE=" + Integer.MAX_VALUE);  
        System.out.println();  
  
        // long  
        System.out.println("基本类型：long 二进制位数：" + Long.SIZE);  
        System.out.println("包装类：java.lang.Long");  
        System.out.println("最小值：Long.MIN_VALUE=" + Long.MIN_VALUE);  
        System.out.println("最大值：Long.MAX_VALUE=" + Long.MAX_VALUE);  
        System.out.println();  
  
        // float  
        System.out.println("基本类型：float 二进制位数：" + Float.SIZE);  
        System.out.println("包装类：java.lang.Float");  
        System.out.println("最小值：Float.MIN_VALUE=" + Float.MIN_VALUE);  
        System.out.println("最大值：Float.MAX_VALUE=" + Float.MAX_VALUE);  
        System.out.println();  
  
        // double  
        System.out.println("基本类型：double 二进制位数：" + Double.SIZE);  
        System.out.println("包装类：java.lang.Double");  
        System.out.println("最小值：Double.MIN_VALUE=" + Double.MIN_VALUE);  
        System.out.println("最大值：Double.MAX_VALUE=" + Double.MAX_VALUE);  
        System.out.println();  
  
        // char  
        System.out.println("基本类型：char 二进制位数：" + Character.SIZE);  
        System.out.println("包装类：java.lang.Character");  
        // 以数值形式而不是字符形式将Character.MIN_VALUE输出到控制台  
        System.out.println("最小值：Character.MIN_VALUE="  
                + (int) Character.MIN_VALUE);  
        // 以数值形式而不是字符形式将Character.MAX_VALUE输出到控制台  
        System.out.println("最大值：Character.MAX_VALUE="  
                + (int) Character.MAX_VALUE);  
    }  
}
```
实际上，JAVA中还存在另外一种基本类型void，它也有对应的包装类 java.lang.Void，不过我们无法直接对它们进行操作。

### 引用数据类型
- 在Java中，引用类型的变量非常类似于C/C++的指针。引用类型指向一个对象，指向对象的变量是引用变量。这些变量在声明时被指定为一个特定的类型，比如 Employee、Puppy 等。变量一旦声明后，类型就不能被改变了。
- 对象、数组都是引用数据类型。
- 所有引用类型的默认值都是null。
- 一个引用变量可以用来引用任何与之兼容的类型。

### Java 常量
常量在程序运行时是不能被修改的。 在 Java 中使用 final 关键字来修饰常量，声明方式和变量类似：
```java
// 虽然常量名也可以用小写，但为了便于识别，通常使用大写字母表示常量。
final double PI = 3.1415927;
```

### 声明变量
```java
int a, b, c;         // 声明三个int型整数：a、 b、c
int d = 3, e = 4, f = 5; // 声明三个整数并赋予初值
byte z = 22;         // 声明并初始化 z
String s = "runoob";  // 声明并初始化字符串 s
double pi = 3.14159; // 声明了双精度浮点型变量 pi
char x = 'x';        // 声明变量 x 的值是字符 'x'。
```

### 类型转换

#### 自动类型转换
> 一般来说, 我们在运算的时候, 要求参与运算的数据类型必须一样. 小类型的数据类型与大类型的数据类型运算的时候, 需要先转换为大的数据类型,再参与运算
1. boolean 不能转换为其他的数据类型
2. byte, short, char --> int --> long --> float --> double 数据类型: 小变大
3. 两个 byte 类型运算也会同时提升为 int 类型
4. 字符串和其他数据类型做+ ,结果是字符串类型, 表示为字符串连接 

#### 强制类型转换
> 大的数据类型 --> 小的数据类型
格式: 目标数据类型 变量 = (目标数据类型) (被转换的数据)




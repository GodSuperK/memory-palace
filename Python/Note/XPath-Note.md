# XPath

> Xpath 是一门在XML文档中查找信息的语言，被用于在XML文档中通过元素和属性进行导航。Xpath既然叫 Path， 就是以路径表达式的形式来指定元素。



## XPath 节点

在XPath中， XML文档是被作为节点树来对待的， 有七种类型的节点：元素、属性、文本、 命名空间、处理指令、注释以及文档（根）节点。树的根被称为文档节点或者根节点。

节点关系：包括父（Parent）、子（Children）、同胞（Sibling）、先辈（Ancestor）、后代（Descendant）

先辈包括（父， 父的父）， 后代包括（子，子的子）

## XPath 语法

XPath 使用路径表达式来选取 XML 文档中的节点或节点集。节点是沿着路径(path)或者步(steps)来选取的。

| 表达式     | 描述                   |
| ---------- | ---------------------- |
| `nodename` | 选取此节点的所有子节点 |
| `/`        | 从根节点选取           |
| `//`       | 选择任意位置的某个节点 |
| `.`        | 选取当前节点           |
| `..`       | 选取当前节点的父节点   |
| `@`        | 选取属性               |

```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
<classroom>
    <student>
        <id>1001</id>
        <name lang='en'>marry</name>
        <age>20</age>
        <country>China</country>
    </student>
    <student>
        <id>1002</id>
        <name lang='en'>jack</name>
        <age>25</age>
        <country>USA</country>
    </student>
</classroom>
```

| 实现效果                                                     | 路径表达式         |
| ------------------------------------------------------------ | ------------------ |
| 选取 classroom 元素的所有子节点                              | classroom          |
| 选取根元素 classroom                                         | /classroom         |
| 选取属于 classroom 的子元素的所有 student 元素               | classroom/student  |
| 选取所有 student 子元素，而不管它们在文档中的位置            | //student          |
| 选择属于 classroom 元素的后代的所有 student 元素，而不管它们位于classroom之下的什么位置 | classroom//student |
| 选取名为 lang 的所有属性                                     | //@lang            |

选取某个特定的节点或者包含某一个指定的值的节点，需要用到谓语，谓语被嵌在方括号中。

| 实现效果                                                     | 路径表达式                       |
| ------------------------------------------------------------ | -------------------------------- |
| 选取属于 classroom 子元素的第一个 student 元素               | /classroom/student[1]            |
| 选取属于 classroom 子元素的最后一个 student 元素             | /classroom/student[last()]       |
| 选取属于 classroom 子元素的倒数第二个 student 元素           | /classroom/student[last()-1]     |
| 选取最前面的两个属于 classroom 元素的子元素的 student 元素   | /classroom/student[position()<3] |
| 选取所有拥有名为 lang 的属性的 name 元素                     | //name[@lang]                    |
| 选取所有 name 元素， 且这些元素拥有值为 eng 的 lang 属性     | //name[@lang='en']               |
| 选取 classroom 元素的所有 studnet 元素， 且其中的 age 元素的值须大于20 | /classroom/student[age>20]       |
| 选取 classroom 元素中的 student  元素的所有 name 元素， 且其中的 age 元素的值须大于20 | /classroom/student[age>20]/name  |

XPath 在进行节点选取的时候可以使用通配符 "*" 匹配未知的元素，同时使用操作符 "|" 一次选取多条路径。

| 实现效果                                                     | 路径表达式                       |
| ------------------------------------------------------------ | -------------------------------- |
| 选取 classroom 元素的所有子元素                              | /classroom/*                     |
| 选取文档中的所有元素                                         | //*                              |
| 选取所有带有属性的name 元素                                  | //name[@*]                       |
| 选取 student 元素的所有name 和 age 元素                      | //student/name \| //studnet/age  |
| 选取属于 classroom 元素的 student 元素的所有 name 元素， 以及文档中的 所有的 age 元素 | /classroom/student/name \| //age |

## XPath 轴

轴定义了所选节点与当前节点之间的树关系。在 Python 爬虫开发中，提取网页中的信息会遇到这种情况： 首先提取到一个节点的信息，然后想在这个节点的基础上提取它的子节点或者父节点，这时候就会用到轴的概念。轴的存在会使提取变得更加灵活和准确。

在说轴的用法之前，需要了解位置路径表达式中的相对位置路径、绝对位置路径和步的概念。位置路径可以是绝对的，也可以是相对的。绝对路径起始于正斜杠（/），而相对路径不会这样。在两种情况中，位置路径均包括一个或多个步，每个步均被斜杠分割： /step/step/...（绝对位置路径），step/step/... （相对位置路径）。

步(step) 包括：轴（axis)、节点测试（node-test）、零个或者更多谓语（predicate），用来更深入地提炼所选的节点集。步的语法为：轴名称::节点测试[谓语]。

| 轴名称             | 含义                                                   |
| ------------------ | ------------------------------------------------------ |
| child              | 选取当前节点的所有子元素                               |
| parent             | 选取当前节点的父节点                                   |
| ancestor           | 选取当前节点的所有先辈（父、祖父等）                   |
| ancestor-or-self   | 选取当前节点的所有先辈（父、祖父等）以及当前节点本身   |
| descendant         | 选取当前节点的所有后代元素（子、孙等）                 |
| descendant-or-self | 选取当前节点的所有后代元素（子、孙等）以及当前节点本身 |
| preceding          | 选取文档中当前节点的开始标记之前的所有节点             |
| following          | 选取文档中当前节点的结束标记之后的所有节点             |
| preceding-sibling  | 选取当前节点之前的所有同级节点                         |
| following-sibling  | 选取当前节点之后的所有同级节点                         |
| self               | 选取当前节点                                           |
| attribute          | 选取当前节点的所有属性                                 |
| namespace          | 选取当前节点的所有命名空间节点                         |

```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
<classroom>
    <student>
        <id>1001</id>
        <name lang='en'>marry</name>
        <age>20</age>
        <country>China</country>
    </student>
    <student>
        <id>1002</id>
        <name lang='en'>jack</name>
        <age>25</age>
        <country>USA</country>
    </student>
    <teacher>
    	<classid>1</classid>
        <name lang="en">tom</name>
        <age>50</age>
        <country>USA</country>
    </teacher>
</classroom>
```

| 实现效果                                                     | 路径表达式                                   |
| ------------------------------------------------------------ | -------------------------------------------- |
| 选取当前 classroom 节点子元素的 teacher 节点                 | `/classroom/child::teacher`                  |
| 选取所有id 节点的父节点                                      | `//id/parent::*`                             |
| 选取所有以 classid 为子节点的祖先节点                        | `//classid/ancestor::*`                      |
| 选取 classroom 节点下的所有后代节点                          | `//classroom/descendant::*`                  |
| 选取所有以 student 为父节点的id 元素                         | `//student/descendant::id`                   |
| 选取所有 classid 元素的祖先节点及本身                        | `//classid/ancestor-or-self::*`              |
| 选取 `/classroom/student`本身及所有后代元素                  | `/classroom/student/descendant-or-self::*`   |
| 选取 `/classroom/teacher`之间的所有同级节点，结果就是选择了所有 student 节点 | `/classroom/teacher/preceding-sibling::*`    |
| 选取`/classroom`中第二个 student之后的所有同级节点，结果就是选择了 teacher 节点 | `/classroom/student[2]/following-sibling::*` |
| 选取`/classroom/teacher/`节点所有之前的节点（除其祖先外），不仅仅是 student 节点，还有里面的子节点 | `/classroom/teacher/preceding::*`            |
| 选取 `/classroom` 中第二个 student 之后的所有节点，结果就是选择了 teacher 节点及其子节点 | `/classroom/student[2]/following::*`         |
| 选取 student 节点， 单独使用没什么意思。主要是跟其他轴一起使用，如 ancestor-or-self, descendant-or-self | `//student/self::*`                          |
| 选取`/classroom/teacher/name`节点下的所有属性                | `/classroom/teacher/name/attribute::*`       |

## XPath 运算符

XPath 表达式可返回节点集、字符串、逻辑值以及数字。

| 运算符 | 描述           | 实例                                    | 含义                                                         |
| ------ | -------------- | --------------------------------------- | ------------------------------------------------------------ |
| \|     | 计算两个节点集 | `//student/name | //student/age`        | 选取 student元素的所有 name 和 age 元素                      |
| +      | 加法           | `/classroom/student[age=19+1]`          | 选取 classroom 元素的所有student 元素，且其中的 age元素的值须等于20 |
| -      | 减法           | `/classroom/student[age=21-1]`          | 同上                                                         |
| *      | 乘法           | `/classroom/student[age=4*5]`           | 同上                                                         |
| div    | 除法           | `/classroom/student[age=40 div 2]`      | 同上                                                         |
| =      | 等于           | `/classroom/student[age=20]`            | 同上                                                         |
| !=     | 不等于         | `/classroom/student[age!=20]`           | 选取 classroom 元素的所有student 元素，且其中的 age元素的值须不等于20 |
| <      | 小于           | `/classroom/student[age<20]`            | 选取 classroom 元素的所有student 元素，且其中的 age元素的值须不小于20 |
| <=     | 小于等于       | `/classroom/student[age<=20]`           | 选取 classroom 元素的所有student 元素，且其中的 age元素的值须小于等于20 |
| >      | 大于           | `/classroom/student[age>20]`            | 选取 classroom 元素的所有student 元素，且其中的 age元素的值须大于20 |
| `>=`   | 大于等于       | `/classroom/student[age>=20]`           | 选取 classroom 元素的所有student 元素，且其中的 age元素的值须大于等于20 |
| or     | 或             | `/classroom/student[age<20 or age>25]`  | 选取 classroom 元素的所有student 元素，且其中的 age元素的值须小于20 或者大于25 |
| and    | 与             | `/classroom/student[age>20 and age<25]` | 选取 classroom 元素的所有student 元素，且其中的 age元素的值须大于20 且小于25 |
| mod    | 计算除法的余数 | 5 mod 2                                 | 1                                                            |


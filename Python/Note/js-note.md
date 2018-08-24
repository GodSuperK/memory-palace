# JS Note

## 基础

### 1. 在 HTML 中插入 JS

```html
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
      
    <script type="text/javascript">
      document.write("Hello, World!");
    </script>
  </body>
</html>
```

### 2. 在 HTML 中引用 JS 外部文件

```js
// script.js
document.write("Hello, World!")
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
      <!-- 引用外部 JS 文件 -->
      <script src="script.js"></script>
  </body>
</html>
```

#### 注意

>  javascript作为一种脚本语言可以放在html页面中任何位置，但是浏览器解释html时是按先后顺序的，所以前面的script就先被执行。比如进行页面显示初始化的js必须放在head里面，因为初始化都要求提前进行（如给页面body设置css等）；而如果是通过事件调用执行的function那么对位置没什么要求的

### 3. 注释

```javascript
// 这里是单行注释
/*
	多行注释
	养成书写注释的良好习惯
*/
```

### 4. 变量

```javascript
// 直接声明变量并赋值
var myage = 22;
// 先声明变量, 再赋值
var myname;
myname = "ABU"
document.write(myname, myage)
```

### 5. 条件判断

```javascript
if (true) {
  document.write("HELLO");
} else {
  document.write("hello");
}
```

### 6. 函数

```javascript
function functionName() {
  
}
functionName();
```

```html
<script src="script.js"></script>
<button type="button" name="button" onclick="functionName()"></button>
```

### 7. 交互

```javascript
// 向页面输出内容
document.write("<h1>Hello, World!</h1>");
// 警告
alert("FBI Warning!");
// 确认, 点击确定, 返回 true, 反之返回false 
var flag = confirm("你确定要离开本页面吗?");
// 提问, 点击确定, 返回 input 中的内容, 反之返回 null
var name = prompt("请输入用户名:")
var password = prompt("请输入口令")
// 打开一个新窗口, 返回一个窗口对象
var new_window = window.open("http://www.imooc.com");
// 关闭当前窗口
window.close()
// 关闭指定窗口
new_window.close()
```

### 数据类型

1. Number

   ```js
   var a = 1;
   var b = "1";
   console.log(typeof a); //查看某个对象的类型
   console.log(typeof NaN); // -> NaN is Number type
   console.log(isNaN(b)); 
   ```

2. String

   ```js
   var b = "feifei";
   console.log(b.length); // 打印字符串的长度
   ```

3. Boolean

   ```js
   var a = true;
   var b = false;
   ```

4. undefined

   ```js
   // var 去声明了变量，但没有赋值
   var c;
   console.log(typeof c); // -> undefined;
   ```

5. null

   ```js
   console.log(typeof null);
   ```

6. object

   ```js
   var a = [1,2,3];
   var b = {"k1":"v1", "k2":"v2"};
   console.log(typeof a);
   console.log(typeof b);
   ```

   



### DOM操作

文档对象模型DOM（Document Object Model）定义访问和处理HTML文档的标准方法。DOM 将HTML文档呈现为带有元素、属性和文本的树结构（节点树）。

 **HTML文档可以说由节点构成的集合，三种常见的DOM节点:**

**1. 元素节点：**上图中`<html>、<body>、<p>`等都是元素节点，即标签。

**2. 文本节点:**向用户展示的内容，如`<li>...</li>`中的JavaScript、DOM、CSS等文本。

**3. 属性节点:**元素属性，如`<a>`标签的链接属性`href="http://www.imooc.com"`。



```javascript
// 通过 id 获取 元素节点对象
var e = document.getElementById("id");
// 通过元素节点对象的 innerHTML 属性 来访问 文本节点
document.write(e.innerHTML);
// 重新修改文本节点的内容
e.innerHTML = "I love JavaScript!";
// 修改属性节点(改变HTML样式) object.style.property = new style;
/*基本属性表
	backgroundColor = "#CCC";
	height = "300px";
	width = "600px";
	color = "red";
	font
	fontFamily
	fontSize = "20px";
	display = "none";  // 此元素不会被显示
	display = "block"; // 此元素将显示为块级元素
*/
e.style.color = "red";
// 取消自己的所有样式修改
e.style = "none";
// 通过修改类名来修改更多的样式 object.className = classname
e.className = "myclass";
```

#### 查找元素节点对象

```js
var tag_list = document.getElementsByTagName(); // -> list
var class_list = document.getElementsByClassName(); // -> list
var name_list = document.getElementsByName(); // -> list
var obj = document.getElementById();  // -> obj

// CSS 选择器 
document.querySelector("div");    // -> select first div 
document.querySelectorAll("div"); // -> select all divs
document.querySelector("#box");   // -> select E node by id
document.querySelectorAll("#box") // -> select all E node by id
document.querySelector(".box");   // -> select E node by class
document.querySelectorAll(".box") // -> select all E node by class
```



#### CSS 样式修改

1. 内联式修改

   ```js
   // 修改单个样式
   var box = getElementByID('box');
   box.style.color="red";
   // 修改多个样式 the first way
   box.style.cssText="height:100px;width:100px;color:yellow;background:black;";
   // 修改多个样式 the second way
   box.className = "myFont";
   ```

2. 修改文本节点

   ```js
   obj.innerText = "Happy"
   ```

3.  修改属性节点

   ```js
   // 合法属性的修改
   // add
   box.className="box";
   // remove
   box.removeAttribute("class")
   // modify
   box.className="up box";
   // query
   console.log(box.className);
   
   // 自定义属性的修改
   box.setAttribute("a", "b"); // 新增a属性,值=b
   box.setAttribute("a", "up");
   console.log(box.hasAttribute("a")); // -> true
   box.removeAttribute("a");
   
   ```

   

#### 鼠标事件

1. 鼠标划入划出

   ```js
   var box2 = document.querySelector(".box2")
   
   box2.onmouseenter=function () {
       box2.style.background="red";
   };
   
   box2.onmouseleave = function () {
     box2.style.background="yellow";  
   };
   ```

2. 鼠标单击和双击

   ```js
   box2.onclick = function () {
       console.log("单击");
   };
   box2.ondblclick = function () {
       console.log("双击");
   };
   ```
3. 下拉列表的选中内容变化事件
    ```js
    box2.onchange = function () {
	console.log("我变了");	
    };
    ```
窗口事件？ window.onresize? 窗口的大小改变了

   

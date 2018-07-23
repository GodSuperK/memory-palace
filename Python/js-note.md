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

# CSS Basics

### How to relationship the css file in html file?

```html
<head>
	<link rel="stylesheet" href="/css/master.css">
</head>
```



### Comment

```css
/* Anything in here is a comment */
```

### Color

```css
selector {
    color: red;
    /*
    Can search color picker on bing.com get other color
    color: #7ced5a;
    color: rgb(124,237,90);
    color: rgba(124,237,90,0.5);
    */
}
```

### Background

```css
selector {
    background-color: gray;
    /*
    background-image: url(image.png);
    background-repeat: no-repeat; repeat; repeat-x; repeat-y; round; space;
    */
}
```

#### Background 简写

```css
/*
background-color
background-position
background-size
background-repeat
background-origin
background-clip
background-attachment
background-image
如果不设置其中的某个值，也不会出问题
*/
body {
    background: #00FF00 url(bgimage.gif) no-repeat fixed top;
}
```

### Border

```css
div {
    border-color: orange;
    border-width: 1px; /* medium; thin; thick; */
    /* dashed; groove; hidden; dotted; none; ridge; solid; */
    border-style: double; 
    
}
```

#### Border 简写

```css
selector {
    border: medium double rgb(250,0,255);
}
```

### Text

```css
selector {
    text-decoration: line-through; /* overline; cursive;*/
    text-align: center;
}
```

### Font

```css
selector {
    font-family: 'Arial'; /* monospace; */
    /*1em = 16px(default font size) 2em = 32px*/
    font-size: 10px;
    font-style: italic;
    font-weight: bold;
}
```

#### 自定义字体

1. [Google Fonts](http://www.googlefonts.cn/)
2. [CSS Font Stack](https://www.cssfontstack.com/)

### 配色方案生成器

[The super fast color schemes generator!](https://coolors.co/)

### Selectors

```html
<div class='divFirst_class' id="divFirst_id">
	<img src="imgage.png" alt="image not found">
    <ul>
        <li>item 1</li>
        <li>item 2</li>
        <li>item 3</li>
    </ul>
    <h4>Heading 4</h4>
    <p>This is a paragraph.</p>
    <a href="https://www.baidu.com">Baidu</a>
    <a href="https://cn.bing.com">Bing</a>
</div>
```

```css
/* id 选择器 */
#divFirst_id {
    border: thin dotted pink;
}

/* 类选择器 */
.divFirst_class {
    border: thin dotted pink;
}

/* 通配符选择器 */
* {
    color: black;
}

/* 相邻兄弟选择器

1. 同一父元素下
2. 选择紧接在一个元素后面的元素
*/
div li + li {
    /* item2 and item3 will be choose */
    color: red;
}
h4 + p {
    /* p will be choose */
    text-decoration: line-through;
}

/* 后代选择器 */
div ul li {
    color: green;
}

/* 属性选择器 */
.divFirst_class a[href="https://cn.bing.com"] {
    color: purple;
}

/* 伪类 */
a:link {color: #FF0000}		/* 未访问的链接 */
a:visited {color: #00FF00}	/* 已访问的链接 */
a:hover {color: #FF00FF}	/* 鼠标移动到链接上 */
a:active {color: #0000FF}	/* 选定的链接 */

/*Specificity cover css style
tag < class < id

*/

```



### Box Model



### Tools

1. Google Browser Inspect
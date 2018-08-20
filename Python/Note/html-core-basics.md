# HTML BASICS



## 基本结构

```html
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    
  </body>
</html>

```

### comment

```html
<!-- Anything here is a comment! -->
```

### Heading

```html
<h1>This is Heading 1</h1>
<h2>This is Heading 2</h2>
<h3>This is Heading 3</h3>
<h4>This is Heading 4</h4>
<h5>This is Heading 5</h5>
<h6>This is Heading 6</h6>
```

### Paragraph

```html
<p>This is paragraph 1 </p>
<p>This is paragraph 2</p>
```

### Bold and Italic

```html
<strong>Bold text</strong>
<em>Italic text</em>
```

### Group Tags

```html
<div class="groupone">
  <h4>This is heading of group one</h4>
  <p>This is group one content</p>
</div>

<span>This is a containter</span>
```

### Lists

```html
<ol>
  <li>ordered list item 1</li>
  <li>ordered list item 2</li>
  <li>ordered list item 3</li>
</ol>

<ul>
  <li>unordered list item 1</li>
  <li>unordered list item 2</li>
  <li>unordered list item 3</li>
</ul>

<ol>
  <li>ordered list item 1</li>
  <li>ordered list item 2</li>
  <ul>
    <li>unordered list item 1</li>
    <li>unordered list item 2</li>
    <li>unordered list item 3</li>
  </ul>
  <li>ordered list item 3</li>
</ol>
```

### Images

```html
<img src="pythonlogo.png" alt="pythonlogo.png not found">
```

### Link

```html
<a href="https://www.python.org">
  <img src="pythonlogo.png" alt="pythonlogo.png not found">
</a>

 <a href="new_file.html">jump to my new_file.html</a>
```

### Table

```html
<table border="1">
      <thead><th>Number</th><th>Color</th><th>Country</th></thead>
      <tbody>
        <tr>
          <td>250</td><td>Red</td><td>China</td>
        </tr>
        <tr>
          <td>250</td><td>Red</td><td>China</td>
        </tr>
        <tr>
          <td>250</td><td>Red</td><td>China</td>
        </tr>
      </tbody>
    </table>
```

### Forms

```html
<form class="" action="index.html" method="post">
      <p><input type="text" name="" value=""></p>
      <p><input type="password" name="" value=""></p>
      <p><input type="email" name="" value=""></p>
      <p><input type="color" name="" value=""></p>
      <p><input type="submit" name="" value="Click me"></p>
    </form>
```

### Label

```html
<form class="" action="https://www.baidu.com" method="post">
      <p><label for=""> Username:
        <input type="text" name="" value="" placeholder="username" required>
      </label>
     </p>

     <p>
       <label for="username2">Username2:</label>
       <input id="username2" type="text" name="Username2" value="" placeholder="username2" required>
     </p>

     <p><input type="submit" name="" value="Submit"> </p>
    </form>
```

### Selections

```html
<form class="" action="index.html" method="get">
      <p>
        <input id="football" type="radio" name="sports" value="football">
        <label for="football">Football</label>

        <input id="pingpang" type="radio" name="sports" value="pingpang">
        <label for="pingpang">PingPang</label>

        <input id="basketball" type="radio" name="sports" value="basketball">
        <label for="basketball">Basketball</label>
      </p>

      <p>
        <select class="" name="city">
          <option value="Shanghai">上海</option>
          <option value="bj">北京</option>
          <option value="nj">南京</option>
        </select>
      </p>

      <textarea name="feedback" rows="8" cols="80"></textarea>
      <p><input type="submit" name="" value="Submit"> </p>
    </form>
```

### Upload File

```html
<form action="index.html" method="post" enctype="multipart/form-data">
    <input type="file">
</form>
```



## Atom Quick Guide

1. <ctrl-/> quick comment 
2. <ctrl-shift-c> copy full path of file


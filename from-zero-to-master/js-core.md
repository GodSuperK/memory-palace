# JavaScript 手记



## 1. 什么是JS？

修改网页的样式

**编写 JS的流程**

1. 布局： HTML+CSS
2. 属性：确定要修改哪些属性
3. 事件：确定用户做哪些操作（产品设计）
4. 编写JS：在事件中，用JS来修改页面元素的样式


## 数据类型转换
1. parseInt() 转为整数
2. parseFloat() 转为浮点数
3. isNaN() 判断是否为NaN
4. == 先转换类型，然后比较
5. === 不转换类型，直接比较

## 变量作用域和闭包
1. 局部变量：函数内定义的变量，只能在自身函数内使用
2. 全局变量：函数体外定义的变量，作用范围在整个 script 标签内
3. 闭包：子函数可以使用父函数的局部变量

## 命名规范，匈牙利命名法
1. 类型前缀
2. 首字母大写

![](pics/js-pics/name_rule.png)

## 运算符

![](pics/js-pics/operator_table.png)

## 程序流程控制
![](pics/js-pics/if_control.png)

## JS 实例

1. [case_1.html](js-src/case_1.html) - 鼠标提示框，鼠标悬浮在元素上，显示提示信息
2. [case_2.html](js-src/case_2.html) - 修改样式
3. [case_3.html](js-src/case_3.html) - 复选框全选，反选
4. [case_4.html](js-src/case_4.html) - 选项卡
5. [case_5.html](js-src/case_5.html) - 简易年历
6. [case_6.html](js-src/case_6.html) - 隔行变色
7. [case_7.html](js-src/case_7.html) - 时间换算


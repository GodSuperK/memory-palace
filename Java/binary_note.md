# Binary

## 2进制
### 如何存储整型？
> 逢2进1
a byte = 8 bit
1K = 1024 byte
1M = 1024K
1G = 1024M
1T = 1024G

a byte can 表示 256 个不同的值 2^8(0~255)
64-bit numbers can 表示
第一位表示正负 1 表示负数 0表示正数

### 如何存储浮点数？
32-bit floating point number
625.9 = 0.6259x10^3
第一位存储符号位
8位存储指数
23位存储有效位数

### 如何存储字符串？
ASCII 1字节编码格式,使用一个字节来表示字符,对英语国家来说够用
Unicode 多字节编码格式， 使用多个字节表示字符，for Chinese and Japanese

## 8进制
使用3个bit位来表示一个8进制位数
010 001 111
 |   |   |
 2   1   7 to 10进制
     |
    217    to 8进制

## 16进制
使用4个bit位来表示一个16进制数
0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F
1000   1111
 |      |
 8      15  to 10进制
    |
   8f    to 16进制

## 在Java中不同进制的数值如何表示
2进制 -0b
8进制 -0
10进制 整数默认10进制
16进制 -0x

## 任意进制的数转为10进制数
位权展开法
12345 = 1x10^5 + 2x10^4 + 3x10^2 + 4x10^1 + 5x10^0
0b100 = 1x2^2 + 0x2^1 + 0x2^0
0100 = 1x8^2 + 0x8^1 + 0x8^0
0x100 = 1x16^2 + 0x16^1 + 0x16^0

## 10进制转为其他进制
使用短除法，除以基数,取余，直到商为0，余数反转
TODO 2.12-2.16

## 任意进制 到 任意进制的转换

1. 使用10进制作为桥梁
2. 拆分组合法

## 有符号数据表示法
在计算机中，有符号数有3种表示法：原码、反码和补码。所有数据的运算都是采用补码进行的。

1. 原码：就是2进制定点表示法，即最高位为符号位，'0' 表示正，'1'表示负，其余位表示数值的大小。
2. 反码：正数的反码与其原码相同；负数的反码是对其原码逐位取反，但符号位除外。
3. 补码：正数的补码与其原码相同；负数的补码是在其反码的末位加1。

## 位运算符
1. 位运算符是2进制数的操作符
2. 要作位运算，需要先将10进制数转为2进制，并求其补码
3. 位运算符：`&, |, ^, ~, <<, >>, >>>`

```java
// & 位与运算符，有0则0，都1才1 (0=false, 1=true)
System.out.println(3 & 4); // Output: 0
// | 位或运算符，有1则1
System.out.println(3 | 4); // Output: 7
// ^ 位异或运算符， 相同则0， 不同则1
System.out.println(3 ^ 4); // Output: 7
// 一个数对另一个数异或两次，结果不变
System.out.println(3 ^ 4 ^ 4); // Output: 3
// ～ 按位取反运算符, 0变1，1变0, (注意，计算后的是补码)
System.out.println(~3); // Output: -4
```

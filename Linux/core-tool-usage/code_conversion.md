# Linux下如何修改txt文件的字符编码
1. file 命令
2. iconv 命令

## 确认文件的编码格式
`file --mime-encoding filename`

## 编码转换
`iconv -f old_encoding -t new_encoding filename`


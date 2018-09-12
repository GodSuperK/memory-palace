# 部署Java应用程序

## Jar 文件
将所有类文件及图像声音等文件打包到 JAR 文件中。每个JAR文件还包含一个用于描述归档特征的清单文件(manifest)。
清单文件被命名为MANIFEST.MF, 它位于JAR文件的一个特殊META-INF子目录中。要想编辑清单文件，需要将希望添加到清单文件中的行放到文本文件中，然后运行命令。
`jar ufm JARFileName MainfestFileName`

```shell
# 创建JAR文件
jar cvf JARFileName [package|*.class]
# 将额外的清单行添加到一个新文件中
echo "Main-Class: package.MainClass" > addition.mf 
# 更新清单文件
jar ufm JARFileName addition.mf

```
执行Jar文件
`java -jar JARFileName`






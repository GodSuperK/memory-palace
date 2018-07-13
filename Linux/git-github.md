# Git & GitHub



## Git

> 实现了版本控制

**Working directory**

**Staging area**

**Repository**

```shell
git init # 初始化 git 仓库,表现为目录下增加了一隐藏文件夹 .git
# 查看 分支下的commit 记录, HEAD 是当前提交的名称, 表示自己的位置
# 不写分支的名字,默认查看当前分支
git log branch1, branch2 ... 
git log --graph --oneline branch1 branch2 ... # 直观更短的输出
# 查看仓库的状态,显示所处的分支, 最近的提交, Untracked files, 已被追踪并有改动的文件
git status 
git add file # 将文件添加到 staging area
git commit # 将文件提交到 Repository
git diff commit_id1 commit_id2
git diff # 找到 staging area 和 working directory 的文件不同
git branch # 显示所有分支, 以及当前所在的分支
git branch new_name # 创建 new_name 分支
git checkout name # 切换到 name 分支 
git checkout -b new_branch_name # 创建分支,并切换到该分支
git checkout commit_id # 分离HEAD
git show commit_id # 将提交与所在分支中的父提交进行对比
# 将所有指定的分支合并到当前检出的分支中，并为该分支新建一个提交
git merge branch_name1 branch_name2 ... 
# 删除一个不是当前 checkout 的分支
git branch -d branch_name


```



### Branches

#### how to resolve the conflict

`<<<<<<<`: 当前分支中的文件内容

`|||||||`: 文件的原始版本内容

`>>>>>>>`: 其他分支的文件内容



## GitHub

> 一个共享代码的地方, 托管本地仓库

```shell
# 查看远程仓库(GitHub仓库)
git remote
# 添加远程仓库
git remote add origin url # 如果只有一个远程仓库,标准做法是命名origin (存储了远程仓库的位置)
# 输出更多详细信息
git remote -V
# 向远程仓库发送更改, 指定 远程仓库的名称, 和本地分支的名称(表示更新哪个分支)
git push origin master
# 拉取远程仓库的更改到本地仓库, 指定远程仓库的名称, 和远程分支的名称
git pull orgin master
```


# Git & GitHub



## Git

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
git branch name # 创建 name 分支
git checkout name # 切换到 name 分支 
```


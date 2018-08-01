# Linux 软件管理方式

1. 二进制 - 二进制预编译软件包，可以快速安装部署你所需要的软件，但是你不能决定软件的特性
2. 源代码 - 虽然比较耗时，但可以满足你的特殊要求

## 预编译软件包

1. **debian 系**(Debian, Ubuntu) 在线安装

| 命令               | 功能                                  |
| ------------------ | ------------------------------------- |
| `apt install`      | 安装软件包                            |
| `apt remove`       | 移除软件包                            |
| `apt purge`        | 移除软件包并删除配置文件              |
| `apt update`       | 更新软件包列表                        |
| `apt upgrade`      | 升级所有可升级的软件包                |
| `apt autoremove`   | 自动删除不需要的包                    |
| `apt full-upgrade` | 在升级软件包时自动处理依赖关系        |
| `apt search`       | 搜索应用程序                          |
| `apt show`         | 显示安装细节                          |
| `apt list`         | 列出包含条件的包（已安装， 可升级等） |
| `apt edit-sources` | 编辑源列表                            |

2. 安装单个`.deb`软件包文件

```shell
# 安装
sudo dpkg -i package_file.deb
# 卸载
sudo dpkg -r package_name
```




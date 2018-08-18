# Basic Snap Usage

- 如何在系统中安装 snapd 服务

  ```
  snapd是在您的计算机上运行的服务，用于跟踪已安装的snap应用，与商店交互并提供snap命令以便您与其进行交互。 ubuntu 16.04 以后的版本自带，不需要额外安装
  ```

- 如何搜索snap应用

  ```shell
  snap find <snap name>
  ```

- 如何安装snap 应用

  ```shell
  sudo snap install <snap name>
  ```

- 如何执行 snap 应用

  ```shell
  # just run command
  app_name
  ```

- 查看已经安装的snap 应用

  ```shell
  snap list
  ```

- 更新应用

  ```shell
  sudo snap refresh <snap name>
  ```

- 移除应用

  ```shell
  sudo snap remove <snap name>
  ```



**See also**: https://tutorials.ubuntu.com/tutorial/basic-snap-usage#0


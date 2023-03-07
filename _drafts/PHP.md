# PHP

## 安装旧版PHP

Kali官方仓库只有最新版，因此需要添加第三方仓库[DEB.SURY.ORG](https://deb.sury.org/)：

```bash
sudo wget -O /etc/apt/trusted.gpg.d/php.gpg https://packages.sury.org/php/apt.gpg
echo "deb https://packages.sury.org/php/ bullseye main" | sudo tee /etc/apt/sources.list.d/php.list
sudo apt update
```

安装旧版PHP：

```bash
sudo apt install php7.4
sudo apt install php5.6
```

提示缺少依赖：

```bash
The following packages have unmet dependencies:
 php7.4-common : Depends: libffi7 (>= 3.3~20180313) but it is not installable
```

这个包在Debian的仓库里有，不知道为什么Kali仓库没有，于是添加Debian仓库：

```bash
echo "deb http://ftp.cn.debian.org/debian bullseye main" | sudo tee /etc/apt/sources.list.d/debian.list
```

再次尝试安装，成功

## 命令行常用选项

`php [options]`：

```shell
--ini       # 查看配置文件
-i, --info  # 查看详细配置，同phpinfo();
-a          # 交互式shell
-f <file>   # 运行文件 ([f]ile)
-l <file>   # 检查语法 ([l]int)
```

## 显示报错信息

修改配置文件`php.ini`：

```ini
display_errors = On
```

服务器会给客户端返回带有错误信息的html

## VS Code 调试 php

[Installation Wizard](https://xdebug.org/wizard)

安装[Xdebug](https://xdebug.org/docs/install#linux)：

```shell
sudo apt install php-xdebug
```

重启`php`生效
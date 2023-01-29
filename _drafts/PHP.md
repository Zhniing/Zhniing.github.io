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
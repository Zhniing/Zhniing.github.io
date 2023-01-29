## 安装

【[文档](https://www.kali.org/tools/dvwa/)】Kali Linux可以直接使用apt安装：

```bash
sudo apt install dvwa
```

## Web文件

`/usr/share/dvwa`

## 登录

- 初始化登录：

   不需要用户名和密码，直接登录

- 创建数据库后登录：

   - 用户名：`admin`
   - 密码：`password`

## PHP配置

`PHP function allow_url_include: Disabled`

解决方法：

1. 在**当前php环境**使用的`php.ini`文件中，搜索并修改`allow_url_include = On`
2. 重启Web服务器生效 _（`sudo apt install dvwa`方式安装的，可能需要重启计算机）_

查找当前`php.ini`文件的位置：

1. 在`dvwa`网站根目录下新建一个`php`文件
2. 输入`<?php phpinfo(); ?>`
3. 浏览器访问该phpinfo页面
4. `Loaded Configuration File`字段指明了**当前php环境**使用的`php.ini`

## reCAPTCHA

自己生成一组秘钥：

`https://www.google.com/recaptcha/admin/create`

填入`dvwa/config/config.inc.php`
## 需要的php插件

```bash
sudo apt install php-mysql  # 提供数据库连接的相关函数
sudo apt install php-gd  # 提供图像处理的相关函数
```

## 暴露破解

爆破字典：https://github.com/danielmiessler/SecLists

Kali提供了`seclists`命令（其实就是SecLists仓库本身）

## XSS

Cross Site Scripting 跨站脚本攻击

攻击者向网页中注入恶意脚本，用户访问网站就会自动执行

只能危害客户端，不会影响服务器

常见应用：盗取用户Cookie

## CSRF

## SQL注入

使`where`后的条件恒为真

如何实现：先闭合前面的引号或括号，再`or 1=1`
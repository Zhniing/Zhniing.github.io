## 需要的php插件

```bash
sudo apt install php-mysql  # 提供数据库连接的相关函数
sudo apt install php-gd  # 提供图像处理的相关函数
```

## 暴力破解

字典：[SecLists仓库](https://github.com/danielmiessler/SecLists)

Kali提供了`seclists`命令（本质就是[SecLists仓库](https://github.com/danielmiessler/SecLists)）

## XSS

Cross Site Scripting 跨站脚本攻击

攻击者向网页中注入恶意脚本，用户访问网站就会自动执行

只能危害客户端，不会影响服务器

盗取用户Cookie，登录获取用户权限，实施攻击

## CSRF

Cross Site Request Forgery 跨站请求伪造

也叫"one-click attack"，借用用户权限实施攻击，并未实际掌握用户权限

## SQL注入

基本思路：使`where`后的条件恒为真

如何实现：先闭合前面的引号或括号，再`or 1=1`

### select联合查询

`union`（查询的项目数需要相同，即结果的列数相同）：

```sql
select id, username, email from member union select user(), database(), version();  # 获取数据库信息
```

查询时还可以用数字来填充一列：

```sql
select id, email from member union select user(), 3;
```

如何判断一个查询有几列：

```sql
select id, email from member order by 1;  # 根据第1列排序
select id, email from member order by 2;  # 根据第2列排序
select id, email from member order by 3;  # 报错
```

### 执行表达式

利用以下SQL函数，执行表达式，执行结果会在报错中呈现

- `updatexml()`
- `extractvalue()`
- `floor()`

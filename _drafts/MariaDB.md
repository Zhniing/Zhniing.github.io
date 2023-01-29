## 初始化

1.进行一系列初始化配置

```bash
sudo mariadb-secure-installation
```

2.进入数据库

```bash
sudo mariadb
```

3.设置root密码

```bash
GRANT ALL ON *.* TO 'root'@'localhost' IDENTIFIED BY 'password' WITH GRANT OPTION;
```

## 重装数据库（清除原有数据）

```bash
sudo apt purge mariadb-server
sudo rm -rf /var/lib/mysql/
sudo apt install mariadb-server
```

[参考](https://mariadb.com/kb/en/completely-unistall-and-then-reinstall-mariadb-103/)
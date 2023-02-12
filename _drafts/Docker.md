## docker.io 和 docker-ce

都是一样的Docker社区版，但它们处理依赖的方式有所不同：

- docker.io是Debian提供的包，每个依赖都是独立的包，更新时更灵活
- docker-ce是官方([docker.com](https://www.docker.com/))提供的包，所有依赖放一起，最终形成一个包，所有依赖需要一起更新

参考：[What is docker.io in relation to docker-ce and docker-ee (now called "Mirantis Kubernetes Engine")?](https://stackoverflow.com/questions/45023363/what-is-docker-io-in-relation-to-docker-ce-and-docker-ee-now-called-mirantis-k)

## 加入docker组

用户加入docker组后，不用`sudo`就能执行`docker`命令

```shell
sudo usermod -aG docker $USER
id $USER  # 看看添加成功没有
sudo reboot -f  # 重启生效
```

## 换源

https://zhuanlan.zhihu.com/p/291280980

## /etc/hosts

镜像中似乎不会包含该文件，新创建的容器中，`/etc/hosts`的内容都是默认的

## 常用指令

```shell
docker run [OPTIONS] <image>  # 创建容器，并运行
```

OPTIONS

- `--name <name>`指定容器名字
- `--detach`后台运行
- `--publish [ip:][hostPort:]<containerPort>`暴露端口

### 容器操作

```shell
docker ps [OPTIONS]  # 查看已有容器
```

OPTIONS

- `--all`列出所有容器
- `--quiet`仅显示容器ID

```shell
docker rm <container>  # 删除容器
docker start | restart | stop <container>  # 启动、重启、停止容器
```

### 连接容器shell

```bash
docker exec -it 28a5cadfdbbc bash
```

### 连接容器mysql

1. 将3306端口暴露出来

```bash
docker run -dt --name sqli-lab -p 8888:80 -p 8889:3306 acgpiano/sqli-labs:latest
```

2. 将登录用户的`host`字段设置为`%`（修改后重启docker生效）

查看目前的`host`字段值：

```sql
select host, user from mysql.user;
```

执行修改：

```sql
update user set host='%' where host='localhost' and user='root';
```

修改后：

```
+------------+------------------+
| host       | user             |
+------------+------------------+
| %          | root             |
+------------+------------------+
```

`%`表示：允许来自任何IP地址的连接

3. 确保`bind-address`被设置为`0.0.0.0`

```bash
mysqld --verbose --help | grep bind-address
```

```
  --bind-address=name IP address to bind to.
bind-address                                      0.0.0.0
```

参考：[Host '172.18.0.1' is not allowed to connect to this MySQL server #275](https://github.com/docker-library/mysql/issues/275#issuecomment-292208567)

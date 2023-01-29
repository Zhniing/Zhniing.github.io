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

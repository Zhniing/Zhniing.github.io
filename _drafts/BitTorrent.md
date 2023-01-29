## BitTorrent(BT)

种子文件`.torrent`采用[Bencode](https://en.wikipedia.org/wiki/Bencode)进行编码，结构与`json`文件类似，可以[解码并转换](https://github.com/riba2534/bencode)为`json`文件

## Magnet Link

可以[转换](https://github.com/Tsuk1ko/magnet2torrent-js)为种子文件`.torrent`

## Aira2

### 下载磁链没有速度

更改DHT：[参考](https://zhuanlan.zhihu.com/p/265105814#:~:text=2.-,%E8%8E%B7%E5%8F%96DHT%E7%BD%91%E7%BB%9C%E8%8A%82%E7%82%B9%E6%95%B0%E6%8D%AE,-DHT%E9%87%8C%E9%83%BD%E6%98%AF)

直接用别人的[dht.dat](https://down.cheshirex.com/%E6%9D%82%E9%A1%B9/dht.dat)，放在`~/.cache/aria2/dht.dat`

每次下载时，DHT都会变（*不确定*），可以维护一个自用的DHT

### 配置文件

默认配置文件位于`~/.aria2/aria2.conf`

在[WebUI-Aria2](https://github.com/ziahamza/webui-aria2)里保存配置**无法**覆写到上述配置文件

### 启动aria2

```shell
aria2c --enable-rpc --rpc-listen-all
```

### 参考

[Aria2安装与配置](https://jasonkayzk.github.io/2020/05/01/Aria2%E5%AE%89%E8%A3%85%E4%B8%8E%E9%85%8D%E7%BD%AE/)

[Termux 高级终端安装使用配置教程](https://www.sqlsec.com/2018/05/termux.html#Aria2)

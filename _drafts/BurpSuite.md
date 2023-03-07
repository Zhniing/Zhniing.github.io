# Burp Suite

## 配置CA证书

没有CA证书就无法访问https网站

1. 打开Burp Suite后，浏览器访问[burp](http://burp)，下载[CA Certificate](http://burp/cert)

2. 在Chrome中导入CA证书：

   - Settings -> Privacy and security -> Security -> Manage certificates -> Authorities
   - 或直接访问[chrome://settings/certificates](chrome://settings/certificates) -> Authorities

参考：[第四章 SSL和Proxy高级选项](https://t0data.gitbooks.io/burpsuite/content/chapter4.html)

## Chrome浏览器设置代理

测试环境：

- **OS**: Kali Linux 2022.3
- **Chrome**: Version 104.0.5112.101 (Official Build) (64-bit)

代理方式：

- 安装Chrome插件：
  - [Proxy SwitchyOmega](https://chrome.google.com/webstore/detail/proxy-switchyomega/padekgcemlokbadohgkifijomclgjgif)（原Proxy SwitchySharp，推荐）
  - [FoxyProxy Standard](https://chrome.google.com/webstore/detail/foxyproxy-standard/gcknhkkoolaabfmlnjonogaaifnjlfnp)
- 设置启动参数：
  - `google-chrome --proxy="localhost:8080"`

### 问题：无法抓取本地包(127.0.0.1)

通过命令行或[SwitchyOmega](https://chrome.google.com/webstore/detail/proxy-switchyomega/padekgcemlokbadohgkifijomclgjgif)设置代理都无法抓取本地包

~~**对策1**：在代理的Bypass List中添加`<-loopback>`~~

**对策2**：在`/etc/hosts`中，为本地主机添加一个新别名，如：`127.0.1.1 kali`

参考：

1. [Burp Suite User Forum](https://forum.portswigger.net/thread/burp-interception-does-not-work-for-localhost-in-chrome-a787f541#:~:text=%22When%20the%20instructions%20tell%20you%20to%20clear%20the%20exceptions%2C%20enter%20%3C%2Dloopback%3E%20as%20the%20sole%20entry%20and%20save.%22)
2. [Burp Interception does not work for localhost in Chrome](https://stackoverflow.com/a/55850268)
3. [在Chrome71上，Auto Switch配置规则localhost和127.0.0.1无法正确跳转到指定的代理 #1712](https://github.com/FelisCatus/SwitchyOmega/issues/1712#issuecomment-565323980)

## Intruder线程数

Intruder -> Resource pool -> Create new resource pool -> Maximum concurrent requests

> So creating a new resource pool and marking the option of 'maximum concurrent requests' with the value 128, will create 128 threads?
>
> That is correct, yes.
>
> -- [Using Burp Intruder threads option](https://forum.portswigger.net/thread/using-burp-intruder-threads-option-ae100db9)

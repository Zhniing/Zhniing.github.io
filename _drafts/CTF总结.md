## 基础

### 编码解码

编码解码很常用

#### base64

base64是web中常用的编码方法

Ubuntu提供了命令行工具`base64`用于编码和解码

#### md5

md5hash和md5sum不一样，Ubuntu提供了命令行工具`md5sum`

md5hash的python实现：

```python
import hashlib

str = 'root'
for _ in range(500):
    str = str.encode()  # 要编码后才能计算MD5Hash
    str_hash = hashlib.md5(str)  # hash对象
    str = str_hash.hexdigest()
    print(str)
```

## Web

**robots.txt**通常位于网站根目录下，是网站跟爬虫间的协议，用于规定爬虫的权限

### SQL Inject

[万能密码](https://www.gaojiufeng.cn/?id=118)
## 基础

### 编码解码

编码解码很常用

#### base64

base64是web中常用的编码方法

命令行工具：`base64`

编码特征：由于base64编码后的字符长度必须是4的倍数，不足时会在结尾填充多个等号`=`

#### md5

命令行工具：`md5sum`

python实现：

```python
import hashlib

str = 'root'
for _ in range(500):
    str = str.encode()  # 要编码后才能计算md5
    str_hash = hashlib.md5(str)  # hash对象
    str = str_hash.hexdigest()
    print(str)
```

## Web

### robots.txt

`robots.txt`通常位于网站根目录下，是网站跟爬虫间的协议，用于规定爬虫的权限

该文件可能藏有Flag

### SQL Inject

[万能密码](https://www.gaojiufeng.cn/?id=118)

### 猜密码

类似题目：[2019掘安杯web writeup](https://xz.aliyun.com/t/4741#:~:text=%E4%B9%9F%E5%8F%AF%E4%BB%A5%E9%AA%8C%E8%AF%81%E4%B8%80%E4%B8%8B%E3%80%82-,web3,-url%E5%9C%B0%E5%9D%80%EF%BC%9A)

```bash
session_start();
if (isset ($_POST['pwd'])){
	if ($_POST['pwd'] == $_SESSION['pwd'])
        die('Flag:'.$flag);
    else{
        print '<p>不对哦，再猜.</p>';
        $_SESSION['pwd']=time().time();
    }
}else{
    $_SESSION['pwd']=time().time();
}
```

目标：由于无法准确预判时间（`time().time()`），只有使第3行的`if`判断为真

重置会话（删掉Cookie中的`PHPSESSID=hs8553q252pka7alr57ggclk2a`），同时，不输入密码直接点击提交（即`pwd=`，此时第2行的`isset`仍会返回`true`）

如此，第3行将为真：`if(null == null)`

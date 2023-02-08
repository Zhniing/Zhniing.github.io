## UAC确认按钮消失

UAC (User Account Control) 用户账户控制

不要用VirtualBox的Unattended方式安装！

安全启动，打开管理员命令行，将用户`w`添加到管理员组：

```batch
net user
net localgroup administrators w /add
```

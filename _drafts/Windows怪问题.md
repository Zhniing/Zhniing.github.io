## 关盖无法睡眠

**Away Mode**会更改*接通电源时的*__睡眠行为__ :question:

1. 正常睡眠：会断网，并且唤醒时要输密码
2. **Away Mode**开启后：不会断网，只关闭显示屏，而且**唤醒不用输密码**

可以在注册表中修改**AwayModeEnabled**，位于*HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Power*

:expressionless: 安装UU加速器会自动开启**Away Mode**，在加速器设置里叫做*手动休眠不断网*

> -- [笔记本关上盖子无法睡眠怎么解决?](https://www.zhihu.com/question/418166535/answer/2100383127)
>
> -- [What is Away Mode?](https://answers.microsoft.com/en-us/windows/forum/all/what-is-away-mode/2a85fc62-9922-4b2e-be47-60a7ca8b1dc0)
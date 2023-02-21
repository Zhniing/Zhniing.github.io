# DWM

## 安装

```bash
git clone https://git.suckless.org/dwm
cd dwm
make  # 确保config.h的拥有者是用户自己
sudo make clean install
```

## 启动

### 通过startx启动

```bash
sudo apt install xinit
echo "dwm" > ~/.xsession  # 启动图形界面时执行的命令：dwm
startx  # 启动图形界面
```

### 通过DM启动

Display Manager

添加`/usr/share/xsessions/i3.desktop`文件，格式参考：[How can I use LightDM for user-defined sessions?](https://askubuntu.com/a/857420)

## 启动时执行的脚本

*以Debian为例，其他发行版可能会有一些不同*

1. `startx`会执行`~/.xinitrc`脚本，如果不存在，则会执行`/etc/X11/xinit/xinitrc`（详见[`man startx`](https://manpages.ubuntu.com/manpages/kinetic/en/man1/startx.1.html#:~:text=To%20determine%20the%20client%20to%20run%2C%20startx%20looks%20for%20the%20following%20files%2C%20in%20order%3A)）

2. `xinitrc`执行`/etc/X11/Xsession`，不执行`Xsession`会导致很多显示问题：UI字体太小、启动延迟，甚至无法正常显示内容

3. `Xsession`执行`/etc/X11/Xsession.d/*`目录下的脚本：（详见[DEFAULT STARTUP PROCEDURE](https://manpages.ubuntu.com/manpages/kinetic/en/man5/Xsession.5.html#:~:text=DEFAULT%20STARTUP%20PROCEDURE)）

   1. `30x11-common_xresources`：执行`/etc/X11/Xresources/*`和`~/.Xresources` (`allow-user-resources`)
   2. `40x11-common_xsessionrc`：执行`~/.xsessionrc`
   3. `50x11-common_determine-startup`依次查找（执行最先找到的文件）：
      1. `~/.xsession` (`allow-user-xsession`)
      2. `~/.Xsession` (`allow-user-xsession`)
      3. `/usr/bin/x-session-manager`
      4. `/usr/bin/x-window-manager`
      5. `/usr/bin/x-terminal-emulator`

5. `~/.xsessionrc`是Debian用来定义全局环境变量的脚本，kali在该文件中设置HiDPI模式所需的变量

6. `~/.xsession`：启动图形界面需要执行的命令，比如`exec dwm`

   > Note that in the Debian system, what many people traditionally put in the .xinitrc file should go in .xsession instead;
   >
   > -- `man startx`

### 参考

1. [`man Xsession`](https://manpages.ubuntu.com/manpages/kinetic/en/man5/Xsession.5.html)
2. [`man startx`](https://manpages.ubuntu.com/manpages/kinetic/en/man1/startx.1.html)
3. [[SOLVED] Lightdm - cannot figure out how to change default xsession - Debian Wheezy](https://www.linuxquestions.org/questions/linux-newbie-8/lightdm-cannot-figure-out-how-to-change-default-xsession-debian-wheezy-943468/)
4. [How to Setup DWM from suckless.org at Kali Linux / Debian](https://jacekkowalczyk.wordpress.com/2018/11/21/how-to-setup-dwm-from-suckless-org-at-kali-linux-debian/)

### 回顾一下

最开始根据网上（针对Arch的）教程，在`~/.xinitrc`脚本里写入`exec dwm`，然后执行`startx`来启动图像界面，结果直接进入xfce4了，当时完全不知道发生了什么，很懵

当时我的`~/.xinitrc`脚本是从`/etc/X11/xinit/xinitrc`拷贝过来的，想着应该是这个`Xsession`脚本启动了xfce4

看一眼源码，然而太复杂懒得看，直接就把`. /etc/X11/Xsession`注释掉了

```bash
# . /etc/X11/Xsession
exec dwm
```

这次成功进入了DWM，但是软件字体和UI非常小

之后又在网上找到了在`~/.Xresources`中设置DPI的方法，绝大部分软件都能正常显示了

然而有一个基于Qt的音乐播放器[Sayonara](https://sayonara-player.com/)无法显示画面，打开就是一片白，但是从LightDM启动的DWM能正常使用Sayonara

说明LightDM做了一些额外的设置，那么是在哪里做的这些设置呢？LightDM启动DWM时执行了哪些文件？

看了一眼我的`.xinitrc`脚本，心想可能是这个`Xsession`脚本的问题，于是取消注释：

```bash
. /etc/X11/Xsession
# xrdb .Xresources  # 使.Xresources生效
# exec dwm
```

然后执行`startx`，发现Sayonara在xfce环境中是正常的

由于不清楚`startx`的具体流程，就在感觉比较重要的几个脚本中添加了打印语句，来做确定其是否会被执行

然后发现：通过LightDM启动时会执行`Xsession`脚本，说明`Xsession`脚本在启动xfce时还做了一些其他设置

在网上搜索`Xsession`脚本的相关资料，最后找到了[manpage](https://manpages.ubuntu.com/manpages/kinetic/en/man5/Xsession.5.html) (`man Xsession`)

manpage写得很详细，读了manpage后再来看脚本源码，发现轻松了很多

在阅读manpage时了解到还有`~/.xsession`这个脚本，于是：

```bash
echo "dwm" > ~/.xsession
```

简单总结一下：

1. 如何快速找到问题的源头？对于复杂脚本，可以借助`echo`来缕清执行流程
2. 之前不知道`man`还能查看文件的说明；仔细一想，其实命令和脚本文件本质上是一样的

## 缩放

1. 在`.Xresources`中调整DPI可以让大部分软件正常显示
2. 对于仍然很小的软件，设置环境变量或启动参数来针对性调整

### DPI

在`~/.Xresources`中设置DPI和鼠标大小：

```
Xft.dpi: 144
Xcursor.size: 32
```

### 环境变量

kali提供了HiDPI模式，实际上就是设置了以下变量：

```bash
# ~/.config/kali-HiDPI/xsession-settings
export QT_SCALE_FACTOR=2
export XCURSOR_SIZE=48
export GDK_SCALE=2
```

`GDK_SCALE`只支持整数缩放（2倍太大了），小数缩放可以用：

```bash
export QT_SCALE_FACTOR=1.5
export GDK_DPI_SCALE=1.5  # 有时也会失效
```

### 启动参数

**Electron**应用可以设置启动参数：

```
--force-device-scale-factor
```

比如Chrome浏览器：

```bash
google-chrome --force-device-scale-factor=1.5
```

### 参考

1. [HiDPI](https://wiki.archlinux.org/title/HiDPI)
2. [[HiDPI] What would be the best place to patch setenv GDK_DPI_SCALE into?](https://forums.freebsd.org/threads/hidpi-what-would-be-the-best-place-to-patch-setenv-gdk_dpi_scale-into.77287/)
3. [Fractional scaling on Linux Xorg](https://ricostacruz.com/til/fractional-scaling-on-xorg-linux)
4. [[SOLVED\]HD Screen very high resolution dimension - small [BUG]](https://bbs.archlinux.org/viewtopic.php?id=195327)

## Patches

打补丁的命令：

```bash
# 严格依照指定的行数
git apply patch.diff
# 可以有偏移，自动进行搜索
patch < patch.diff
```

The workflow for patching dwm:

`git apply`只能应用在`origin/master`上，因此，每个patch都需要从`origin/master`创建分支，打好补丁后再合并到主分支

```bash
# Patch 1
git checkout -b p1 origin/master
git apply p1.diff

# Patch 2
git checkout -b p2 origin/master
git apply p2.diff

# 将patch分支合并到主分支
git switch master
git merge p1 p2
```

有时还需要手动解决`patch`或`git merge`过程中的发生的冲突

## Burp Suite显示问题

问题：Burp Suite无法占满整个窗口（很多JAVA软件都有这个问题）

解决方案：设置环境变量

```bash
env _JAVA_AWT_WM_NONREPARENTING=1 java -jar burpsuite.jar
```

参考：[FIX: Burpsuite not using full resolution - Burp Suite User Forum](https://forum.portswigger.net/thread/fix-burpsuite-not-using-full-resolution-689ff4d6#:~:text=_JAVA_AWT_WM_NONREPARENTING%3D1)

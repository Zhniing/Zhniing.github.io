# Linux

## Check network

```bash
sudo lshw -class network
```

## Check distribution

```bash
lsb_release -a
cat /etc/os-release
```

## Touchpad

`Devices` -> select `Device` _Touchpad_:

1. `Buttons and Feedback` -> `Buttons` -> `Reverse scroll direction`
2. `Touchpad` -> `General` -> `Tap touchpad to click`

## Check missing firmware

`sudo update-initramfs -u`

## Fix the time conflict

Refer to [this](https://askubuntu.com/questions/169376/clock-time-is-off-on-dual-boot).

### Solution 1: Make Windows use UTC

Download [WindowsTimeFixUTC.reg](https://help.ubuntu.com/community/UbuntuTime?action=AttachFile&do=view&target=WindowsTimeFixUTC.reg) and then double click on it to merge the contents with the registry.

### Solution 2: Make Linux use 'Local' time

```bash
timedatectl set-local-rtc 1
```

## 安装输入法

### 搜狗拼音输入法

[官网](https://shurufa.sogou.com/linux)下载`.deb`包，并安装

`Fcitx Configuration` -> `+` -> `Only Show Current Language` -> search `sogoupinyin`

### Mozc日语输入法

[Mozc](https://github.com/google/mozc)是Google日语输入法的跨平台开源版本

```shell
sudo apt install fcitx-mozc
```

## Set proxy

### Command line

```bash
export http_proxy=http://127.0.0.1:7890
export https_proxy=http://127.0.0.1:7890
```

### Google chrome

```bash
google-chrome-stable --proxy-server="http://127.0.0.1:7890"
```

## Appearance

### plank dock

```bash
sudo apt install plank
```

## 网易云音乐

安装官网的deb包：`netease-cloud-music_1.2.1_amd64_ubuntu_20190428.deb`

运行`netease-cloud-music`报错：

```bash
/opt/netease/netease-cloud-music/netease-cloud-music: /opt/netease/netease-cloud-music/libs/libselinux.so.1: no version information available (required by /lib/x86_64-linux-gnu/libgio-2.0.so.0)
/opt/netease/netease-cloud-music/netease-cloud-music: symbol lookup error: /lib/x86_64-linux-gnu/libgio-2.0.so.0: undefined symbol: g_module_open_full
```

[解决方案](https://tieba.baidu.com/p/7789661083)：

在`/opt/netease/netease-cloud-music/netease-cloud-music.bash`中增加第6行：

```bash
#!/bin/sh
HERE="$(dirname "$(readlink -f "${0}")")"
export LD_LIBRARY_PATH="${HERE}"/libs
export QT_PLUGIN_PATH="${HERE}"/plugins
export QT_QPA_PLATFORM_PLUGIN_PATH="${HERE}"/plugins/platforms
cd /lib/x86_64-linux-gnu/  # 增加这一行
exec "${HERE}"/netease-cloud-music $@
```

## [NetEase-MusicBox](https://github.com/darknessomi/musicbox)

登录账号密码错误

解决方案（[不能登录#195](https://github.com/darknessomi/musicbox/issues/195#issuecomment-181794014)）：

直接在配置文件`～/.netease-musicbox/database.json`中输入`username`、`username`和`user_id`。

_网易云音乐[网页版](https://music.163.com/)`我的主页`的`url`中有`user_id`_

## VLC

### 绿屏

`tools` -> `preferences` -> `Video` -> `Output` -> `X11 video output`

## 微信

优麒麟的软件商店提供了微信的`deb`包：[应用下载-优麒麟｜Linux 开源操作系统](https://www.ubuntukylin.com/applications/)

## Turn bell off

[pcspkr](https://wiki.archlinux.org/title/PC_speaker)

```bash
echo 'blacklist pcspkr' | sudo tee /etc/modprobe.d/pcspkr-blacklist.conf
```

## Remove the black line of plank

`Settings` -> `Window Manger Tweaks` -> `Compositor` -> uncheck `Show shadows under dock windows`

## Enable autostart for Xfce

`Settings` -> `Session and Startup` -> `Applicaiton AutoStart`

The corresponding config file is `~/.config/autostart/plank.desktop`

## Change language

`sudo dpkg-reconfigure locales`

## Install live image

Have Rufus work in DD mode _instead of_ ISO mode.

You will get the following error message when using ISO mode:

> There was a problem reading data. Please make sure you have inserted the installation media correctly. If retrying does not work, you should check the integrity of you installation media (there is an associated entry in the main menu for that).
> Failed to copy file from installation media. Retry?

## Dual boot

1. 没有`Windows`启动项

   解决方案：

   ```bash
   sudo update-grub
   ```

2. 提示：`Warning: os-prober will not be executed to detect other bootable partitions.`

   解决方案：

   在`/etc/default/grub`中，添加：

   ```bash
   GRUB_DISABLE_OS_PROBER=false
   ```

## 网络图标消失

开机后发现没有网络，联网的图标也不见了

尝试重启`NetworkManager`服务：

```shell
sudo service NetworkManager restart
```

如果仍不行，进一步检查如下

通过`ifconfig`，发现wlan0没有开启(**DOWN**)：

```shell
ip addr
1: ...
2: wlan0: <BROADCAST,MULTICAST> mtu 1500 qdisc noqueue state DOWN group default qlen 1000
3: ...
```

尝试开启wlan0：

```shell
sudo ifconfig wlan0 up
SIOCSIFFLAGS: Operation not possible due to RF-kill
```

查看rfkill：

```shell
rfkill list
0: ...
1: phy0: Wireless LAN
        Soft blocked: yes
        Hard blocked: no
2: ...
3: ...
```

解锁：

```shell
sudo rfkill unlock wifi
```

OK！网络图标重新出现在任务栏，可以正常联网！参考：[WiFi hardware blocked. RFkill not working.](https://forums.kali.org/showthread.php?18311-WiFi-hardware-blocked-RFkill-not-working)

## 更改GRUB主题

1. 将*主题文件夹*放到`/boot/grub/themes`目录下，*主题文件夹*内的`theme.txt`定义了主题样式
2. 【先备份一下】在`/etc/default/grub`中修改或添加：`GRUB_THEME="/boot/grub/themes/<你的主题文件夹>/theme.txt"`
3. 执行`sudo update-grub`生效

:exclamation:*对于Kali Linux，需要移除或修改`/etc/default/grub.d/kali-themes.cfg`，否则不会生效*

参考：

1. [Setting up GRUB theme in Kali Linux](https://github.com/VandalByte/grub-tweaks#-setting-up-grub-theme-in-kali-linux)
2. [Grub2 theme tutorial](http://wiki.rosalab.ru/en/index.php/Grub2_theme_tutorial)

## 在开始菜单中添加应用

将`.desktop`文件，放入`/usr/share/applications/`或`~/.local/share/applications/`目录，即可被桌面环境的开始菜单、程序启动器(Rofi)检测到

参考：

1. [Some apps not being listed in menu or "Application Finder"](https://forum.xfce.org/viewtopic.php?id=7966)
2. [Where do I put a .desktop file so the launcher can always show it?](https://askubuntu.com/questions/173958/where-do-i-put-a-desktop-file-so-the-launcher-can-always-show-it)

## 禁用息屏

参考：[Screen turns off after 10 minutes and I can't find out why](https://unix.stackexchange.com/a/329906)

```bash
xset -dpms # Disables Energy Star features
xset s off # Disables screen saver
```

# Kali Linux

## Install kali tool set

`sudo apt install kali-linux-default`

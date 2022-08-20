# Linux

## Check network

```bash
sudo lshw -class|-c network
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

## 安装搜狗输入法

`Fcitx Configuration` -> `+` -> `Only Show Current Language` -> search `sogoupinyin`

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

# Kali Linux

## Turn bell off

```bash
xset b off
```
## Remove the black line of plank

`Settings` -> `Window Manger Tweaks` -> `Compositor` -> uncheck `Show shadows under dock windows`

## Enable autostart for Xfce

`Settings` -> `Session and Startup` -> `Applicaiton AutoStart`

The corresponding config file is `~/.config/autostart/plank.desktop`

## Install kali tool set

`sudo apt install kali-linux-default`

## Change language

`sudo dpkg-reconfigure locales`

## Install live image

Have Rufus work in DD mode _instead of_ ISO mode.

You will get the following error message when using ISO mode:

> There was a problem reading data. Please make sure you have inserted the installation media correctly. If retrying does not work, you should check the integrity of you installation media (there is an associated entry in the main menu for that).
> Failed to copy file from installation media. Retry?

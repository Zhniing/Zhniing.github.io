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

## 输入法

### 搜狗拼音输入法

[官网](https://shurufa.sogou.com/linux)下载`.deb`包，并安装

`Fcitx Configuration` -> `+` -> `Only Show Current Language` -> search `sogoupinyin`

### Mozc日语输入法

[Mozc](https://github.com/google/mozc)是Google日语输入法的跨平台开源版本

```shell
sudo apt install fcitx-mozc
```

### fcitx无法在终端中使用

在`~/.xinitrc`中添加环境变量：

```bash
export GTK_IM_MODULE=fcitx
export QT_IM_MODULE=fcitx
export XMODIFIERS=@im=fcitx
```

参考：[Fcitx](https://wiki.archlinux.org/title/Fcitx#Set_environment_variables_for_IM_modules)

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

## 音乐软件

[sayonara](https://sayonara-player.com/)：播放音乐

[picard](https://picard.musicbrainz.org/)：自动检索元数据

## 挂载Windows分区

```bash
sudo fdisk -l  # 找到需要挂载的分区
sudo mkdir /mnt/c  # 创建挂载目录
sudo ntfs-3g /dev/nvme0n1p3 /mnt/c  # 挂载
```

## WPS

### 字体

从Windows中拷贝字体，`C:\Windows\Fonts`

缺失的符号字体：[BannedPatriot/ttf-wps-fonts](https://github.com/BannedPatriot/ttf-wps-fonts)

1. symbol.ttf
2. wingding.ttf
3. WINGDNG2.ttf
4. WINGDNG3.ttf
5. mtextra.ttf

常用的中文字体：

1. 宋体：simsun.ttc
2. 微软雅黑：msyhbd.ttc, msyhl.ttc, msyh.ttc

# i3wm

## 安装

### 从软件仓库中安装

```bash
sudo apt i3
```

### 从源码安装

```bash
# 先进入源码目录
mkdir build & cd build
meson ..
ninja
sudo ninja install
```

参考：[i3status Compilation](https://github.com/i3/i3status#compilation)

## 常用操作

- 重载配置文件：`$mod Shiftc`
- 退出i3：`$mod Shift e`

```bash
i3-msg restart  # 重启i3wm
i3-msg reload  # 重新加载配置文件
```

## 高分辨率

如何计算合适的DPI：[How to find and change the screen DPI?](https://askubuntu.com/questions/197828/how-to-find-and-change-the-screen-dpi)

设置DPI：[How do I scale i3 window manager for my HiDPI display?](https://unix.stackexchange.com/questions/267885/how-do-i-scale-i3-window-manager-for-my-hidpi-display)

```bash
echo "Xft.dpi: 123" >> ~/.Xresources
```

## 双屏

```bash
xrandr  # 查看当前RandR配置
xrandr --output HDMI-0 --rotate left  # 为指定显示器设置旋转
```

另外：`nvidia-settings`提供了图形化的配置界面，与`xrandr`的效果相同

参考：[X11 多显示器配置：玩转 XRandR](https://harttle.land/2019/12/24/auto-xrandr.html)

## 绑定特殊字符的快捷键

首先需要知道特殊字符的keysym（名字）：

```bash
xev  # 在新窗口中按下`键（ESC下面那个键）

KeyPress event, serial 34, synthetic NO, window 0x6600001,
    root 0x1e3, subw 0x0, time 8901690, (69,554), root:(3861,1187),
    state 0x10, keycode 49 (keysym 0x60, grave), same_screen YES,
    XLookupString gives 1 bytes: (60) "`"
    XmbLookupString gives 1 bytes: (60) "`"
    XFilterEvent returns: False

KeyRelease event, serial 34, synthetic NO, window 0x6600001,
    root 0x1e3, subw 0x0, time 8901770, (69,554), root:(3861,1187),
    state 0x10, keycode 49 (keysym 0x60, grave), same_screen YES,
    XLookupString gives 1 bytes: (60) "`"
    XFilterEvent returns: False
```

可以看到，`` ` ``键的*keysym*是*grave*

参考：[How to Find keycode / keysym of a Key?](http://xahlee.info/linux/linux_show_keycode_keysym.html#:~:text=How%20to%20Find%20keycode%20/%20keysym%20of%20a%20Key%3F)

## 窗口切换

### Scratchpad

类似于Windows terminal的[Quake mode](http://freesoftwaremagazine.com/articles/how_to_use_quake-style_terminals_on_GNU_Linux/#:~:text=Quake%20is%20a%20wildly%20popular%20first%20person%20shooter%20created%20by%20id%20Software.%20In%20the%20game%2C%20there%20is%20a%20terminal%20that%20is%20accessible%20by%20hitting%20the%20~%20key.%20It%20is%20used%20to%20edit%20settings%20and%20variables%2C%20show%20logs%2C%20and%20enter%20commands%20and%20cheats%20(for%20more%2C%20read%20the%20Quake%2Dstyle%20Console%20article%20at%20Wikipedia).)，即通过一个固定的快捷键，来打开或关闭一个特定窗口，参考：[i3 quake terminal](https://konfou.xyz/posts/i3-quake-terminal/)

在`~/.config/i3/config`中添加：

```config
bindsym $mod+grave [class="qterminal"] scratchpad show, resize set 2560 1440, move position 1440px 560px
```

这时需要获取窗口的*class*：

```bash
xprop | grep CLASS
WM_CLASS(STRING) = "x-terminal-emulator", "qterminal"
```

运行后，鼠标会变成十字符号，此时点击一个窗口内的任意位置，得到2个字符串，第一个是*instance*，第二个是*class*

参考：

1. [Scratchpad – Switch to My Favorites](https://whhone.com/posts/i3-switching-windows/#1-scratchpad--switch-to-my-favorites)
2. [How to find application's window class in i3 window manager](https://www.tuxtips.info/linux/how-to-find-applications-window-class-in-i3-window-manager)
3. [i3 User's Guide](https://i3wm.org/docs/userguide.html#command_criteria:~:text=The%20first%20part%20of%20the%20WM_CLASS%20is%20the%20instance%20(%22irssi%22%20in%20this%20example)%2C%20the%20second%20part%20is%20the%20class%20(%22URxvt%22%20in%20this%20example).)

# Rofi

搜索所有已打开的窗口，详见[Match – Switch by What I Know](https://whhone.com/posts/i3-switching-windows/#3-match--switch-by-what-i-know)

# Ranger

查看帮助：`?`或`F1`

## 文本预览语法高亮

根据`$HOME/.config/ranger/scope.sh`脚本，`ranger`会**依次**尝试调用以下程序来预览文本文件：

- `highlight`（推荐）
- `bat`
- `pygmentize`

# 音乐播放

## Music Player Daemon (mpd)

无法启动，报错如下：

```bash
exception: Failed to set group 29: Operation not permitted
```

【解决方案】修改配置文件：

```conf
user "你的用户名"  # 默认为mpd
```

# Kali Linux

## Install kali tool set

`sudo apt install kali-linux-default`

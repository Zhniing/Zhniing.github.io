## i3wm

### 安装

#### 从软件仓库中安装

```bash
sudo apt i3
```

#### 从源码安装

```bash
# 先进入源码目录
mkdir build & cd build
meson ..
ninja
sudo ninja install
```

参考：[i3status Compilation](https://github.com/i3/i3status#compilation)

### 常用操作

- 重载配置文件：`$mod Shiftc`
- 退出i3：`$mod Shift e`

```bash
i3-msg restart  # 重启i3wm
i3-msg reload  # 重新加载配置文件
```

### 高分辨率

如何计算合适的DPI：[How to find and change the screen DPI?](https://askubuntu.com/questions/197828/how-to-find-and-change-the-screen-dpi)

设置DPI：[How do I scale i3 window manager for my HiDPI display?](https://unix.stackexchange.com/questions/267885/how-do-i-scale-i3-window-manager-for-my-hidpi-display)

```bash
echo "Xft.dpi: 123" >> ~/.Xresources
```

### 双屏

```bash
xrandr  # 查看当前RandR配置
xrandr --output HDMI-0 --rotate left  # 为指定显示器设置旋转
```

另外：`nvidia-settings`提供了图形化的配置界面，与`xrandr`的效果相同

参考：[X11 多显示器配置：玩转 XRandR](https://harttle.land/2019/12/24/auto-xrandr.html)

### 绑定特殊字符的快捷键

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

### 窗口切换

#### Scratchpad

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

## Rofi

搜索所有已打开的窗口，详见[Match – Switch by What I Know](https://whhone.com/posts/i3-switching-windows/#3-match--switch-by-what-i-know)

## Ranger

查看帮助：`?`或`F1`

### 文本预览语法高亮

根据`$HOME/.config/ranger/scope.sh`脚本，`ranger`会**依次**尝试调用以下程序来预览文本文件：

- `highlight`（推荐）
- `bat`
- `pygmentize`

## DWM

### 安装

```bash
git clone https://git.suckless.org/dwm
cd dwm
sudo make clean install
```

### 启动

#### 通过startx

```bash
sudo apt install xinit
cp /etc/X11/xinit/xinitrc ~/.xinitrc  # 创建用户配置文件
echo "exec dwm" >> ~/.xinitrc  # 添加dwm到配置文件
startx  # 启动图形界面（需要先退出图形界面）
```

#### 通过DM(Display Manager)

添加`/usr/share/xsessions/i3.desktop`文件，格式参考：[How can I use LightDM for user-defined sessions?](https://askubuntu.com/a/857420)

### Patches

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

### Burp Suite显示问题

问题：Burp Suite无法占满整个窗口

解决方案：设置环境变量

```bash
env _JAVA_AWT_WM_NONREPARENTING=1 java -jar burpsuite.jar
```

参考：[FIX: Burpsuite not using full resolution - Burp Suite User Forum](https://forum.portswigger.net/thread/fix-burpsuite-not-using-full-resolution-689ff4d6#:~:text=_JAVA_AWT_WM_NONREPARENTING%3D1)

## 音乐播放

### Music Player Daemon (mpd)

无法启动，报错如下：

```bash
exception: Failed to set group 29: Operation not permitted
```

【解决方案】修改配置文件：

```conf
user "你的用户名"  # 默认为mpd
```

---
categories:
- Android
last-updated-date: 2022-02-06 00:43:57.860000+08:00
---

# 名词解释

## ROM

> Custom ROM is the name what we call a **Custom OS** made by the Android Development Community. These ROMs Include some special feature that **Stock ROMs** Doesn’t. For example, Enhanced Audio Drivers, Improved Battery, Overclocking options and many additional customizing options. There several popular Custom OSes in the world. Linage OS, CARBON, Resurrection Remix, Cyanogen (Abandoned) are a few examples.
>
> -- [How to Root Android - Samsung Galaxy/Note](https://odindownload.com/root-android/)

## Root

> Root is actually a **user account** with extremely higher administrative power over the phone. Android is based on Linux so it’s the same root user you might familiar with LINUX Systems. Rooting is the process of **acquiring the root user privileges**. The safest way for root privileges is to install necessary files via a custom recovery.
>
> -- [How to Root Android - Samsung Galaxy/Note](https://odindownload.com/root-android/)

## Systemless Root

没有`/system`访问权限的Root

原理：

> 大致是通过**修改boot分区**，使得手机在启动时，**systemless中的文件先作为系统文件加载，然后才加载真正的系统**，达到了不修改system分区而实现修改的效果，比如修改机型或是字体，只需要安装并启用相应的模块，模块存放在systemless里面，就会在手机启动时生效，又因为system本身并没有被修改，只需要禁用模块就可以还原，无需备份原有的配置；而root，也当然就是把root相关的一些文件放在systemless里，取代掉手机系统原本的su文件（SuperSU就是直接修改system里的su文件，而magisk是把su放在systemless中，手机启动时取代系统原有su）。
>
> [什么是systemless？它是以什么形式存在于Android系统中？](https://www.zhihu.com/question/278585502)

优点：

1. 如果更改了`/system`，**OTA更新**时，验证系统完整性就无法通过，可能出现以下情况：

   1. 更新**完整**的系统，顶替掉修改过的`/system`分区，之前的Root就会消失
   2. 无法进行OTA更新
   3. 变砖:fearful:

   因此Systemless Root保证用户在Root后，还能正常进行OTA更新

2. 安全要求较高的APP（如：手机银行），会检查有无Root，已Root的手机被认为不安全，无法运行APP或在使用中限制功能。Systemless Root*可以实现*对特定的APP**隐藏Root**，使用户能够正常使用这些APP

缺点：

由于修改了Boot分区（在哪？）：

- 可能卡在开机Logo画面（小米手机：**卡米**MI），因为无法通过**AVB**？（解锁后效验失败也会继续启动？）
- 启动设备时，可能无法通过**供应商(vendor)驱动校验**，可能提示：*您的设备内部出现了问题*

[教你搞懂目前Root的三種APP](https://www.kocpc.com.tw/archives/145014)

## AVB

**Android Verified Boot**，[Verified Boot](https://source.android.com/security/verifiedboot)的一种*实现*

AVB 是 Android 8.0 增加的一种启动(Boot)方式/流程：先验证一些*重要分区*(system.img, recovery.img, vendor.img, boot.img)的完整性，再启动系统

~~刷了第三方Rec*好像*无法通过AVB验证？修补boot*好像*可以通过AVB验证？~~

AVB2.0增加了一个**vbmeta分区**，其工作原理为：

1. **vbmeta.img**的内容是*待验证分区的Hash值*，并且用私钥（*key0*）进行加密签名，私钥*key0*对应的公钥*key0_pub*被编译进BootLoader里
2. 启动时，BootLoader用*key0_pub*验证签名，确保*vbmeta*是可信的
3. 再用*vbmeta*去验证其他分区的完整性

**dm-verity**(device-mapper-verity) 是 Android 4.4 增加的一个内核功能，AVB 通过调用 dm-verity 实现分区完整性验证（？）

[Android Verified Boot 2.0 -- CSDN](https://blog.csdn.net/rikeyone/article/details/80606147)

[Android Verified Boot 2.0 -- Official Doc](https://android.googlesource.com/platform/external/avb/+/master/README.md)

[Android Verified Boot 2.0 -- 台译](https://www.twblogs.net/a/5c4b53ddbd9eee6e7e06d4fb)

[Implementing dm-verity](https://source.android.com/security/verifiedboot/dm-verity)

## FastBoot/Bootloader

关机后，同时按住**开机键**和**音量下键**，进入Bootloader模式

### BL 锁

**BootLoader**锁，解锁BL锁是ROOT的必要条件

bootloader/fastboot相当于手机上的BIOS，锁住的情况下进入bootloader就会一直卡在*FASTBOOT界面*（？）

小米查看BL锁状态：开发者模式->设备解锁状态

手机进入fastboot模式，连接电脑，运行`fastboot oem device-info`查看解锁状态

## Recovery

> Every android phone contains a small OS-like System called **RECOVERY**. Its job is to reset Phone when you can’t boot normally. But the Android developer community has made some special recovery programs that are capable of doing many things that a normal **stock recovery** Can’t do. Such as installing custom Operating System and install files into the system. Most popular custom recovery is "Team Win Recovery Project" also known as [TWRP](https://twrp.me/). We recommend using this as your recovery rather than using an unpopular buggy one.
>
> -- [How to Root Android - Samsung Galaxy/Note](https://odindownload.com/root-android/)

进入Recovery模式：关机后，同时按住**开机键**和**音量上键**

### Rec

一般指代第三方Recovery，用来替换*原来自带的recovery*，功能更多

可以理解成一个手机上的**刷机工具**，把手机内部存储里的文件刷入系统底层

刷第三方Rec不需要root，只需要BL解锁

*出厂时的recovery*，英文术语叫：**stock recovery**

### TWRP

TeamWin Recovery Project，使用最广的第三方Rec，一个可触摸操作的图形界面recovery，

> Now, Why TWRP over default recovery of Andorid?
> The manufactures of the android devices do not expect from you to install new software images other than their own. So they give very limited features which are mostly used by their service centers. Recovery softwares like TWRP can be used to by any advanced android user so that he/she can do whatever his/her phone since he bought it. :D
>
> -- [Quora Answer](https://www.quora.com/What-is-TWRP-Why-is-it-used/answer/Pratik-Rathod-19?ch=10&share=e412aff0)

[安卓手机如何刷入TWRP_Recovery刷机工具-2021年xda精编版](http://www.romleyuan.com/lec/read?id=470)

双清：一般指**两个Cache**（`Dalvik / ART Cache`和`Cache`）

可以刷入**zip**或**img**文件

## Android "Ramdisk"

> `initramfs`: a section in Android’s boot image that the Linux kernel will use as `rootfs`. People also use the term **ramdisk** interchangeably
>
> -- [Android Booting Shenanigans (#Terminologies)](https://topjohnwu.github.io/Magisk/boot.html#terminologies)

（？）如上所述，虽然叫做[Ramdisk](http://junyelee.blogspot.com/2020/03/ramfs-rootfs-and-initramfs.html)（一种古老的启动方式），实际指的是Linux中的`rootfs`

`ramdisk`，`initramfs`，`rootfs`在Android这好像是同义词？

### rootfs

> 在 Linux 中将一个文件系统与一个存储设备关联起来的过程称为挂载（mount）
>
> 根文件系统被挂载到根目录下“/”上后，在根目录下就有根文件系统的各个目录，文件：/bin /sbin /mnt等，再将其他分区挂接到/mnt目录上，/mnt目录下就有这个分区的各个目录和文件。
>
> rootfs是**基于内存的文件系统**，所有操作都在内存中完成；也没有实际的存储设备，所以**不需要设备驱动程序**的参与。基于以上原因，linux在启动阶段使用rootfs文件系统，当磁盘驱动程序和磁盘文件系统成功加载后，linux系统会将系统根目录从rootfs切换到磁盘文件系统。
>
> -- [浅谈linux中的根文件系统（rootfs的原理和介绍）](https://blog.csdn.net/LEON1741/article/details/78159754)

> rootfs is a special instance of **ramfs**
>
> -- [RAMDISK, RAMFS, TMPFS, ROOTFS, INITRD AND INITRAMFS](http://junyelee.blogspot.com/2020/03/ramfs-rootfs-and-initramfs.html)

*这里的**ram**(ramfs)可以理解成**内存**吧*

## Magisk

[github源码](https://github.com/topjohnwu/Magisk)

完整功能由两部分组成：

- Magisk：核心组件
- Magisk Manager：用于和Magisk核心交互，管理手机的Root权限

22.0版本开始合并了Magisk和Magisk Manager：

> Ever since the first Magisk release, Magisk (the **core** components) and Magisk Manager (the companion **app**) are released separately and isn't necessarily always in sync. This leads to some confusion and a lot of complexity when downloading/installing Magisk through the app. Starting from v22.0, the Magisk app (renamed from Magisk Manager) includes everything it needs within the APK itself, making installation a 100% offline process.
>
> From [Magisk v22.0](https://github.com/topjohnwu/Magisk/releases/tag/v22.0)

> Magisk is nothing without the Magisk Manager app.
>
> From [How To Root Android Free With Magisk](https://androidroothub.jimdofree.com/2019/06/03/how-to-root-android-free-with-magisk/)

### 安装方式

Magisk修补Boot其实是修补Boot镜像中的Ramdisk

因此，对于有Ramdisk的设备，可以直接修补Boot；否则只能修补Recovery（也有例外，取决于OEM的实现方式），这会导致必须从Recovery启动才能使用Magisk [doc](https://topjohnwu.github.io/Magisk/install.html#magisk-in-recovery)

### A/B设备OTA更新，如何保留Magisk(Root)

对于已有Magisk的A/B分区设备，**全量**OTA更新会安装*完整的系统*到*未使用的槽位*（假设Slot B），即使原来Slot B中有Magisk也会被新系统覆盖掉，丢失Magisk

*Magisk APP*提供了【安装到未使用的槽位】，OTA后**不要直接重启**，先在Magisk中【安装到未使用的槽位】，再重启，这样就能保证重启设备后（自动切换槽位），新的分区有Magisk可用

这里重启可能会花较长时间

[Mi11_Series_UpdaterMod](https://github.com/BadFishy/Mi11_Series_UpdaterMod#%E5%9B%9B%E4%B8%BA%E4%BA%86%E5%9C%A8%E6%9B%B4%E6%96%B0%E5%90%8E%E4%BF%9D%E7%95%99-magisk)

### busybox

Magisk自带功能完整的[BusyBox](https://github.com/topjohnwu/Magisk/blob/master/docs/guides.md#busybox)，位于`/data/adb/magisk/busybox`

- vi编辑器：`busybox vi <filename>`

## OTA 更新

> OTA（Over－the－AirTechnology）
>
> **OTA更新**：手机终端通过无线网络下载远程服务器上的升级包，对系统或应用进行升级的技术。
>
> [百度百科](https://baike.baidu.com/item/OTA/1381310)
>
> [百度知道](https://zhidao.baidu.com/question/493144253.html)

什么情况会导致无法正常OTA更新？

1. 刷入第三方TWRP后，**进行OTA更新**，可能会：
   - OTA会下载全量更新包（完整的系统），TWRP会被替换掉
   - 变砖：升级重启时，无限重启进不去
   

MIUI官方ROM下载：[update_miui_ota](https://github.com/mooseIre/update_miui_ota)

## 卡刷

在BL解锁的状态下，通过**Recovery**，把SD卡中的文件刷入系统

如果刷入不同的*系统*（ROM，OS），一般都需要清理很多数据（双清、四清）

如果只刷入*软件包*，如Magisk，就不用清数据

## 线刷

用数据线连接电脑，通过**Fastboot**进行刷机

## 9008/EDL  模式

可以绕过BL锁（？），最底层的刷机方式（又叫*深度刷机*），需要9008线（又叫高通EDL线、救砖线、工程线）

[9008是什么？如何进入9008模式给手机解锁，降级？](https://www.bilibili.com/read/cv205958/)

## QPST

Qualcomm Product Support Tool，高通刷机工具，[QPST Tool](https://qpsttool.com/)

刷机工具，可以把（原厂）固件刷入基于高通芯片组的设备里面

集成([inbuilt](https://androidmtk.com/download-qpst-flash-tool))了QFIL

### QFIL

Qualcomm Flash Image Loader，[QFIL Tool](https://qfiltool.com/)

## A/B 分区

Android 8.0时，Google提供了A/B分区选项，供应商（OEM）可以选择是否启用这项功能

A/B分区就是同时在硬盘上存储了2套系统，进行OTA更新时，实际是在更新另一套系统（当前在A，就更新B，反之亦然），这样就不会影响当前系统的继续使用，在后台静默更新，也叫**无缝更新**(Seamless Updates)

[Treble Check](https://play.google.com/store/apps/details?id=com.kevintresuelo.treble) 这个APP可以可以查看当前设备是否支持A/B分区

`fastboot getvar all`其中

1. `slot-count`：有几个分区（槽）
2. `current-slot`：当前位于哪个分区（槽）

有2种情况会切换分区：

1. 进行OTA更新，然后重启设备，就会自动切换到新更新的分区
2. 使用`fastboot set_active [SLOT]`命令手动切换分区

[How to Check if You’re on Partition Slot A or Slot B?](https://krispitech.com/check-partition-slot-a-b/)

### 刷写镜像

- 【**! 重要 !**】**USB接口**选择非常重要！**USB2.0**的**兼容性**更好，3.0可能会出现各种奇怪的问题
- **不指定**分区`fastboot flash boot xxx.img`会自动刷到当前所在槽位(slot)
- A/B分区的Boot分别为`boot_a`和`boot_b`

### V_A/B 分区

虚拟A/B分区，A/B分区的一种实现方式？

出厂Android 11和V_A/B的机型*一般***没有独立的Recovery分区**，而是被合并进了Boot分区，也就无法使用传统的卡刷方法

## 解密DATA分区

Android 6.0开始对`DATA`分区进行了加密，不解密就无法进行读写，也就无法刷入软件包或ROM系统

根据刷入的第三方Rec，解密方式一般有以下几种：

1. 自带解密的Rec，直接能挂载访问`DATA`分区
2. 打解密补丁包
3. 格式化`DATA`分区

# Android Debug Bridge(adb)

[Android 调试桥 (adb)](https://developer.android.com/studio/command-line/adb)

[下载 SDK Platform Tools](https://developer.android.com/studio/releases/platform-tools)

[ADB Shell](https://adbshell.com/)

## 连接准备

### 有线连接

- Android设备在开发者选项中打开**USB调试**
- Windows电脑安装USB驱动（好像小米解锁工具里的驱动就行）

## adb 命令

`adb --help`查看帮助，有很多手册上没写的命令

`adb devices -l`查看已连接的设备，如果找不到设备可以重启一下adb服务（`adb kill-server`）

`adb disconnect [HOST[:PORT]]`不指定`HOST`就断开所有连接，`PORT`默认`5555`

`adb reboot [bootloader|recovery|edl]`重启到*fastboot*，*recovery*，*edl*模式；不指定模式就重启设备

`adb -t [ID] [command]` ：根据`transport id`选择设备

`adb root`：以root权限*启动*adb

### adb shell

`adb shell`进入交互式shell环境

`ls /system/bin`查看可用命令

`su`获取root权限

`pm list packages`等价于`pm -l`：列出安装的所有应用（包）

`pm path [package]`查看给定包的`.apk`所在路径；也可以在`/data/app`目录下搜索包名（位于乱码目录的*子目录*）

## fastboot 命令

*注意：并不是所有机型都支持全部fastboot命令，某些机型可能不支持特定命令*

`fastboot`的所有命令，需要设备处于fastboot模式下，并且连接到电脑才可以使用

`fastboot --help`查看帮助

查看fastboot模式下的连接设备`fastboot devices`

`fastboot oem device-info`查看解锁状态

`fastboot getvar [unlocked|product|...|all]`显示指定的*bootloader变量*

`fastboot flashing unlock`解锁

`fastboot flash PARTITION [FILENAME]`以镜像文件(.img)`FILENAME`，刷写分区`PARTITION`

`fastboot reboot [bootloader]`重启设备（到fastboot）

`fastboot oem reboot-recovery`重启到Recovery

`fastboot boot xxx.img`**本次**（临时）以`xxx.img`这个boot启动系统（有些机型不支持），以Magisk修补镜像启动可以获得Root权限

## 手机运行ADB

1. Magisk ADB模块：[ADB & Fastboot for Android NDK](https://github.com/Magisk-Modules-Repo/adb-ndk)
2. 被调试的设备应打开【USB调试】，调试本机就打开本机的【USB调试】
3. 任意终端模拟器，输入`su`获取root权限，即可使用adb命令

# 社区

[XDA](https://forum.xda-developers.com/)

[ROM乐园](http://www.romleyuan.com/)

# 实战总结

## 解锁

用fastboot命令解锁前记得关闭锁屏密码，解锁后密码可能失效，导致无法进入系统:sob:。要么[清除密码](https://www.htcp.net/3681.html)，要么格式化`/Data`（密码存里面）

## 刷写镜像

【玄学事件】命令就是`fastboot flash boot xxx.img`没错，默认刷到当前槽位，但由于**未知的神秘原因**刷入失败，重启设备再尝试，成功刷入。开始以为是USB3.0的问题，后面再测试发现3.0也能正常刷入:confounded:。也测试了指定槽位`fastboot flash boot_b xxx.img`，一切正常
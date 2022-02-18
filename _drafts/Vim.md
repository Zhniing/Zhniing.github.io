## 教程

[Vimrc Configuration Guide - How to Customize Your Vim Code Editor with Mappings, Vimscript, Status Line, and More](https://www.freecodecamp.org/news/vimrc-configuration-guide-customize-your-vim-editor/)

## 常用快捷键

`CTRL-X CTRL+F`路径补全 [ref](https://codeyarns.com/tech/2016-10-06-how-to-autocomplete-path-in-vim-insert-mode.html)

`CTRL-<PageDown>`或`gt`下一个tab，`CTRL-<PageUp>`或`gT`上一个tab

## 命令

Normal模式下，按`:`，然后就可以输入各种命令

命令可以不写全，写道`Tab`能自动补全时，就可以直接敲回车了；例：`Explore`，输入`E`，按`Tab`就能补全`Explore`，直接执行`:E`与`:Explore`没有区别

用`%`代表*当前文件名*

`:!<command>`执行命令，会暂停vim，回到Shell，例：`:!ls`

`:f[ile]`显示文件名，总行数，当前位置

`:E[xplore]`打开文件浏览器（Vim自带的），会关闭当前文件

`:Se[xplore]`(**S**plit & **Ex**plore)水平分割一个窗口用来打开`Explore`

`:Ve[xplore]`(**V**ertical Split & **Ex**plore)

## 插件

[vim-plug](https://github.com/junegunn/vim-plug)：插件管理器

## 分屏

垂直分屏（打开指定文件）：`:vs[plit] [file]`或`CTRL-W v`

水平分屏（打开指定文件）：`:sp[lit] [file]`或`CTRL-W s`

调整分屏大小：

- 左右（宽度）：`CTRL-W [N] <` `CTRL-W [N] >`
- 上下（高度）：`CTRL-W [N] +` `CTRL-W [N] -`


## 教程

[Vimrc Configuration Guide - How to Customize Your Vim Code Editor with Mappings, Vimscript, Status Line, and More](https://www.freecodecamp.org/news/vimrc-configuration-guide-customize-your-vim-editor/)

## Buffers, Windows, Tabs

- 一个标签 (Tab) 用来组织多个窗口 (Windows)，可以理解为窗口的布局，每个标签拥有独立的窗口布局
- 一个窗口用来显示一个指定的缓冲区 (Buffer)
- 一个缓冲区就是一个已打开的文件

参考：[Using buffers, windows, and tabs efficiently in Vim](https://dev.to/iggredible/using-buffers-windows-and-tabs-efficiently-in-vim-56jc)

## 常用快捷键

`Ctrl-r 0`粘贴剪贴板0的内容

`.` 重复上一个*更改文件的操作*

`Ctrl-x Ctrl-f`路径补全（路径不能与前面的字符连在一起） [ref](https://codeyarns.com/tech/2016-10-06-how-to-autocomplete-path-in-vim-insert-mode.html)

`Ctrl-PageDown`或`gt`下一个tab，`Ctrl-PageUp`或`gT`上一个tab

`Ctrl-w o`使当前窗口全屏化（关闭其他窗口，仅保留当前窗口，`:h only`）；帮助文档通常分屏呈现，全屏化阅读更方便

### 光标移动

- 移动`N`行：
  - `[N] +`
  - `[N] -`
- 翻页：
  - 下一页：`Ctrl-f` Forwards
  - 上一页：`Ctrl-b` Backwards

### 屏幕调整

- 当前行**置顶**：`zt`
- 当前行**居中**：`zz`（常用于浏览上下文）
- 当前行**置底**：`zb`

### 单词操作

- `ciw` "change inner word" 删除当前单词，并进入*insert*模式
- `diw` "delete inner word" 删除当前单词
- `yiw` "yank inner word" 复制当前单词
- `viwp` "view inner word paste" 用复制的内容替换当前单词（粘贴）

一些扩展：

w或{或"：

- `**w` 分隔符为空格
- `**{` 分隔符为`{}`（操作`{}`的内部）
- `**"` 分隔符为`""`（操作`""`的内部)

i或a:

- `*i*` "inner word" 不包括前后的分隔符
- `*a*` "a word" 包括前后的分隔符

参考：[How to delete a word and go into insert mode in Vim?](https://stackoverflow.com/questions/1379198/how-to-delete-a-word-and-go-into-insert-mode-in-vim)

## 命令

Normal模式下，按`:`，然后就可以输入各种命令

命令可以不写全，写到`Tab`能自动补全时，就可以直接敲回车了； 如：`Explore`，输入`E`，按`Tab`就能补全`Explore`，直接执行`:E`与`:Explore`没有区别

用`%`代表*当前文件名*

`:!<command>`执行命令，会暂停vim，回到Shell，例：`:!ls`

`:f[ile]`显示文件名，总行数，当前位置

`:E[xplore]`打开文件浏览器（Vim自带的），会关闭当前文件

`:Se[xplore]`水平分割一个窗口用来打开`Explore`

`:Ve[xplore]`垂直分割一个窗口用来打开`Explore`

`:reg[isters]`查看剪贴板（暂存器）

`:ls`查看缓冲区

## 插件

[vim-plug](https://github.com/junegunn/vim-plug)：插件管理器

## 分屏

移动窗口（改变布局）：

- 移到最左：`Ctrl-w H`
- 移到最下：`Ctrl-w J`
- 移到最上：`Ctrl-w K`
- 移到最右：`Ctrl-w L`

打开文件:

- 水平分割：`:sp[lit] [file]`
- 竖直分割：`:vs[plit] [file]`

## 缩进

1. 如何缩进：
   - Normal模式：`>>`和`<<`
   - Visual模式：`>`和`<`
2. 缩进长度：

```vim
set shiftwidth=4  " 缩进的长度
set tabstop=4     " 制表符(\t)的长度
set expandtab     " 用空格替换制表符(\t)
```

参考：[Tab settings in Vim](https://arisweedler.medium.com/tab-settings-in-vim-1ea0863c5990)

## NeoVim与vim共享配置

*不推荐，因为Neovim大多用Lua配置，而Vim只支持Vimscript*

1. 查看nvim的`runtimepath`（简写`rtp`）：

```vim
:echo &runtimepath
:echo &rtp
```

1. 在`runtimepath`列出的目录中创建软链（这里选择`~/.config/nvim/`）：

```bash
ln -s ~/.vimrc ~/.config/nvim/init.vim  # 配置文件
ln -s ~/.vim/autoload ~/.config/nvim/autoload  # vim-plug插件
```

参考：[neovim Unknown function: plug#begin · Issue #245 · junegunn/vim-plug · GitHub](https://github.com/junegunn/vim-plug/issues/245#issuecomment-239705687)

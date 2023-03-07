# Zsh

## 基础

### 什么是 zle, zstyle, zmodload ?

### 调试

```bash
set -x  # 打开调试
# 这之间的代码会被调试
set +x  # 关闭调试

set -- qqq www  # 传递参数
echo "$1 $2"
```

## grml-zsh-config

### xsource()函数

源码如下：

```bash
# Check if we can read given files and source those we can.
function xsource () {
    if (( ${#argv} < 1 )) ; then
        printf 'usage: xsource FILE(s)...\n' >&2
        return 1
    fi

    while (( ${#argv} > 0 )) ; do
        [[ -r "$1" ]] && source "$1"
        shift
    done
    return 0
}
```

接下来以如下命令为例，进行说明：

```bash
source a b c
xsource a b c
```

`source`只会执行第一个参数`a`，后续参数`b` `c`会被视为执行`a`时传入的参数：`$1` `$2`

而`xsource`会依次`source`多个文件：

```bash
source a
source b
source c
```

**但这样会导致一个问题：**

在`a` `b` `c`文件中，能读取到`xsource`中的位置参数（`$1` `$2`等等），这些位置参数就是`a` `b` `c`文件名本身，但在这种情况下是没有任何意义的，一旦`a` `b` `c`在文件中调用这些位置参数，就会得到错误的信息

**解决方案：**

1. 把需要使用位置参数的代码放入函数中，因为**函数中的位置参数与外部是独立的**，但`source`不是（这就是导致该问题的元凶）

   ```bash
   # https://unix.stackexchange.com/a/219346
   # enclose the code as a function
   function fun () {
   	# Execute some code which will invoke "$1" "$2" "..."
   }
   
   fun
   ```

2. 把位置参数暂存起来：

   ```bash
   # Stage the positional arguments
   args="$@"
   shift "${#argv}"
   
   # Execute some code which will invoke "$1" "$2" "..."
   
   # Restore the arguments
   [ -n "$args" ] && set -- "$args"
   ```

### prompt

```bash
prompt  # 查看帮助
```

### 参考

1. [What is the key difference between grml zsh config and oh-my-zsh config](https://unix.stackexchange.com/questions/58319/what-is-the-key-difference-between-grml-zsh-config-and-oh-my-zsh-config)
2. [Prompt themes for grml](http://bewatermyfriend.org/p/2013/001/)
3. [Appendix to zsh prompt themes in grml](http://bewatermyfriend.org/p/2013/002/)
4. [grml zshrc: More items for prompts](http://bewatermyfriend.org/p/2013/003/)
5. [如何使用 shell（3/3）—— 配置 zsh](https://a-wing.top/shell/2021/05/10/zsh-config#grml-zsh-config)

## 实用功能

Zsh现在的功能非常丰富，但大多数默认是关闭的，需要手动开启

### push-line

```bash
# https://a-wing.top/shell/2021/05/10/zsh-config#push-line
bindkey "\eq" push-line
```

## Troubleshooting

### 补全

1. 同时补全隐藏文件 (Dotfiles)

```bash
echo "_comp_options+=(globdots)" >> ~/.zshrc
```

1. 不显示特殊目录`.`和`..`

```bash
echo "zstyle ':completion:*' special-dirs false" >> ~/.zshrc
```

参考：

1. [How can I configure zsh completion to show hidden files and folders?](https://unix.stackexchange.com/questions/308315/how-can-i-configure-zsh-completion-to-show-hidden-files-and-folders)
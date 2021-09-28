---
last-updated-date: 2021-08-17 21:44:02+08:00
---

# DOS & CMD

- DOS: The **operating system**.

- CMD: The **shell** that allows you to enter your commands to perform your tasks.

[ref](https://qr.ae/pGkDIh)

# 创建文件

`copy con [file_name]`从标准输入新建文件，`Ctrl+Z`结束输入（`copy con`特有的用法）

# CMD

cmd中，命令的**参数**叫做**开关switch**，写为：斜杠`/`+单个字母，不像Linux用短线`-`

cmd中，命令、开关和环境变量**大小写不敏感**，大写小写是同一个指令

[Windows commands官方文档](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/for)

## 内部命令 & 外部命令

内部命令是集成在`cmd.exe`中的命令，任何时候都可以执行，例如`cd`，`cls`

外部命令是存储在磁盘上的可执行文件，大多存放在`C:\Windows\System32`，通常以`.com`或`.exe`为后缀，如`ping.exe`

[Internal and External Commands](http://cis2.oc.ctc.edu/oc_apps/Westlund/xbook/xbook.php?unit=05&proc=page&numb=5)

## 常用命令

`help`：帮助文档，类似于Linux的`man`：

```batch
help [command]
[command] /?
```

`findstr`：`grep`

`ren`/`rename`：重命名文件

`rmdir`：删除**空**文件夹，`/S`递归删除，可以删除非空文件夹；`/Q`不需要确认(*quiet*)

`choice`：通过`%errorlevel%`获取用户输入的结果，第一个选项为`1`，依次递增

`type`：显示文本文件的内容，Linux`cat`？

`cls`：清屏*clear*

`copy`：合并文件

```batch
copy a.jpg /b + b.txt /a c.jpg

# /b 二进制格式，接在文件后面
# /a ASCII码格式，接在文件后面
# c.jpg 合并后的文件名

copy /b a.mpg + b.jpg c.mpg

# /b 写在最前面，指定所有文件的格式 
```

`tree`：以树状结构打印目录，`-f`显示子目录中的内容

## 脚本

脚本后缀为`.bat`或`.cmd`

手册/教程：

- [ss64 cmd](https://ss64.com/nt/)
- [tacktect: Batch Guide](https://www.tacktech.com/display.cfm?ttid=307)
- [Batch Script Tutorial](https://www.tutorialspoint.com/batch_script/index.htm)

### 命令回显

```batch
@echo [on|off]
```

`echo`表示接下来的是否打印（回显）命令本身，前面的`@`表示这条命令本身不回显

### 注释

```batch
@REM 这里是注释，推荐这种方式
```

`REM`表示后面的命令不会被执行，但会回显；加`@`设置不回显

```batch
:: 这里是注释，不提倡通过label(:)设置注释
```

双冒号`::`，本质上是永远不会被跳转到的`label`，**不会回显**。

`label`所在的行不会被执行，理论上单冒号也能写注释吧？

### 变量

#### 环境变量

查看现有环境变量`set`

设置环境变量`set [<variable>=[<string>]]`，等号`=`两边不能有空格，参数如下：

- `/p`：打印提示(*prompt*)，将用户输入存入变量

- `/a`：将`<string>`当作**数值表达式**计算（可以`+=`），结果存入变量。这个表达式中，`+`和`-`只是用来算操作数的正负号的，可以负负`--`得正

  ```batch
  C:\>set a=1
  C:\>set /a a+=1
  2
  
  C:\>set /a a=1+1
  2
  C:\>set /a a=1--1
  2
  ```

调用全局变量：`%a%`，局部变量`!a!`

#### 变量的运作方式

脚本是**逐语句**执行的，一条复杂语句可能有多行简单语句组成（如`for`语句），cmd每次把一条最外层的**语句**加载到内存中，并进行**预处理**：把语句中所有变量`%a%`替换成环境变量（感觉像C语言的**宏替换**:sweat_smile:）。这样所有的变量就变成了字符串常量（可以理解成写死到代码里了）。如果执行过程中修改了环境变量`%a%`，（**该语句中**）后面引用的`%a%`值也不会改变，因为`%a%`在语句执行前就已经被替换成字符串常量了。只有在后面的**语句**中，才能引用到修改后的变量`%a%`

这种现象叫做***变量延迟***，代码如下：

```batch
@echo off
set a=1
set /a a+=1 && echo %a%
for /l %%i in (1, 1, 3) do (
    set /a a+=1
    echo %a%
)
```

执行结果为：

```batch
1
2
2
2
```

防止***变量延迟***的方法：

在使用变量之**前**（具体位置随意），执行`setlocal EnableDelayedExpansion`，并且使用**感叹号**`!a!`调用延迟变量

```batch
@echo off
setlocal EnableDelayedExpansion
set a=1
set /a a+=1 && echo !a!
for /l %%i in (1, 1, 3) do (
    set /a a+=1
    echo !a!
)
```

#### 局部变量

`setlocal`和`endlocal`声明了一个局部作用域，在里面定义的环境变量`b`，会在`endlocal`时被**销毁**

```batch
setlocal
set b=1
set | findstr b=1
echo b %b%
endlocal
set | findstr b=1
echo b %b%
```

### 引号

bat脚本**仅**在for循环的内容中使用**单引号**：`for /f %%a in ('someCommand or string') do (...)`

其余都是双引号

**含空格**的字符串可以用**双引号**包起来`echo "this is xxx"`，连续字符串可以不用引号`echo abcdef`

[shell吞引号问题](http://teaching.idallen.com/cst8207/13w/notes/440_quotes.html)

cmd变量是宏替换，所以尽量不要在引号外面套引号，可能会出现奇怪的bug:clown_face:

### 值比较

`& rem`表示行尾注释

```batch
set str_quote="aaa"
set str=aaa

if  %str_quote%  == "aaa" (echo eq) else (echo not eq) & rem eq
if "%str_quote%" == "aaa" (echo eq) else (echo not eq) & rem not eq
if  %str_quote%  ==  aaa  (echo eq) else (echo not eq) & rem not eq
if "%str_quote%" ==  aaa  (echo eq) else (echo not eq) & rem not eq
if  %str%  == "aaa" (echo eq) else (echo not eq) & rem not eq
if "%str%" == "aaa" (echo eq) else (echo not eq) & rem eq
if  %str%  ==  aaa  (echo eq) else (echo not eq) & rem eq
if "%str%" ==  aaa  (echo eq) else (echo not eq) & rem not eq
```

感觉字符串变量像是**宏替换**？只在都有引号或都没引号时相等

### errorlevel

一条命令执行完后都会有一个返回值*errorlevel*，**0**表示执行**成功**，其他表示各种错误 [ref](https://www.tutorialspoint.com/batch_script/batch_script_return_code.htm)

通过变量`%errorlevel%`查看上一条指令的返回值

### 命令连接符

#### && 和 ||

连接两条指令，依据第一条指令返回的`errorlevel`，进行与`&&`和或`||`的**短路**运算

```batch
C:\>cd 1 && echo 2
系统找不到指定的路径。

C:\>cd 1 || echo 2
系统找不到指定的路径。
2
```

#### &

连接两条命令，**顺序**执行

```batch
C:\>echo hello & echo world
hello
world
```

#### |

**管道**：前一条命令的标准输出作为后一条命令的输入

```batch
C:\>dir | findstr -i program
2021/06/23  22:56    <DIR>          Program Files
2021/06/23  22:50    <DIR>          Program Files (x86)
```

### for

```batch
for { %% | % }<variable> in (<set>) do (
    <command> [<commandlineoptions>]
)
```

for循环替代变量：bat脚本中用双引号`%%a`，cmd交互式命令中用单引号`%a`

`<set>`：多个对象之间用**空格分隔**，依次执行for，而**不是同时**for所有对象

#### 命令扩展（参数选项）

在关键字`for`后添加如下参数

- `for /f ["options"]`：**逐行**遍历文件

  `"options"`如下：

  - `"tokens=1,3"`：对于每行文件，获取第`1`和第`3`项，默认分隔符为*空格*或*制表符tab*
  - `"delims=,|"`：自定义分隔符`,`或`|`

- `for /r [[drive:]path]`：递归遍历文件夹

`<set>`此时还可以是文件（可多个）、命令（仅一条）

`%%~a`：去掉变量a最外层的引号

`%%~na`：**不含后缀**的文件名，也会去掉外层引号

### goto

冒号`:`开头的行都会被视为标签`label`，执行goto语句可以跳转到指定的`label`

```batch
goto a1
这里随便写
不会被执行
可以用来写注释？
:a1
echo a1
```

但只有**数字和字母开头**（不管后面有什么怪符号）的`label`可以被goto语句识别，所以其他符号开头的`label`由于永远不会被跳转，所以可以写成注释（*不提倡*）

### 数组

假数组:sweat_smile:

### 小技巧

- `pause`：暂停脚本，并打印`请按任意键继续. . . `

- `title`：设置窗口（黑框框）标题

- `mode `：
  
  - `mode con cols=15 lines=20`：设置窗口大小
  
- 打印包含特殊字符的字符串：**转义**符`^`

  ```batch
  setlocal EnableDelayedExpansion
  SET "msg=There are no archives to convert^!"
  ECHO !msg!
  ```

  如果只打印感叹号`!`，还可以禁用延迟扩展`DisableDelayedExpansion`，来避免`!`被当成特殊符号：

  ```batch
  setlocal DisableDelayedExpansion
  ECHO: & ECHO xxxxxx!
  endlocal
  ```

- 自定义`PAUSE`的提示文本

  ```batch
  ECHO Press any key to EXIT... && PAUSE > nul && EXIT
  ```

- 判断变量`a`是否为空，注意`defined`后的变量**不用加双引号**`%a%`

  ```batch
  if defined a echo not null
  ```

- 打印空行

  [How can I echo a newline in a batch file?](https://stackoverflow.com/questions/132799/how-can-i-echo-a-newline-in-a-batch-file#comment51324419_132811)

  ```batch
  C:\>echo hello & echo: & echo batch
  hello
  
  batch
  ```

  `echo:`是什么原理啊？:astonished:

  冒号还可以换成其他分隔符`. , / \`，但都可能引发奇怪的bug：[ss64 - Echo - Echo a blank line](https://ss64.com/nt/echo.html)

### 实战

压缩包格式转换：Rar5 -> 7z

```batch
@ECHO off
@REM rar_to_7z.bat
setlocal EnableDelayedExpansion

@REM 设置archives为空
SET archives=
@REM 遍历当前文件夹下的所有7z
ECHO Finding Rar5 archives in current directory ... & ECHO:
for /f "delims=" %%f in ('dir /b *.7z') do (
    @REM 检查压缩文件类型
    for /f "tokens=1,3" %%a in ('7z t "%%f"') do (
        @REM 查找Rar5压缩包
        if %%a == Type if %%b == Rar5 (
            ECHO %%f: Type = %%b
            SET archives=!archives! "%%f"
        )
    )
)

@REM 判断archives是否为空
if not defined archives (
    SET "msg=There are no archives to convert^!"
    ECHO !msg!
    ECHO Press any key to EXIT...
    PAUSE > nul
    EXIT
)

CHOICE /m "Convert the above archives to 7z?"
if %errorlevel% == 2 EXIT

@REM 执行转换
@REM 遍历archives，默认以空格分隔
for %%a in (%archives%) do (
    @REM 解压到文件夹
    7z x %%a -o%%a.contents
    @REM 重新压缩成7z
    CD %%a.contents
    7z a -t7z ..\"%%~na".7z.tmp *
    CD ..
    @REM 删除解压的临时文件夹
    RMDIR /S /Q %%a.contents
    @REM 重命名原压缩包和新压缩包
    REN %%a %%a.bak
    REN "%%~na".7z.tmp "%%~na".7z
)

@REM 打印转换前的压缩包
ECHO: & ECHO The previous archives have been renamed to *.bak:
DIR /b *.bak
@REM 询问是否删除原压缩包
CHOICE /m "Delete the previous archives(*.bak)?"
if %errorlevel% == 1 DEL *.bak

setlocal DisableDelayedExpansion
ECHO: & ECHO Conversion completed!
endlocal
ECHO Press any key to EXIT... && PAUSE > nul
```

[MASS ZIP, RAR TO 7ZIP RECOMPRESSION BATCH FILE](http://aarmstrong.org/tutorials/mass-zip-rar-to-7zip-recompression-batch-file)

# PowerShell

脚本后缀`.ps1`

# Cmder

更现代化的CMD替代品，移植了部分linux命令

Cmder安装后都要在环境变量中配置**根目录**：`%CMDER_ROOT%`

`Win+R`输入`%CMDER_ROOT%`直接打开文件夹
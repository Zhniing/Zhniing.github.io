[~~一文搞定 Windows Terminal 设置与 zsh 安装【非WSL】~~](https://zhuanlan.zhihu.com/p/455925403) 从`git bash`里面调用`zsh`感觉非常卡

[如何在 windows 上使用 zsh](https://www.v2ex.com/t/703987) 准备试试

[msys2](https://www.msys2.org/)

总结：

- 只要用了`zsh-syntax-highlighting`插件就会很卡
- `msys2`的启动速度比`git bash`里的`zsh`快一些

---

在`msys2`里面用zsh就不卡

在`windows terminal`里面就会很卡

## Windows Terminal 配色

[Using VS Code themes in Windows Terminal](https://blog.anaisbetts.org/vs-code-themes-in-windows-terminal/)

### Gruvbox Dark

```json
// https://ttys3.dev/post/windows-terminal-msys2-mingw64-setup/#42-windows-terminal%E4%B8%BB%E9%A2%98%E5%AE%89%E8%A3%85
// magenta -> purple
{
    "background": "#32302F",
    "black": "#32302F",
    "blue": "#83A598",
    "brightBlack": "#665C54",
    "brightBlue": "#83A598",
    "brightCyan": "#8EC07C",
    "brightGreen": "#B8BB26",
    "brightPurple": "#D3869B",
    "brightRed": "#FB4934",
    "brightWhite": "#FBF1C7",
    "brightYellow": "#FABD2F",
    "cursorColor": "#FFFFFF",
    "cyan": "#8EC07C",
    "foreground": "#D5C4A1",
    "green": "#B8BB26",
    "name": "Gruvbox dark, soft",
    "purple": "#D3869B",
    "red": "#FB4934",
    "selectionBackground": "#FFFFFF",
    "white": "#D5C4A1",
    "yellow": "#FABD2F"
}
```

```json
// https://github.com/mbadolato/iTerm2-Color-Schemes/blob/master/windowsterminal/Gruvbox%20Dark.json
{
    "background": "#1E1E1E",
    "black": "#1E1E1E",
    "blue": "#377375",
    "brightBlack": "#7F7061",
    "brightBlue": "#719586",
    "brightCyan": "#7DB669",
    "brightGreen": "#AAB01E",
    "brightPurple": "#C77089",
    "brightRed": "#F73028",
    "brightWhite": "#E6D4A3",
    "brightYellow": "#F7B125",
    "cursorColor": "#E6D4A3",
    "cyan": "#578E57",
    "foreground": "#E6D4A3",
    "green": "#868715",
    "name": "Gruvbox Dark",
    "purple": "#A04B73",
    "red": "#BE0F17",
    "selectionBackground": "#E6D4A3",
    "white": "#978771",
    "yellow": "#CC881A"
}
```

```json
// https://github.com/ZeusOfTheCrows/gruvbox-everything/blob/main/Terminals/Windows%20Terminal/gruvbox_dark
{
    "background": "#282828",
    "black": "#282828",
    "blue": "#458588",
    "brightBlack": "#928374",
    "brightBlue": "#83A598",
    "brightCyan": "#8EC07C",
    "brightGreen": "#B8BB26",
    "brightPurple": "#D3869B",
    "brightRed": "#FB4934",
    "brightWhite": "#EBDBB2",
    "brightYellow": "#FABD2F",
    "cursorColor": "#EBDBB2",
    "cyan": "#689D6A",
    "foreground": "#EBDBB2",
    "green": "#98971A",
    "name": "Gruvbox Dark",
    "purple": "#B16286",
    "red": "#CC241D",
    "selectionBackground": "#3C3836",
    "white": "#A89984",
    "yellow": "#D79921"
},
{
    "background": "#1D2021",
    "black": "#1D2021",
    "blue": "#458588",
    "brightBlack": "#928374",
    "brightBlue": "#83A598",
    "brightCyan": "#8EC07C",
    "brightGreen": "#B8BB26",
    "brightPurple": "#D3869B",
    "brightRed": "#FB4934",
    "brightWhite": "#EBDBB2",
    "brightYellow": "#FABD2F",
    "cursorColor": "#EBDBB2",
    "cyan": "#689D6A",
    "foreground": "#EBDBB2",
    "green": "#98971A",
    "name": "Gruvbox Dark [Hard]",
    "purple": "#B16286",
    "red": "#CC241D",
    "selectionBackground": "#3C3836",
    "white": "#A89984",
    "yellow": "#D79921"
},
{
    "background": "#32302F",
    "black": "#32302F",
    "blue": "#458588",
    "brightBlack": "#928374",
    "brightBlue": "#83A598",
    "brightCyan": "#8EC07C",
    "brightGreen": "#B8BB26",
    "brightPurple": "#D3869B",
    "brightRed": "#FB4934",
    "brightWhite": "#EBDBB2",
    "brightYellow": "#FABD2F",
    "cursorColor": "#EBDBB2",
    "cyan": "#689D6A",
    "foreground": "#EBDBB2",
    "green": "#98971A",
    "name": "Gruvbox Dark [Soft]",
    "purple": "#B16286",
    "red": "#CC241D",
    "selectionBackground": "#3C3836",
    "white": "#A89984",
    "yellow": "#D79921"
}
```

### Nord

```json
{   // Convert from VS Code: Nord extension
    "background": "#2E3440",
    "black": "#3B4252",
    "blue": "#81A1C1",
    "brightBlack": "#4C566A",
    "brightBlue": "#81A1C1",
    "brightCyan": "#8FBCBB",
    "brightGreen": "#A3BE8C",
    "brightPurple": "#B48EAD",
    "brightRed": "#BF616A",
    "brightWhite": "#ECEFF4",
    "brightYellow": "#EBCB8B",
    "cursorColor": "#FFFFFF",
    "cyan": "#88C0D0",
    "foreground": "#D8DEE9",
    "green": "#A3BE8C",
    "name": "Nord",
    "purple": "#B48EAD",
    "red": "#BF616A",
    "selectionBackground": "#FFFFFF",
    "white": "#E5E9F0",
    "yellow": "#EBCB8B"
},
```
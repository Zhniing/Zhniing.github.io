## 导入游戏(ROM)

导入方式的区别：

- 【扫描文件夹】需要匹配数据库（自动命名、获取元素据）；测试发现：只能识别效验和与[DAT-o-MATIC](https://datomatic.no-intro.org/)绿标 (Trusted Dump) 一致的游戏文件
- 【手动扫描】不强制匹配数据库，文件名将直接作为列表中的游戏名；但在指定各种条件后，也会匹配数据库

*注意：【设置】>【列表】>【扫描时不匹配核心】（允许扫描还没有安装游戏核心的游戏文件并将其添加到游戏列表中），默认为关，意思是如果没有下载相应核心，【扫描文件夹】就扫不到游戏文件*

## 缩略图(Thumbnails)

### 自动下载

RetroArch从[http://thumbnails.libretro.com](http://thumbnails.libretro.com)下载缩略图

一键下载所有缩略图：【菜单】>【在线更新】>【列表缩略图更新】

无法下载的情况：（参阅[官方文档](https://docs.libretro.com/guides/roms-playlists-thumbnails/#retroarch-thumbnail-packs)）

- 没有匹配数据库，【信息】>【数据库条目】为空
- [http://thumbnails.libretro.com](http://thumbnails.libretro.com)的NDS目录是空的，因此无法自动下载NDS游戏缩略图

### 手动添加

*搜索引擎关键字：boxart*

按F5打开桌面菜单，在列表中找到游戏，将找到的缩略图拖拽进去即可（只支持png格式）

## 列表管理

清理失效的条目：【设置】>【列表】>【管理列表】>【清除列表】

## 名词解释

校验和、Checksum、哈希值、HASH是同一个东西

## 常见的校验和(Checksum)算法

- MD5：128位，`md5sum`
- SHA-1：160位，`sha1sum`
- SHA-2：
  - SHA-256：256位，`sha256sum`
  - SHA-384：384位，`sha384sum`
  - SHA-512：512位，`sha512sum`

## 命令用法

1. `sha1sum <file>`

   直接计算`<file>`的校验和

2. `sha1sum -c <file.sha1>`

   `<file.sha1>`的格式为：哈希值


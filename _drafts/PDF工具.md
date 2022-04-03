## PDFtk

[Homepage](https://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/)

[TLDR](https://linuxcommandlibrary.com/man/pdftk)

## Ghostscript

[Homepage](https://www.ghostscript.com/)

[TLDR](https://linuxcommandlibrary.com/man/gs)

### 压缩图像

```shell
gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook -dNOPAUSE -dQUIET -dBATCH -sOutputFile=output.pdf input.pdf
```

> [如何减小扫描的 PDF 文件的文件大小？](https://ubuntuqa.com/article/12473.html)
# Wox.Plugin.QiniuMarkdownImage
Wox.Plugin.QiniuMarkdownImage是一个Windows上在Markdown中快速插入图片的小工具，作为[Wox](https://github.com/Wox-launcher/Wox)的插件实现。

可以一键上传图片或截图至七牛云，并将Markdown引用复制到剪切板。


本项目参考了Mac上的工具[qiniu-image-tool](https://github.com/jiwenxing/qiniu-image-tool)。

# 说明
出于两点原因，这个插件没有最终发布。一个是需要用户手动填写七牛云的配置，而wox中python插件无法在插件面板中提供编辑配置的能力，只能自己去插件目录下编辑config.json文件。二是这个插件依赖了两个pip包，wox在安装插件时不会处理插件的依赖。

# 使用
## 1.下载
将本项目clone到wox的插件目录，如`C:\Users\javan\AppData\Local\Wox\app-1.3.424\Plugins`。可以通过 wox设置-插件-选择任意插件-插件目录 找到插件所在目录。

## 2.安装依赖
```bash
pip install pypiwin32
pip install pillow
```

## 3.配置本插件的config.json
几个字段都是七牛云的鉴权字段。

## 4.使用
复制图片文件或截图后，打开wox，输入qn，待出现"图片已上传"字样时，回车确认。

![image](http://opkq28qwn.bkt.clouddn.com/FlndJzimu4uwjb35UtttoVSStpyk)
# -*- coding: utf-8 -*-

from wox import Wox
import json
import os
import tempfile
import win32clipboard as w
from PIL import ImageGrab, Image
from qiniu import Auth, put_file, etag
CF_HDROP = 15
with open(os.path.join(os.path.dirname(__file__),"config.json"), "r") as content_file:
    config = json.loads(content_file.read())
    access_key = config['access_key']
    secret_key = config['secret_key']
    q = Auth(access_key, secret_key)
    bucket_name = config['bucket_name']

class Qiniu(Wox):
    def set_clipboard(self,text):
        w.OpenClipboard()
        w.EmptyClipboard()
        w.SetClipboardText(text)
        w.CloseClipboard()

    # 将剪切板图片存到临时文件，并返回文件路径
    def getImage(self):
        # 先看剪切板有没有图片
        img = ImageGrab.grabclipboard()
        # 如果没有就看有没有复制图片文件
        if not img:
            w.OpenClipboard()
            hasFile = w.IsClipboardFormatAvailable(CF_HDROP)
            if hasFile:
                fileLists=w.GetClipboardData(CF_HDROP)
                if fileLists and len(fileLists)>0 :
                    img = Image.open(fileLists[0])
            w.CloseClipboard()
        imgdir = None
        if img:
            imgdir = tempfile.mkstemp('.jpg')[1]
            img.save(imgdir, 'jpeg')
        return imgdir
    def query(self, query):
        imgdir = None
        results = []
        try:
            imgdir = self.getImage()
        except Exception as e:
            results.append({
                "Title": "something error",
                "SubTitle": str(e),
                "IcoPath":"Images/app.png"
            })
            return results
        if not imgdir:
            results.append({
                "Title": "剪切板中没有图片",
                "SubTitle": "no image in clipboard",
                "IcoPath":"Images/app.png"
            })
            return results
        else:
            key = etag(imgdir)
            token = q.upload_token(bucket_name, key, 3600)
            localfile = imgdir
            ret, info = put_file(token, key, localfile)
            url = config["bucket_url"]+'/'+key
            results.append({
                "Title": "图片已上传",
                "SubTitle": url,
                "IcoPath":imgdir,
                "JsonRPCAction":{
                    "method": "set_clipboard",
                    "parameters":['![image]('+url+')'],
                    "dontHideAfterAction":False
                }
            })
            return results

if __name__ == "__main__":
    Qiniu()
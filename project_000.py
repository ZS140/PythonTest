#-*-coding:utf-8-*-
from PIL import Image,ImageFont,ImageDraw
import sys

headPath = r'C:\\Users\\zengshuai\\Desktop\\'  #头像路径
outPath = r'C:\\Users\\zengshuai\\Desktop\\'  #输出头像路径
fontPath = r"C:\\Windows\\Fonts\\"#字体路径

headFile = 'butterfly.jpg'#头像文件
outFile = 'output.jpg'#输出文件

with Image.open(headPath+headFile) as img:#打开图片
    draw = ImageDraw.Draw(img)#建立画布

    fontSize = min(img.size)//4#根据图片大小确定字体大小

    fontobj = ImageFont.truetype(font=fontPath+"AdobeHeitiStd-Regular.otf",size=fontSize,index=0,encoding="",layout_engine=None)#实例字体对象
    draw.text((img.size[0]-fontSize,0),text='5',fill=(255,0,0),font=fontobj,anchor=None)#用draw对象的text方法添加文字

    img.save(outPath+outFile)



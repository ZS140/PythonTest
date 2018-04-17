import random

import numpy
from PIL import ImageDraw, Image, ImageFont

array = numpy.zeros((100,300,3),dtype=numpy.uint8)
Shape = array.shape
for i in range(Shape[0]):
    for j in range(Shape[1]):
        for k in range(Shape[2]):
            array[i][j][k] = random.randint(0,255)
im = Image.fromarray(array)#生成图片
draw = ImageDraw.Draw(im)#在生成的图片上添加文字
L=[chr(i+65) for i in range(26)]+[chr(i+97) for i in range(26)]
for i in range(4):
    draw.text((i*75+random.randint(0,20),random.randint(0,40)),
              text=random.choice(L),
              fill=(random.randint(0,255),random.randint(0,255),random.randint(0,255)),
              font=ImageFont.truetype(font="C:\Windows\Fonts\RosewoodStd-Regular.otf",size=55,index=0,encoding="",layout_engine=None))
im.save('project_010.jpg')
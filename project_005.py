import os

import re
from PIL import Image

Path = r'C:\\Users\\zengshuai\\Desktop\\changeImg\\'

iphone5_width = 640
iphone5_depth = 1136

list = os.listdir(Path)

for p in list:
    imgPath = Path+p
    print(imgPath)
    with Image.open(imgPath,'r') as img:
        w,h = img.size
        print('w:,',w,'h:%s',h)
        if w>iphone5_width:
            new_h = iphone5_width * h // w
            new_w = iphone5_depth
            new_pic = re.sub(p[:-4], p[:-4] + '_new', p)
            reImg = img.resize((new_w, new_h), Image.ANTIALIAS)
            new_path = Path + new_pic
            reImg.save(new_path)
        if h>iphone5_depth:
            new_w = iphone5_depth * w // h
            new_h = iphone5_depth
            new_pic = re.sub(p[:-4], p[:-4] + '_new', p)
            reImg = img.resize((new_w,new_h),Image.ANTIALIAS)
            new_path = Path + new_pic
            reImg.save(new_path)

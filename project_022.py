import PIL
import re
from PIL import Image


def changeSize(width,height,path):
    with Image.open(path,'r') as f:
        w,h = f.size
        new_w = w
        new_h = h
        if w>width:
            new_h = width * h // w
            new_w = width
            new_img = f.resize((new_w, new_h), Image.ANTIALIAS)
            new_img.save('new_pic.jpg')
        if h>height:
            new_w = height * w // h
            new_h = height
        new_img = f.resize((new_w,new_h),Image.ANTIALIAS)
        new_path = re.sub(path[:-4],path[:-4]+'_new',path)
        new_img.save(new_path)
if __name__ == '__main__':
    changeSize(750,1334,'pic.jpg')
#coding:utf-8
import hashlib

def md_password(password):
    md = hashlib.md5()
    md.update(password.encode('utf-8'))
    return md.hexdigest()
def sha1_password(password):
    sha1 = hashlib.sha1()
    sha1.update(password.encode('utf-8'))
    return sha1.hexdigest()
if __name__ == '__main__':
    password = input("输入一个密码:\n")
    s1 = md_password(password)
    s2 = sha1_password(password)
    print("MD5加密后：",s1)
    print("SHA1加密后：",s2)
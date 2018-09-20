import re

def passwordDetect(password):
    if len(str(password)) < 8:
        return False
    number1 = re.compile(r'\d+')
    if number1.search(password) == None:
        return False
    number2 = re.compile(r'[a-z]+')
    if number2.search(password) == None:
        return False
    number3 = re.compile(r'[A-Z]+')
    if number3.search(password) == None:
        return False
    return True

while True:
    print('请输入测试密码：')
    password = input()
    if passwordDetect(password):
        print('输入正确')
        break
    else:
        print('输入错误')
        print('请重新输入密码（长度不少于8个字符，同时包含大写和小写字符，至少有一位数字。）')
        continue
#! python
# phoneAndEmai.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?      #电话号码前三位数字
    (\s|-|\.)?              #分隔符号
    (\d{3})                 #中间三位数字
    (\s|-|\.)               #分隔符号
    (\d{4})                 #最后四位数字
    (\s*(ext|x|ext\.)\s*(\d{2,5}))?     #分机号
)''', re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+       #邮箱账户名
    @                       #@符号分割
    [a-zA-Z0-9.-]+          #域名
    (\.[a-zA-Z]{2,4})       #顶级域名
)''', re.VERBOSE)

text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))      #复制到剪切板上
    print('Copied to clipboard:')
    print('\n'.join(matches))               #按换行打印
    #print(pyperclip.paste())
else:
    print('No phone numbers or email addresses found.')
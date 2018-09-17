#！ python3
PASSWORDS = {'email': 'j45646',
            'blog': 'luadsfsf',
            'luggage': 'f51615621'
}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: py box.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print(account + '密码已复制到剪切板')
else:
    print('没有找到' + account + '账户名称')
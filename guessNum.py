import random

num = random.randint(1, 20)
print('请猜1-20的数字')
for guessTaken in range(1, 7):
    print('猜数字：')
    guessNum = int(input())

    if guessNum > num:
        print('你猜测的数字大了')
    elif guessNum < num:
        print('你猜测的数字小了')
    else:
        break

if guessNum == num:
    print('恭喜你，你花了'+ str(guessTaken) + '次猜对')
else:
    print('数字是'+ str(num))
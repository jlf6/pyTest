import random

getNum = random.randint(1, 9)
def getAnswer(answerNumber):
    if answerNumber == 1:
        return '这是1'
    elif answerNumber == 2:
        return '这是2'
    elif answerNumber == 3:
        return '这是3'
    elif answerNumber == 4:
        return '这是4'
    elif answerNumber == 5:
        return '这是5'
    elif answerNumber == 6:
        return '这是6'
    elif answerNumber == 7:
        return '这是7'
    elif answerNumber == 8:
        return '这是8'

a = getAnswer(getNum)
print(a)



theBorad = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '
}
def printBorad(borad):
    print(borad['top-L'] + '|' + borad['top-M'] + '|' + borad['top-R'])
    print('-+-+-')
    print(borad['mid-L'] + '|' + borad['mid-M'] + '|' + borad['mid-R'])
    print('-+-+-')
    print(borad['low-L'] + '|' + borad['low-M'] + '|' + borad['low-R'])

turn = 'X'
for i in range(9):
    printBorad(theBorad)
    print('将' + turn + '下到那个位置？')
    move = input()
    theBorad[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printBorad(theBorad)
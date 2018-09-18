catsName = []

while True:
    print('请输入第' + str(len(catsName) + 1) + '个猫的名字：')
    name = input()
    if name == '':
        break
    catsName += [name]

print('所有猫的名字是：')
for i in catsName:
    print(i)
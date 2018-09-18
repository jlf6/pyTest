tableData = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]
def findMaxLen(listData):          #找列表中最大长度
    maxLen = 0
    for i in range(len(listData)):
        if maxLen < len(listData[i]):
            maxLen = len(listData[i])
    return maxLen

subListLen = len(tableData)     #列表tableData中子列表的个数
colwidths = [0]*subListLen      #创建一个列表，元素个数为子列表个数，用于保存每个子列表的最大宽度
listNum = len(tableData[0])     #每个子列表的元素个数（假设相等）

for i in range(subListLen):
    colwidths[i] = findMaxLen(tableData[i])     #每个子列表中的最大宽度

for i in range(listNum):
    for j in range(subListLen):
        print(tableData[j][i].rjust(colwidths[j] + 2), end='')
    print()
spam = ['apples', 'bananas', 'tofu', 'cats']
print(spam)

def commaCode(nameList):
    n = len(nameList)
    newList = nameList[0]
    for i in range(0, n):
        if i == 0:
            newList = newList
        elif i == n-1:
            newList = newList + ',and ' + nameList[i]
        else:
            newList = newList + ',' + nameList[i]
    print(newList)

commaCode(spam)
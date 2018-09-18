def printPicnic(itemsDict, leftwidth, rightwidth):
    print('PICNIC ITEMS'.center(leftwidth + rightwidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftwidth, '.') + str(v).rjust(rightwidth))

picnicItems = {'sandwiches': 4, 'apple': 6, 'cups': 8}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)
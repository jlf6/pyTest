def spam(divideBy):
    try:
        return 42 / divideBy
    except:
        print('错误')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
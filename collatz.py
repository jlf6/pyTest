print('输入数字：')
number = int(input())

def collatz(num):
    if num % 2 == 0:
        return num // 2
    elif num % 2 == 1:
        return 3 * num + 1

while True:
    number = collatz(number)
    print(str(number))
    if number == 1:
        break


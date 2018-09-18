import pprint
message = '你好，我好，大家好才是真的好！'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] += 1

pprint.pprint(count)
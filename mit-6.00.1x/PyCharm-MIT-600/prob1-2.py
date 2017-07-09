s = 'azcbobobegghakl'

count = 0

idx = 0

keyword = 'bob'

while True:
    idx = s.find(keyword, idx)
    if idx >= 0:
        count += 1
        idx += 1

    else:
        break


print("Number of times bob occurs is: %d" % count)
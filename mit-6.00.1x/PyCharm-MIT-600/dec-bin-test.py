num = 0.375
p = 0
while ((2 ** p)* num) % 1 != 0:
    p += 1
    x = int(num*(2 ** p))
result = ''
if x == 0:
    result = '0'
while x > 0:
    result = str(x % 2) + result
    x = x // 2
for i in range(p - len(result)):
    result = '0' + result
result = result[0:-p] + '.' + result[-p:]

print(result)


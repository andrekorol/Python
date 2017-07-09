s = 'abcbcd'

r = ''

c = ''


for char in s:
    if (c == ''):
        c = char

    elif (c[-1] <= char):
        c += char

    elif (c[-1] > char):
        if (len(r) < len(c)):
            r = c
            c = char
        else:
            c = char

if (len(c) > len(r)):
    r = c


print("Longest substring in alphabetical order is: %s" % r)
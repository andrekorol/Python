from sys import argv

script, f = argv

file = open(f, 'w+')

file.seek(9)

print file.tell()

file.write('I like surfing')

print file.read()